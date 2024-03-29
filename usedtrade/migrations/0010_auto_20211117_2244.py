# Generated by Django 3.2.7 on 2021-11-17 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usedtrade', '0009_auto_20211117_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usedtrade_comment_author', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='delete_status',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='file',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usedtrade_file_author', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='file',
            name='author_ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='nested',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usedtrade_nested_author', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='nested',
            name='author_ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='nested',
            name='delete_status',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usedtrade_post_author', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author_ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='delete_status',
            field=models.BooleanField(),
        ),
    ]
