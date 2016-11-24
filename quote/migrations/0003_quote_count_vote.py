# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0002_auto_20161124_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='count_vote',
            field=models.IntegerField(default=0, verbose_name=b'State of votes'),
        ),
    ]
