# Generated by Django 4.1.2 on 2023-06-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0041_alter_province_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
