"""
Checkout process utilities.
"""

from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import settings
from cartridge.shop.utils import set_shipping, clear_session
from cartridge.shop.templatetags.shop_tags import currency

settings.use_editable()


def _get_ship_zone(country: str) -> str:
    for zone, info in settings.SHIPPING_ZONES.items():
        try:
            if country in info['countries']:
                return zone
        except TypeError:
            pass
    return settings.SHIPPING_FALLBACK_ZONE.upper()


def get_ship_choices(country: str, request) -> list:
    """
    Given a country, return which shipping choices are available to the
    user based on the cart amount.
    """
    zone = _get_ship_zone(country.upper())
    zone_code = zone.upper()
    choices = []
    free_ship = getattr(settings, "SHIPPING_FREE_AMOUNT_%s" % zone_code)
    if request.cart.total_price() >= free_ship:
        choices.append({
            'code': "FREE",
            'display': "%s - %s" % (_("free shipping").title(), currency(0))
        })
        return choices
    for ship_type in settings.SHIPPING_TYPES:
        type_code = ship_type[0].upper()
        type_name = ship_type[1].title()
        cost_code = 'SHIPPING_COST_%s_%s' % (zone_code, type_code)
        cost = getattr(settings, cost_code)
        if cost:
            choices.append({
                'code': cost_code,
                'display': "%s - %s" % (type_name.title(), currency(cost))
            })
    return choices


def _set_ship_rate(country: str, shipping_code: str, request) -> bool:
    choices = get_ship_choices(country, request)
    shipping_cost = None
    for choice in choices:
        if choice["code"] == shipping_code:
            shipping_cost = getattr(settings, shipping_code)
            break
    # cost can be 0
    if shipping_cost != None:
        zone_name, ship_name = shipping_code.split('_')[2:]
        zone_name = settings.SHIPPING_ZONES[zone_name.upper()]['name']
        for ship_type in settings.SHIPPING_TYPES:
            if ship_name == ship_type[0]:
                ship_name = ship_type[1]
                break
        shipping_type = "%s - %s" % (zone_name.title(), ship_name.title())
        set_shipping(request, shipping_type, shipping_cost)
        return True
    else:
        clear_session('shipping_type', 'shipping_total')
        return False


def multizone_billship_handler(request, order_form) -> None:
    """
    This function will typically contain any shipping calculation
    where the shipping amount can then be set using the function
    ``cartridge.shop.utils.set_shipping``. The Cart object is also
    accessible via ``request.cart``
    """
    try:
        country = order_form.cleaned_data['shipping_detail_country']
        shipping_type = order_form.cleaned_data['shipping_type']
    except AttributeError:
        return

    if not request.session.get("free_shipping"):
        _set_ship_rate(country, shipping_type, request)
