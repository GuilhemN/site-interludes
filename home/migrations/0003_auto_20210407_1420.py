# Generated by Django 3.0.8 on 2021-04-07 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210329_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterludesActivityChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveIntegerField(verbose_name='priorité')),
                ('accepted', models.BooleanField(default=False, verbose_name='Obtenue')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.InterludesParticipant', verbose_name='participant')),
            ],
            options={
                'verbose_name': "choix d'activités",
                'verbose_name_plural': "choix d'activités",
                'ordering': ('participant', 'priority'),
            },
        ),
        migrations.CreateModel(
            name='InterludesSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='{act_title}', help_text="Utilisez '{act_title}' pour insérer le titre de l'activité correspondante", max_length=200, verbose_name='Titre')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='début')),
                ('room', models.CharField(blank=True, max_length=100, null=True, verbose_name='salle')),
                ('on_planning', models.BooleanField(default=False, help_text='Nécessite de salle et heure de début non vide', verbose_name='afficher sur le planning')),
                ('subscribing_open', models.BooleanField(default=False, help_text="Si vrai, apparaît dans la liste du formulaire d'inscription", verbose_name='ouvert aux inscriptions')),
            ],
            options={
                'verbose_name': 'créneau',
                'verbose_name_plural': 'créneaux',
            },
        ),
        migrations.RemoveField(
            model_name='interludesactivity',
            name='canonical',
        ),
        migrations.RemoveField(
            model_name='interludesactivity',
            name='on_planning',
        ),
        migrations.RemoveField(
            model_name='interludesactivity',
            name='room',
        ),
        migrations.RemoveField(
            model_name='interludesactivity',
            name='start',
        ),
        migrations.RemoveField(
            model_name='interludesactivity',
            name='subscribing_open',
        ),
        migrations.AlterField(
            model_name='interludesactivity',
            name='must_subscribe',
            field=models.BooleanField(default=False, help_text="Informatif, il faut utiliser les créneaux pour ajouter dans la liste d'inscription", verbose_name='sur inscription'),
        ),
        migrations.DeleteModel(
            name='ActivityList',
        ),
        migrations.AddField(
            model_name='interludesslot',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.InterludesActivity', verbose_name='Activité'),
        ),
        migrations.AddField(
            model_name='interludesactivitychoices',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.InterludesSlot', verbose_name='créneau'),
        ),
        migrations.AlterUniqueTogether(
            name='interludesactivitychoices',
            unique_together={('participant', 'slot'), ('priority', 'participant')},
        ),
    ]
