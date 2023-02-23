# Generated by Django 4.1.2 on 2023-02-23 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageTool', '0028_alter_contractemployment_name_surname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractemployment',
            name='type',
            field=models.CharField(choices=[(0, 'Umowa o dzieło stawka godzinowa'), (1, 'Umowa o dzieło stawka za wizytę')], default=0, max_length=255, verbose_name='Typ umowy'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='account_number',
            field=models.CharField(max_length=255, verbose_name='Numer konta bankowego'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='bounded_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bounded_user', to=settings.AUTH_USER_MODEL, verbose_name='Pracownik'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Adres e-mail'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data zakończenia pracy'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='fuel_refund',
            field=models.FloatField(blank=True, default=0.75, help_text='zł/km', null=True, verbose_name='Zwrot kosztów paliwa'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='house_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Numer mieszkania'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='id_number',
            field=models.CharField(max_length=255, verbose_name='Numer dowodu osobistego'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='pesel',
            field=models.CharField(max_length=255, verbose_name='PESEL'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='signature',
            field=jsignature.fields.JSignatureField(verbose_name='Podpis pracownika'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data rozpoczęcia pracy'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='street',
            field=models.CharField(max_length=255, verbose_name='Ulica'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='street_number',
            field=models.CharField(max_length=20, verbose_name='Numer domu'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='town',
            field=models.CharField(blank=True, max_length=255, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='transport_form',
            field=models.CharField(max_length=255, verbose_name='Forma transportu'),
        ),
        migrations.AlterField(
            model_name='contractemployment',
            name='zip_code',
            field=models.CharField(max_length=20, verbose_name='Kod pocztowy'),
        ),
    ]
