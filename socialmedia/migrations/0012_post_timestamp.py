# Generated by Django 4.2.1 on 2023-09-21 02:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("socialmedia", "0011_alter_post_content_cost"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
