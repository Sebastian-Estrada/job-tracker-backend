# Generated by Django 5.1 on 2024-08-18 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0002_jobdescription_jobposition_job_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobposition",
            name="description",
        ),
    ]
