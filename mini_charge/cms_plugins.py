# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from mini_charge.models.charge import MiniChargePluginModel


class MiniChargePlugin(CMSPluginBase):
    model = MiniChargePluginModel
    name = _("MiniCharge Plugin")
    render_template = "mini_charge/base_plugin.tmpl"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance
        })
        return context

plugin_pool.register_plugin(MiniChargePlugin)
