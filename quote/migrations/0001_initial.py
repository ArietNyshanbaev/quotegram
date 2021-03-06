# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=1000, verbose_name=b' Body of quote ')),
                ('user', models.ForeignKey(verbose_name=b' Quote of user ', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quote',
                'verbose_name_plural': 'Quotes',
            },
        ),
    ]
