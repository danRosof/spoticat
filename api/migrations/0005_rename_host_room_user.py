# Generated by Django 4.0.8 on 2022-12-10 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_room_guest_can_pause_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='host',
            new_name='user',
        ),
    ]
