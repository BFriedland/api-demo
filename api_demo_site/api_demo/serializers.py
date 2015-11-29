from rest_framework import serializers
from api_demo_site.api_demo.models import Stuff


class StuffSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stuff
        fields = ('title', 'description')
