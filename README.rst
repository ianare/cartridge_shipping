******************
cartridge_shipping
******************

Multiple zone shipping handler for Cartridge.


WARNING
=======

**This is pre-alpha code!** Don't use it... *yet*.

Also, I reserve the right to rebase master, so don't clone it, either ;-)

Installing
==========

Add shipping URLS::

    urlpatterns += [
      # cartridge_shipping URLs.
      url("^shop/", include("cartridge_shipping.urls", namespace='cartridge_shipping')),

      ...
    ]

Configure your shipping types in ``settings.py``::

    SHOP_SHIPPING_TYPES = (
        ('STD', _('standard')),
        ('RGT', _('registered')),
        ('XPR', _('express')),
    )

Configure your shipping zones in ``settings.py``.
For example for France we could use::

    SHIPPING_ZONES = {
        'FR': {
            'name': _("France"),
            'countries': (
                'AD',
                'FR',
                'MC'
            )
        },
        'DT': {
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
        'EU': {
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
        'NA': {
            'name': _("North America"),
            'countries': (
                'CA',
                'US',
            )
        },
        'World': {
            'name': _("World"),
            'countries': None
        }
    }
