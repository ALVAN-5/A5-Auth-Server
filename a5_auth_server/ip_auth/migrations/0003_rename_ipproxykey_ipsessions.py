# Generated by Django 5.0.3 on 2024-03-09 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip_auth', '0002_remove_ipproxykey_id_ipuser_home_group_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IPProxyKey',
            new_name='IPSessions',
        ),
    ]
