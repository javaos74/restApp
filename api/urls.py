# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from . import views
from rest_framework import routers
from rest_framework import urls

urlpatterns = [
    url(r'^endpoint', views.EPTrackerViewSet.as_view(), name=u'Endpoint API'),
    url(r'^domain', views.DomainViewSet.as_view(), name=u'Domain API'),
    url(r'^fault', views.FaultMessageViewSet.as_view(), name=u'Fault API'),
]
