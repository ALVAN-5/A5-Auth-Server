# Generated by Django 5.0.3 on 2024-03-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipproxykey',
            name='id',
        ),
        migrations.AddField(
            model_name='ipuser',
            name='home_group',
            field=models.CharField(default='sirota_home', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ipproxykey',
            name='session_key',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
