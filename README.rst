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
      url("^shop/", include("cartridge_shipping.urls")),

      ...
  ]

