# Generated by Django 2.2.15 on 2020-08-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="title",),
        migrations.AddField(
            model_name="customtext",
            name="title234",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
