# Generated by Django 4.1.2 on 2023-02-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0011_order_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bounded_to', models.IntegerField()),
                ('name_surname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('work_region', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('height', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
                ('worked_with_children', models.CharField(max_length=255)),
                ('similar_work_experience', models.CharField(max_length=255)),
                ('driver_license', models.CharField(max_length=255)),
                ('car', models.CharField(max_length=255)),
                ('work_24_12', models.CharField(max_length=255)),
                ('description_and_experience', models.TextField()),
                ('created', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
