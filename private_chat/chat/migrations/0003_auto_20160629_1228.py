# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20160629_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='user',
            new_name='autor',
        ),
    ]
