# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 12:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accreditations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DclRecordUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_id', models.CharField(max_length=2048)),
                ('new_value', models.TextField(blank=True, default='', max_length=5120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accreditations.AccreditedParty')),
                ('user', models.ForeignKey(blank=True, help_text='Staff member who performed the action, if applicable', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
