# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('who_id', models.IntegerField()),
                ('who_meta', models.TextField(max_length=2000)),
                ('what', models.CharField(max_length=50, null=True, verbose_name=b'What', blank=True)),
                ('what_meta', models.TextField(max_length=2000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('who_id', models.IntegerField()),
                ('who_meta', models.TextField(max_length=1000)),
                ('comment', models.TextField(null=True, verbose_name=b'Comment', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shortcode', models.CharField(unique=True, max_length=50, verbose_name=b'ShortCode')),
                ('display', models.CharField(max_length=50, null=True, verbose_name=b'Display', blank=True)),
                ('severity', models.CharField(max_length=50, null=True, verbose_name=b'Severity', blank=True)),
                ('group', models.CharField(max_length=50, null=True, verbose_name=b'Group', blank=True)),
                ('configurable_counts', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vio_date', models.DateTimeField(auto_now_add=True)),
                ('who_id', models.IntegerField()),
                ('who_type', models.CharField(max_length=50, null=True, verbose_name=b'Who Type', blank=True)),
                ('who_meta', models.TextField(max_length=2000)),
                ('whom_id', models.IntegerField()),
                ('whom_type', models.CharField(max_length=50, null=True, verbose_name=b'Whom Type', blank=True)),
                ('whom_meta', models.TextField(max_length=2000)),
                ('cc_list', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.IntegerField(), blank=True)),
                ('cc_list_meta', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.TextField(max_length=2000), blank=True)),
                ('bcc_list', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.IntegerField(), blank=True)),
                ('bcc_list_meta', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.TextField(max_length=2000), blank=True)),
                ('status', models.CharField(max_length=50, null=True, verbose_name=b'Status', blank=True)),
                ('violation_nature', models.CharField(max_length=50, null=True, verbose_name=b'Violation Nature', blank=True)),
                ('vio_type', models.ForeignKey(default=None, blank=True, to='violations.Type', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='violation',
            field=models.ForeignKey(related_name='comments', default=None, blank=True, to='violations.Violation', null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='violation',
            field=models.ForeignKey(related_name='actions', default=None, blank=True, to='violations.Violation', null=True),
        ),
    ]
