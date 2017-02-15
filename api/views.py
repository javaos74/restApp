# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import viewsets, mixins, serializers
from rest_framework.generics import GenericAPIView
from models import *
from serializers import *

# Create your views here.

# for rest api
class DomainViewSet(GenericAPIView, mixins.ListModelMixin):
    """
    API endpoint that allows Domain to be viewed or edited.
    """
    queryset = Domain.objects.all().order_by('-created_date')
    serializer_class = DomainSerializer

    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)


class EPTrackerViewSet( GenericAPIView, mixins.ListModelMixin):
    """
    API endpoint that allows EPTracker to be viewed or edited.
    """
    queryset = EPTracker.objects.all()
    serializer_class = EPTrackerSerializer

    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)

class FaultMessageViewSet( GenericAPIView, mixins.ListModelMixin):
    """
    API endpoint that allows FaultMessage to be viewed or edited.
    """
    queryset = FaultMessage.objects.all()
    serializer_class = FaultMessageSerializer

    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)

