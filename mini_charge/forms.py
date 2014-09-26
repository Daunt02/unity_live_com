# -*- coding: utf-8 -*-

from django import forms

class ChargeForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2, max_digits=7)
