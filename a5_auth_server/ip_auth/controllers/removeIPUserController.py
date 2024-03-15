from django.http import HttpResponse, Http404, HttpResponseNotFound  # type: ignore
from django.shortcuts import get_object_or_404
import json
from ..models import IPUser


def removeIPUserController(ip):
    try:
        ip_user = get_object_or_404(IPUser, ('ip_address', ip))
    except Http404:
        return HttpResponseNotFound()

    deleted_user = {
        'ip_address': ip_user.ip_address,
        'token': ip_user.token,
        'home_group': ip_user.home_group
    }
    
    ip_user.delete()
    print('[]')
    print(deleted_user)
    print('[]')
    return HttpResponse(json.dumps(deleted_user))
