# Generated by Django 3.2.7 on 2021-10-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usedtrade_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField()),
                ('modified_date', models.DateField(blank=True, null=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]