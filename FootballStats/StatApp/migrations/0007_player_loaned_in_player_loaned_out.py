# Generated by Django 5.1 on 2024-08-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StatApp', '0006_stat_blocks_stat_own_goals_stat_penalties_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='loaned_in',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='loaned_out',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
