# Generated by Django 4.2.1 on 2023-09-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("socialmedia", "0012_post_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
