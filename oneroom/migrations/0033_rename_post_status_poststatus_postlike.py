# Generated by Django 4.0 on 2022-01-11 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oneroom', '0032_post_status_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post_Status',
            new_name='PostStatus',
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipAddress', models.GenericIPAddressField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_set', to='oneroom.post')),
            ],
        ),
    ]
