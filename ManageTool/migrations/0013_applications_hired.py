# Generated by Django 4.1.2 on 2023-02-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0012_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='hired',
            field=models.BooleanField(default=False),
        ),
    ]
