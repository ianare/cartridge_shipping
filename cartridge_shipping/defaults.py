from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


SHOP_SHIPPING_ZONES = {
    'France': (
        'AD',
        'FR',
        'MC'
    ),
    'DOM-TOM': (
        'BL',
        'GF',
        'GP',
        'MF',
        'MQ',
        'NC',
        'PF',
        'PM',
        'RE',
        'WF'
    ),
    'Europe': (
        # Euro zone
        'AT',
        'BE',
        'CY',
        'DE',
        'EE',
        'ES',
        'FI',
        'GR',
        'IE',
        'IT',
        'LV',
        'LT',
        'LU',
        'NL',
        'MC',
        'PT',
        'MS',
        'MT',
        'SI',
        'SK',
        'SM',
        'VA',
        # non-Euro zone
        'CH',
        'BG',
        'DK',
        'GB',
        'HU',
        'LI',
        'TR',
    ),
    'World': None
}
register_setting(
        name="SHOP_SHIPPING_ZONES",
        label=_("Shipping zones"),
        description=_("Shipping zones"),
        editable=False,
        default=SHOP_SHIPPING_ZONES
)

SHOP_SHIPPING_TYPES = (
    ('STD', 'standard'),
    ('RGT', 'registered'),
)
register_setting(
        name="SHOP_SHIPPING_TYPES",
        label=_("Shipping types"),
        description=_("Shipping types"),
        editable=False,
        default=SHOP_SHIPPING_TYPES
)

register_setting(
        name="SHOP_SHIPPING_FALLBACK_ZONE",
        label=_("Fallback zone"),
        description=_("Fallback zone"),
        editable=False,
        default='World'
)

template_settings = []

for zone, countries in SHOP_SHIPPING_ZONES.items():
    zone_code = zone.upper()
    zone_title = zone.title()

    free_amount_setting = "SHOP_SHIPPING_FREE_AMOUNT_%s" % zone_code
    register_setting(
        name=free_amount_setting,
        label=_("Free shipping amount - %(zone)s" % {
            'zone': zone_title
        }),
        description=_("Minimum cart amount to apply free shipping to the '%(zone)s' shipping zone" % {
            'zone': zone_title
        }),
        editable=True,
        default=50.0
    )
    template_settings.append(free_amount_setting)

    for type in SHOP_SHIPPING_TYPES:
        type_code = type[0].upper()
        type_name = type[1].title()
        value_setting = "SHOP_SHIPPING_COST_%(zone)s_%(type)s" % {
            'zone': zone_code,
            'type': type_code
        }
        register_setting(
            name=value_setting,
            label=_("%(type)s Shipping Cost - %(zone)s" % {
                'zone': zone_title,
                'type': type_name
            }),
            description=_("Cost of '%(type)s' shipping to the '%(zone)s' shipping zone" % {
                'zone': zone_title,
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
