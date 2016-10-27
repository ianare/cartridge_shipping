from django.utils.translation import ugettext_lazy as _
from django import forms

from cartridge.shop.forms import OrderForm

from .checkout import get_ship_choice_codes


class ShippingForm(OrderForm):
    shipping_type = forms.CharField(label=_("Shipping type"), required=True, widget=forms.Select())

    def clean_shipping_type(self):
        country = self.cleaned_data["shipping_detail_country"]
        choices = get_ship_choice_codes(country)
        if self.cleaned_data["shipping_type"] in choices:
            return self.cleaned_data["shipping_type"]
        else:
            raise forms.ValidationError(_("Invalid shipping type for country."))
