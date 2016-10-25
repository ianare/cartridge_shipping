
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import settings, register_setting

from django.apps import AppConfig


class CartridgeShippingConfig(AppConfig):
    name = 'cartridge_shipping'

    def ready(self):
        template_settings = []

        for zone, info in settings.SHIPPING_ZONES.items():
            zone_code = zone.upper()
            zone_name = info['name'].title()

            free_amount_setting = "SHIPPING_FREE_AMOUNT_%s" % zone_code
            register_setting(
                name=free_amount_setting,
                label=_("Free shipping amount - %(zone)s" % {
                    'zone': zone_name
                }),
                description=_("Minimum cart amount to apply free shipping to the '%(zone)s' shipping zone" % {
                    'zone': zone_name
                }),
                editable=True,
                default=50.0
            )
            template_settings.append(free_amount_setting)

            for type in settings.SHIPPING_TYPES:
                type_code = type[0].upper()
                type_name = type[1].title()
                value_setting = "SHIPPING_COST_%(zone)s_%(type)s" % {
                    'zone': zone_code,
                    'type': type_code
                }
                register_setting(
                    name=value_setting,
                    label=_("%(type)s Shipping Cost - %(zone)s" % {
                        'zone': zone_name,
                        'type': type_name
                    }),
                    description=_("Cost of '%(type)s' shipping to the '%(zone)s' shipping zone" % {
                        'zone': zone_name,
                        'type': type_name
                    }),
                    editable=True,
                    default=5.0
                )
                template_settings.append(value_setting)


        register_setting(
            name="TEMPLATE_ACCESSIBLE_SETTINGS",
            editable=False,
            default=tuple(template_settings),
            append=True,
        )
