# Generated by Django 3.2.7 on 2021-10-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0006_alter_post_manage_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='common_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='dedicated_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='deposit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
