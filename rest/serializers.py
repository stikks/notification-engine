__author__ = 'stikks'

# import third party modules
from rest_framework import serializers

# import applocation modules
from rest.models import ClientApplication, PushMessage, User


class ClientApplicationSerializer(serializers.ModelSerializer):
    """ custom serializer for serializing and deserializing a user instance into json representation
    """
    class Meta:
        model = ClientApplication
        fields = ('id', 'server_key', 'name', 'date_created', 'date_modified')

    def create(self, validated_data):
        """
        Create and return a new `Client Application` instance, given the validated data.
        """
        return ClientApplication.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates an existing 'User' instance, given the validated data.
        """
        instance.server_key = validated_data.get('server_key', instance.server_key)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """ custom serializer for serializing and deserializing a user instance into json representation
    """
    class Meta:
        model = User
        fields = ('id', 'application_id', 'registration_id', 'date_created', 'date_modified')

    def create(self, validated_data):
        """
        Create and return a new `Client Application` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates an existing 'User' instance, given the validated data.
        """
        instance.application_id = validated_data.get('application_id', instance.application_id)
        instance.registration_id = validated_data.get('registration_id', instance.registration_id)
        instance.save()
        return instance


class PushMessageSerializer(serializers.ModelSerializer):
    """ custom serializer for serializing and deserializing a user instance into json representation
    """
    class Meta:
        model = PushMessage
        fields = ('id', 'body', 'target', 'notification', 'registration_id', 'date_created', 'date_modified')

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
        instance.registration_id = validated_data.get('registration_id', instance.registration_id)
        instance.target = validated_data.get('target', instance.target)
        instance.time_to_live = validated_data.get('time_to_live', instance.time_to_live)
        instance.delay_while_idle = validated_data.get('delay_while_idle', instance.delay_while_idle)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance

