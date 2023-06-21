# Generated by Django 4.1.2 on 2023-06-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0042_alter_province_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='arrival_fee',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='company_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='district',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='name_surname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='nip',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='pref_visit_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='street',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='town',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='visit_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='visit_length',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='visit_time',
            field=models.CharField(max_length=100),
        ),
    ]
