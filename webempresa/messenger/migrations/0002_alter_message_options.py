# Generated by Django 5.0.1 on 2024-01-26 21:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("messenger", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={"ordering": ["created"]},
        ),
    ]
