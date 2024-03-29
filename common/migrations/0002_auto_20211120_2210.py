# Generated by Django 3.2.7 on 2021-11-20 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20211117_2243'),
        ('usedtrade', '0010_auto_20211117_2244'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='community_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_post', to='community.post'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='used_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_post', to='usedtrade.post'),
        ),
    ]
