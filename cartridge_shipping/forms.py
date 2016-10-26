from django.utils.translation import ugettext_lazy as _
from django import forms


class ShippingChoiceField(forms.ChoiceField):
    def validate(self, value):
        return


class ShippingForm(forms.Form):
    shipping_type = ShippingChoiceField(label=_("Shipping type"), choices=(), required=True)
