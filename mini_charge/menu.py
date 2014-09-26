# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from mini_charge.models.charge import Charge


class MiniChargeMenu(CMSAttachMenu):
    name = _("MiniCharge Menu")

    def get_nodes(self, request):
        nodes = []
        for charge in Charge.objects.all():
            node = NavigationNode(
                charge.amount,
                reverse(
                    'mini_charge.detail',
                    args=(charge.pk,)
                ),
                charge.pk
            )
            nodes.append(node)
        return nodes

#menu_pool.register_menu(MiniChargeMenu)
