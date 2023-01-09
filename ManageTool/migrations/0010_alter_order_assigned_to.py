# Generated by Django 4.1.2 on 2022-10-25 09:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageTool', '0009_order_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='assigned_to',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
