# Generated by Django 3.0.7 on 2020-07-30 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userClientProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 10, 17, 47, 384379), verbose_name=datetime.datetime(2020, 7, 30, 10, 17, 47, 384379)),
        ),
    ]
