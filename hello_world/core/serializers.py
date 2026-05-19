from rest_framework import serializers


class CharacterSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.CharField()
    image1 = serializers.CharField()
    image2 = serializers.CharField()
    description = serializers.CharField()
    history = serializers.CharField()
    abilities = serializers.JSONField()
    source = serializers.URLField()
