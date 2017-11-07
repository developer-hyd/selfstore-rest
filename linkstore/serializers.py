from rest_framework import serializers
from linkstore.models import Link


class LinkSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    subject = serializers.CharField(required=True)
    link = serializers.CharField(required=True, allow_blank=False, max_length=200)
    description = serializers.CharField(required=True)



    def create(self, validated_data):
        return Link.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.link = validated_data.get('link', instance.link)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance