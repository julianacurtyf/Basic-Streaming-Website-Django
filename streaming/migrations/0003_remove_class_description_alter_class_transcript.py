# Generated by Django 4.0 on 2022-01-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0002_alter_course_totalhours_alter_episode_duration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='description',
        ),
        migrations.AlterField(
            model_name='class',
            name='transcript',
            field=models.CharField(max_length=2000),
        ),
    ]
