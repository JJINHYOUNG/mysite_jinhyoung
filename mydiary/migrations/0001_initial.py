# Generated by Django 3.0.5 on 2020-04-09 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 4, 9, 10, 57, 10, 571985, tzinfo=utc))),
                ('body', models.TextField(default='')),
            ],
        ),
    ]
