# Generated by Django 3.2.9 on 2021-11-22 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_chat_used_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='chatroom',
        ),
    ]
