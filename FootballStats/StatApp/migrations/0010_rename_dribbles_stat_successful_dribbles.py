# Generated by Django 5.1 on 2024-08-25 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StatApp', '0009_rename_motm_award_stat_dribbles_stat_through_balls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stat',
            old_name='dribbles',
            new_name='successful_dribbles',
        ),
    ]
