# Generated by Django 4.1.2 on 2023-02-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0034_alter_contractemployment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractemployment',
            name='signed_by_employer',
            field=models.BooleanField(default=False, verbose_name='Umowa podpisana przez pracodawcę'),
        ),
    ]
