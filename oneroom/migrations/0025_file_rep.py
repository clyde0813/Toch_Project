# Generated by Django 4.0 on 2022-01-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0024_remove_post_author_ip_remove_post_common_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='rep',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]