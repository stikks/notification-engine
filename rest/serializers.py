__author__ = 'stikks'

# import third party modules
from rest_framework import serializers

# import applocation modules
from rest.models import ClientApplication, PushMessage


class ClientApplicationSerializer(serializers.ModelSerializer):
    """ custom serializer for serializing and deserializing a user instance into json representation
    """
    class Meta:
        model = ClientApplication
        fields = ('id', 'registration_id', 'name', 'date_created', 'date_modified')

    def create(self, validated_data):
        """
        Create and return a new `Client Application` instance, given the validated data.
        """
        return ClientApplication.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates an existing 'User' instance, given the validated data.
        """
        instance.gcm_id = validated_data.get('gcm_id', instance.gcm_id)
        instance.save()
        return instance


class PushMessageSerializer(serializers.ModelSerializer):
    """ custom serializer for serializing and deserializing a user instance into json representation
    """
    class Meta:
        model = PushMessage
        fields = ('id', 'body', 'target', 'notification', 'date_created', 'date_modified')

    def create(self, validated_data):
        """
        Create and return a new `Push Message` instance, given the validated data.
        """
        return PushMessage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates an existing 'Push Message' instance, given the validated data.
        """
        instance.body = validated_data.get('body', instance.body)
        instance.notification = validated_data.get('notification', instance.notification)
        instance.target = validated_data.get('target', instance.target)
        instance.time_to_live = validated_data.get('time_to_live', instance.time_to_live)
        instance.delay_while_idle = validated_data.get('delay_while_idle', instance.delay_while_idle)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance

