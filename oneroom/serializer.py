from rest_framework import serializers


class AttributionSerializer(serializers.Serializer):
    post = serializers.CharField(max_length=100)
    A = serializers.IntegerField()
    B = serializers.IntegerField()
    C = serializers.IntegerField()
    D = serializers.IntegerField()
    E = serializers.IntegerField()
