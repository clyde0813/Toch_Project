# Generated by Django 3.2.7 on 2021-10-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0002_rename_oneroom_post_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='room_num',
        ),
        migrations.RemoveField(
            model_name='post',
            name='toilet_num',
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]