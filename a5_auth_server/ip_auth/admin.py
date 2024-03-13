from django.contrib import admin # type: ignore
from ip_auth.models import IPSession, IPUser

# Register your models here.
admin.register(IPUser)
admin.register(IPSession)
