# Generated by Django 3.2.3 on 2021-06-02 21:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_core", "0022_authenticatedsession"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="meta_launch_url",
            field=models.TextField(
                blank=True,
                default="",
                validators=[django.core.validators.URLValidator()],
            ),
        ),
    ]