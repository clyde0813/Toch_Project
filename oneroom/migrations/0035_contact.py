# Generated by Django 4.0 on 2022-01-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0034_postlike_liked_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
