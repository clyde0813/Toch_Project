# Generated by Django 3.2.3 on 2021-09-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oneroom_post',
            name='gas_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oneroom_post',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
