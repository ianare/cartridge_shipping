from django.conf.urls import url

from mezzanine.conf import settings
from cartridge.shop.views import checkout_steps

from .views import get_choices
from .forms import ShippingForm

_slash = "/" if settings.APPEND_SLASH else ""

extra_options = {
    'form_class': ShippingForm,
}

urlpatterns = [
    url('^shipping_choices%s$' % _slash, get_choices, name='shipping_choices_js'),
    url('^shipping_choices/(?P<country>[a-zA-Z]{2})%s$' % _slash, get_choices, name='shipping_choices'),
    url("^shop/checkout%s$" % _slash, checkout_steps, extra_options, name="shop_checkout"),
]
