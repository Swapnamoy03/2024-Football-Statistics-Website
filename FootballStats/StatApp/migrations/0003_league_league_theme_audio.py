# Generated by Django 5.1 on 2024-08-24 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StatApp', '0002_alter_club_club_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='league_theme_audio',
            field=models.FileField(blank=True, null=True, upload_to='leagues/league_audio/'),
        ),
    ]
