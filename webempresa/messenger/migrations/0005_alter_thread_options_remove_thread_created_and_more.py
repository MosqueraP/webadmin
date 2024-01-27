# Generated by Django 5.0.1 on 2024-01-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("messenger", "0004_alter_thread_options_thread_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="thread",
            options={"ordering": ["-updated"]},
        ),
        migrations.RemoveField(
            model_name="thread",
            name="created",
        ),
        migrations.AddField(
            model_name="thread",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
