# Generated by Django 4.2.5 on 2023-11-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_room_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsub',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
