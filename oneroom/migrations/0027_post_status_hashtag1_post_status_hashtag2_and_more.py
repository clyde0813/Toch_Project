# Generated by Django 4.0 on 2022-01-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0026_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_status',
            name='hashtag1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post_status',
            name='hashtag2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post_status',
            name='hashtag3',
            field=models.TextField(blank=True, null=True),
        ),
    ]