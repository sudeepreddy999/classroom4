# Generated by Django 4.2.5 on 2023-10-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_branch_user_profilepic_user_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(default='default.png', upload_to='profile/'),
        ),
    ]
