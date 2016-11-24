# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quote', '0002_auto_20161124_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_upvote', models.BooleanField(default=True, verbose_name=b'is vote positive?')),
                ('quote', models.ForeignKey(verbose_name=b' Quote of vote ', to='quote.Quote')),
                ('user', models.ForeignKey(verbose_name=b' User who votes ', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
            },
        ),
    ]
