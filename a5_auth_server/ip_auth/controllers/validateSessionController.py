from django.http import HttpResponse # type: ignore
from django.utils.timezone import make_aware # type: ignore
import json
from ..models import IPSession
from datetime import datetime


def validateSessionController(session, ip=None):
    try:
        ipSession = IPSession.objects.get(session_key=session)
    except Exception:
        return HttpResponse(json.dumps({'session_key': ''}))

    if ipSession.expiration < make_aware(datetime.now()):
        ipSession.delete()
        return HttpResponse(json.dumps({'session_key': ''}))
    else:
        session = json.loads(str(ipSession))
        return HttpResponse(json.dumps({'session_key': session['session_key']}))
