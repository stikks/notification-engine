# import core python modules
import json

# import core django modules
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder


class JSONField(models.TextField):
    """
    JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly.
    Django snippet #1478
    """

    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if value == "":
            return None

        try:
            if isinstance(value, basestring):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return super(JSONField, self).get_db_prep_save(value, *args, **kwargs)


# Create your models here.
class AbstractClass(models.Model):
    """
    Abstract base model class
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('date_created',)


class ClientApplication(AbstractClass):
    """
    Model class to handle registered users
    """
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50, blank=False)
    server_key = models.CharField(blank=False, max_length=255)


class User(AbstractClass):
    """ Instance of client application
    """
    id = models.AutoField(primary_key=True)
    registration_id = models.TextField(blank=False)
    client_application = models.ForeignKey(ClientApplication)


class PushMessage(AbstractClass):
    """
    Model class to handle push notifications
    """
    id = models.AutoField(primary_key=True)
    registration_id = models.TextField(blank=False)
    target = models.TextField(blank=False)
    notification = JSONField(blank=True)
    body = JSONField(blank=True)
    time_to_live = models.BigIntegerField(blank=True)
    priority = models.CharField(default="normal", max_length=6)
    delay_while_idle = models.BooleanField(default=True)
    application = models.ForeignKey(ClientApplication)
