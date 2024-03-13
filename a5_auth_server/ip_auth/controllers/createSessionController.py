from django.db.utils import IntegrityError # type: ignore
from django.http import HttpResponse, HttpResponseServerError # type: ignore
from django.utils.timezone import make_aware # type: ignore
import datetime as dt
import json
import random
import string
from ..models import IPUser


def createSessionController(ip=None, token=None):
    SESSION_KEY_LENGTH = 64
    if ip is None and token is None:
        class MissingIPUserKeyError(Exception):
            def __init__(self):
                self.message = "Either the client IP or token must be provided to create a session"
        try:

            raise MissingIPUserKeyError
        except MissingIPUserKeyError:
            return HttpResponseServerError()

    session_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(SESSION_KEY_LENGTH))
    expiration_datetime = make_aware(dt.datetime.now() + dt.timedelta(days=365))
    try:
        if ip:
            user = IPUser.objects.get(ip_address=ip)
        else:
            user = IPUser.objects.get(token=token)

        new_ip_session = user.ipsession_set.create(
            session_key=session_key,
            expiration=expiration_datetime
        )
        new_ip_session.save()

        new_ip_session = json.loads(str(new_ip_session))
        new_ip_session['ip_address'] = json.loads(new_ip_session['ip_address'])['ip_address']

        return HttpResponse(json.dumps(new_ip_session))
    except IntegrityError:
        return createSessionController(ip=ip, token=token)
