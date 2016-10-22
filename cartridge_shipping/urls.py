from django.conf.urls import url

from mezzanine.conf import settings

from .views import get_choices

_slash = "/" if settings.APPEND_SLASH else ""

urlpatterns = [
    url('^shipping_choices/(?P<country>[a-zA-Z]{2})%s$' % _slash, get_choices, name='shipping_choices'),
]
