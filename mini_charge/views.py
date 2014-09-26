# -*- coding: utf-8 -*-

from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST
from payments import models

import stripe


def _ajax_response(request, template, **kwargs):
    response = {
        "html": render_to_string(
            template,
            RequestContext(request, kwargs)
        )
    }
    if "location" in kwargs:
        response.update({"location": kwargs["location"]})
    return HttpResponse(json.dumps(response), content_type="application/json")


def charge(request, form_class=ChargeForm):
    data = {}
    form = form_class(request.POST)
    if form.is_valid():
        try:
            try:
                customer = request.user.customer
            except ObjectDoesNotExist:
                customer = Customer.create(request.user)
        except stripe.StripeError as e:
            data['form'] = form
            try:
                data['error'] = e.args[0]
            except IndexError:
                data['error'] = 'Unknown error'
    else:
        data['error'] = form.errors
        data['form'] = form

    return _ajax_response(request, "mini_charge/_charge_form.html", **data)
