# -*- coding: utf-8 -*-

from django.db import models
from imagestore.models.bases.image import BaseImage


class MiniChargeImage(BaseImage):

    class Meta(BaseImage.Meta):
        abstract = False
        app_label = 'mini_charge'
        db_table = 'mini_charge_image'
