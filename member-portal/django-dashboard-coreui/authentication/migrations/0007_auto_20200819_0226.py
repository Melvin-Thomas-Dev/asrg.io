# Generated by Django 2.1.15 on 2020-08-18 20:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20200819_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='foundation',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 18, 20, 56, 43, 162372, tzinfo=utc)),
        ),
    ]
