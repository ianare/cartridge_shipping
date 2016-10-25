from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting

SHIPPING_ZONES = {
    'WLD': {
        'name': _("World"),
        'countries': None
    }
}
register_setting(
        name="SHIPPING_ZONES",
        label=_("Shipping zones"),
        description=_("Shipping zones"),
        editable=False,
        default=SHIPPING_ZONES
)

SHIPPING_TYPES = (
    ('STD', _('standard')),
)
register_setting(
        name="SHIPPING_TYPES",
        label=_("Shipping types"),
        description=_("Shipping types"),
        editable=False,
        default=SHIPPING_TYPES
)

register_setting(
        name="SHIPPING_FALLBACK_ZONE",
        label=_("Fallback zone"),
        description=_("Fallback zone"),
        editable=False,
        default='WLD'
)
