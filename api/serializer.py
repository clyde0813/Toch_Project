from rest_framework import serializers

from oneroom.models import Attribution


class AttributionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribution
        fields = ['post', 'A', 'B', 'C', 'D', 'E']
