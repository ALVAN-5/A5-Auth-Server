from django.http import HttpResponse, Http404, HttpResponseNotFound  # type: ignore
from django.shortcuts import get_object_or_404
import json
from ..models import IPUser
from ..utils.generate_token import generateToken


def resetIPTokenController(ip, home_group):
    try:
        ip_user = get_object_or_404(IPUser, ('ip_address', ip), ('home_group', home_group))
    except Http404:
        return HttpResponseNotFound()
    ip_user.token = generateToken()
    ip_user.save()

    updated_ip_user = json.loads(str(ip_user))

    return HttpResponse(json.dumps(updated_ip_user))
