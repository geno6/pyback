# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('user', models.OneToOneField(related_name='user_profile', to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(verbose_name='Address', max_length=255)),
                ('phone', models.CharField(verbose_name='Phone number', max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'auth_user_profile',
            },
            bases=(models.Model,),
        ),
    ]
