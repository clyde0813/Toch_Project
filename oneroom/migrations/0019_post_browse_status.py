# Generated by Django 3.2.7 on 2021-11-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0018_rename_longtitude_post_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='browse_status',
            field=models.BooleanField(null=True),
        ),
    ]