# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from mini_charge.menu import MiniChargeMenu

class MiniChargeApp(CMSApp):
    name = _("MiniCharge App")
    urls = ["mini_charge.urls"]
    app_name = "mini_charge"
    #menus = [MiniChargeMenu]

apphook_pool.register(MiniChargeApp)
