# -*- coding: utf-8 -*-

from models import Domain, EPTracker, FaultMessage
from rest_framework import serializers


class DomainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Domain
        fields = ('name', 'controllers', 'user', 'password', 'created_date')


class EPTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EPTracker
        fields = ('mac', 'ip', 'domain', 'tenant','app', 'epg', 'dn', 'intf', 'start', 'stop')


class FaultMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FaultMessage
        fields = ('code', 'title', 'syslog', 'explan','actions')

