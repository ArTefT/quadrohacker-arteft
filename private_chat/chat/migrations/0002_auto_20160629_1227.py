# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='date_msg',
            new_name='data_message',
        ),
        migrations.RenameField(
            model_name='usermessage',
            old_name='text_msg',
            new_name='text_message',
        ),
        migrations.RenameField(
            model_name='usermessage',
            old_name='user_msg',
            new_name='user',
        ),
    ]
