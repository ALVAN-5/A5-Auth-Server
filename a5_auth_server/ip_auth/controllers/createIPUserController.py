from django.db.utils import IntegrityError  # type: ignore
from django.http import HttpResponse  # type: ignore
import json
from ..models import IPUser
from ..utils.generate_token import generateToken


def createIPUserController(ip, home_group):
    try:
        new_ip_user = IPUser.objects.create(
            ip_address=ip,
            token=generateToken(),
            home_group=home_group
        )
        new_ip_user.save()

        new_ip_user = json.loads(str(new_ip_user))
        new_ip_user['already_existed'] = False

        return HttpResponse(json.dumps(new_ip_user))
    except IntegrityError:
        existing_ip_user = json.loads(str(IPUser.objects.get(ip_address=ip)))
        existing_ip_user['already_existed'] = True

        return HttpResponse(json.dumps(existing_ip_user))
