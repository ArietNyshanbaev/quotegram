# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(verbose_name=b' User of quote ', to=settings.AUTH_USER_MODEL),
        ),
    ]
