# Generated by Django 4.1.2 on 2023-02-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0021_contractemployment'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['type', 'province'], name='ManageTool__type_1dda3b_idx'),
        ),
    ]
