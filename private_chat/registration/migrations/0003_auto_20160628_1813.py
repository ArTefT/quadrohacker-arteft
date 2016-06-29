# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
