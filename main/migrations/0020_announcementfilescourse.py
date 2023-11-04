# Generated by Django 4.2.5 on 2023-11-01 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_announcementscourse_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementFilesCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='announceC/')),
                ('announce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annFiles', to='main.announcements')),
            ],
        ),
    ]