# Generated by Django 3.2.7 on 2021-10-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0008_auto_20211011_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='elevator',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='moving_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='parking',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
