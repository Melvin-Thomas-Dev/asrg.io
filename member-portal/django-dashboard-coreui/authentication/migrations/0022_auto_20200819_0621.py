# Generated by Django 2.1.15 on 2020-08-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_auto_20200819_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='foundation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
