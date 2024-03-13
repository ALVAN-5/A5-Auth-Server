from django.db import models # type: ignore
import json

# Create your models here.
MAX_IP_LENGTH = 45
HOME_GROUP_LENGTH = 32
TOKEN_LENGTH = 32
SESSION_KEY_LENGTH = 64


class IPUser(models.Model):
    ip_address = models.CharField(max_length=MAX_IP_LENGTH, primary_key=True)
    home_group = models.CharField(max_length=HOME_GROUP_LENGTH)
    token = models.CharField(max_length=TOKEN_LENGTH, unique=True)

    def __str__(self):
        return json.dumps({
            'ip_address': self.ip_address,
            'token': self.token,
            'home_group': self.home_group
        })


class IPSession(models.Model):
    ip_address = models.ForeignKey(IPUser, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=SESSION_KEY_LENGTH, primary_key=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return json.dumps({
            'ip_address': str(self.ip_address),
            'session_key': self.session_key,
            'expiration': str(self.expiration)
        })
