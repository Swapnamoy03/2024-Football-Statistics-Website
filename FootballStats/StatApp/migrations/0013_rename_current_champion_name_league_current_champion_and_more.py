# Generated by Django 5.1 on 2024-08-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StatApp', '0012_rename_current_champion_league_current_champion_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='current_champion_name',
            new_name='current_champion',
        ),
        migrations.RemoveField(
            model_name='league',
            name='current_champion_logo',
        ),
    ]
