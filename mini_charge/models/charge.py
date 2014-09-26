# -*- coding: utf-8 -*-

from django.db import models
#from django.core.urlresolvers import reverse
from cms.models import CMSPlugin
from django.conf import settings

from mini_charge.models.image import MiniChargeImage


class Charge(models.Model):

    '''
        Charge Model
        @see https://stripe.com/docs/api#create_charge
    '''

    def __init__(self, *args, **kwargs):
        super(Charge, self).__init__(*args, **kwargs)
        import stripe
        stripe.api_key = settings.STRIPE_PUBLIC_KEY
        self.stripe = stripe

    name = models.CharField(max_length=50)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        null=True,
        blank=True)
    currency = models.CharField(
        max_length=10,
        help_text='"USD", "EUR", etc. Review https://support.stripe.com/questions/which-currencies-does-stripe-support for more detail.'
    )
    description = models.CharField(max_length=300)

    # Expect user to create a price specification before attaching
    # a work of art or product.
    work = models.ManyToManyField(MiniChargeImage)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'mini_charge'


class MiniChargePluginModel(CMSPlugin):

    '''
        MiniCharge Plugin Model
    '''
    charge = models.ForeignKey(
        Charge,
        related_name='plugins'
    )

    def __unicode__(self):
        return self.charge.name

    class Meta:
        app_label = 'mini_charge'
