# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PgtIOU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pgtIou', models.CharField(unique=True, max_length=255, verbose_name='proxy ticket IOU')),
                ('tgt', models.CharField(max_length=255, verbose_name='ticket granting ticket')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'django_cas_pgtiou',
                'verbose_name': 'proxy ticket IOU',
                'verbose_name_plural': 'proxy ticket IOUs',
            },
        ),
        migrations.CreateModel(
            name='SessionServiceTicket',
            fields=[
                ('service_ticket', models.CharField(max_length=255, serialize=False, verbose_name='service ticket', primary_key=True)),
                ('session_key', models.CharField(max_length=40, verbose_name='session key')),
            ],
            options={
                'db_table': 'django_cas_session_service_ticket',
                'verbose_name': 'session service ticket',
                'verbose_name_plural': 'session service tickets',
            },
        ),
        migrations.CreateModel(
            name='Tgt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=255, verbose_name='username')),
                ('tgt', models.CharField(max_length=255, verbose_name='ticket granting ticket')),
            ],
            options={
                'db_table': 'django_cas_tgt',
                'verbose_name': 'ticket granting ticket',
                'verbose_name_plural': 'ticket granting tickets',
            },
        ),
    ]
