# -*- coding: utf-8 -*-

#from django import forms
from django.contrib import admin
import imagestore.admin
from mini_charge.models.charge import Charge
from mini_charge.models.image import MiniChargeImage
#from mini_charge.models.album import MiniChargeAlbum


admin.site.register(Charge)


class MiniChargeImageAdmin(imagestore.admin.ImageAdmin):

    def __init__(self, *args, **kwargs):
        super(MiniChargeImageAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = MiniChargeImage

admin.site.register(MiniChargeImage, MiniChargeImageAdmin)
