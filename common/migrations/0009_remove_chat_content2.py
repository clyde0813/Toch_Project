# Generated by Django 3.2.9 on 2021-11-22 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_chat_content2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='content2',
        ),
    ]