# Generated by Django 4.1.2 on 2023-02-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0016_applications_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='appointment_made',
            field=models.BooleanField(default=False),
        ),
    ]
