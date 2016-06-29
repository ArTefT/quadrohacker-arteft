# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20160629_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='data_message',
            new_name='date_message',
        ),
    ]
