******************
cartridge_shipping
******************

Multiple zone shipping handler for Cartridge.


WARNING
=======

**This is pre-alpha code!** Don't use it... *yet*.

Also, I reserve the right to rebase master, so don't clone it, either ;-)

Configuration
=============

Add shipping URLS::

    urlpatterns += [
      # cartridge_shipping URLs.
      url("^shop/", include("cartridge_shipping.urls", namespace='cartridge_shipping')),

      ...
    ]

Configure ``SHIPPING_TYPES`` in ``settings.py``, a list of list of shipping types.

The first element is the type code used internally, keep it short and uppercase.

The second element is displayed to the user, it is translatable.

For example::

    SHIPPING_TYPES = (
        ('STD', _('standard')),
        ('RGT', _('registered')),
        ('XPR', _('express')),
    )

Configure ``SHIPPING_ZONES`` in ``settings.py``, a dictionary of all your shipping zones.

The key is the zone code used internally, keep it short and uppercase.

The ``name`` property is displayed to the user, it is translatable.

The ``countries`` property is a list of ISO 2-letter country codes in the zone.
You may not have the same country is different zones.

For example for France we could have::

    SHIPPING_ZONES = {
        'FRA': {
            'name': _("France"),
            'countries': (
                'AD',
                'FR',
                'MC'
            )
        },
        'DOM': {
            'name': _("DOM-TOM"),
            'countries': (
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
            )
        },
        'EUR': {
            'name': _("Europe"),
            'countries': (
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
            )
        },
        'NAM': {
            'name': _("North America"),
            'countries': (
                'CA',
                'US',
            )
        },
        'WLD': {
            'name': _("World"),
            'countries': None
        }
    }

You'll notice the 'WLD' item at the bottom, it's the fallback case.
When a country doesn't match any zone it goes in there.

You can modify ``SHIPPING_FALLBACK_ZONE`` to something else.
