# Generated by Django 3.0.8 on 2021-04-25 13:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210424_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interludesslot',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 11, 0, tzinfo=utc), verbose_name='début'),
            preserve_default=False,
        ),
    ]
