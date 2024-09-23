# -*- coding: utf-8 -*-

from django.urls import re_path

from envelope.views import ContactView


urlpatterns = [
    re_path(r'^$', ContactView.as_view(), name='envelope-contact'),
]
