# Generated by Django 4.1.2 on 2023-02-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0018_applications_own_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
