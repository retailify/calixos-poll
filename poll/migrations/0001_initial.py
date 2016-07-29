# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=250, verbose_name=b'value')),
                ('pos', models.SmallIntegerField(default=b'0', verbose_name='Position')),
            ],
            options={
                'ordering': ['pos'],
                'verbose_name': 'answer',
                'verbose_name_plural': 'answers',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'question')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'date')),
                ('is_published', models.BooleanField(default=True, verbose_name='ver\xf6ffentlicht')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'poll',
                'verbose_name_plural': 'polls',
            },
        ),
        migrations.CreateModel(
            name='PollPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('poll', models.ForeignKey(to='poll.Poll')),
            ],
            options={
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(verbose_name=b"user's IP")),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(verbose_name=b'voted item', to='poll.Item')),
                ('poll', models.ForeignKey(verbose_name=b'poll', to='poll.Poll')),
                ('user', models.ForeignKey(verbose_name='Benutzer', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='poll',
            field=models.ForeignKey(to='poll.Poll'),
        ),
    ]
