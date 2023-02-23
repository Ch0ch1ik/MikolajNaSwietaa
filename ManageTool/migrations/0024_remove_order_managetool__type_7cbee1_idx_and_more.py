# Generated by Django 4.1.2 on 2023-02-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0023_remove_order_managetool__type_1dda3b_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='order',
            name='ManageTool__type_7cbee1_idx',
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['type', 'province'], name='ManageTool__type_1dda3b_idx'),
        ),
    ]
