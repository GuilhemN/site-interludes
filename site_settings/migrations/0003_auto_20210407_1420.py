# Generated by Django 3.0.8 on 2021-04-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_auto_20210324_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='discord_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Lien du serveur discord'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='global_message_as_html',
            field=models.BooleanField(default=False, help_text='Assurez vous que le message est bien formaté, cela peut casser toutes les pages du site', verbose_name='Message global au format HTML'),
        ),
    ]
