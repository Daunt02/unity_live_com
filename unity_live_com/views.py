# -*- coding: utf-8 -*-

from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from mini_charge import forms
#from decimal import *

import requests
import stripe
from django.core.mail import send_mail

#from django.views.generic.base import View
#from django.utils import simplejson as json
#from django.conf import settings
#from django.http import HttpResponse, HttpResponseServerError
#from ribbon import signals as ribbon_signals


def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


def error_404(request):
    return render_response(request, '404.tmpl')


def error_500(request):
    return render_response(request, '500.tmpl')

def mail_by_charge():
    '''
    @todo webhook_signals processing based on charge success, etc.; send e-mail
    based on semantic model of Stripes charge webhooks.
    '''

    return requests.post(
        "https://api.mailgun.net/v2/sandbox7a36881bac8742d39380c7422c133e0a.mailgun.org/messages",
        auth=("api", settings.MAILGUN_API_KEY),
        data={"from": "LM Postmaster<postmaster@sandbox7a36881bac8742d39380c7422c133e0a.mailgun.org>",
              "to": ["nerdfiles <hello@nerdfiles.net"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

def charge(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    token = request.POST['stripe_token']
    amount = request.POST['amount']
    amount = amount.encode('ascii', 'ignore')
    amount = float(amount)
    currency = request.POST['currency']
    description = request.POST['description']
    try:
        mail_by_charge()
        charge = stripe.Charge.create(
            amount=int(amount * 100),
            currency=currency.lower(),
            card=token,
            description=description
        )
    except stripe.CardError as e:
        pass

    return redirect('/gallery')
