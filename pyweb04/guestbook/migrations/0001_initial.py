# Generated by Django 2.2.1 on 2019-08-14 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
