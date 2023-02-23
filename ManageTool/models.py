from django.contrib.auth.models import User
from django.db import models
from django.forms import DateInput
from jsignature.fields import JSignatureField


# Create your models here.

class Vs1YkBaformsSubmissions(models.Model):
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=2048)
    date_time = models.CharField(max_length=255)
    submission_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vs1yk_baforms_submissions'


class Vs1YkBaformsItems(models.Model):
    form_id = models.IntegerField()
    column_id = models.IntegerField()
    settings = models.TextField()
    custom = models.CharField(max_length=255)
    options = models.TextField()
    parent = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vs1yk_baforms_items'


class Order(models.Model):
    bounded_to = models.IntegerField()
    type = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255, blank=True)
    facility_name = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=20)
    house_number = models.CharField(max_length=20, blank=True)
    zip_code = models.CharField(max_length=20)
    town = models.CharField(max_length=255, blank=True)
    arrival_fee = models.SmallIntegerField(default=0)
    company_name = models.CharField(max_length=255, blank=True)
    name_surname = models.CharField(max_length=255)
    nip = models.CharField(max_length=255, blank=True)
    facility_address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    visit_length = models.CharField(max_length=255)
    visit_date = models.CharField(max_length=255)
    visit_time = models.CharField(max_length=255)
    pref_visit_time = models.CharField(max_length=255)
    additional_info = models.TextField()
    order_details = models.JSONField(blank=True, null=True)
    marketing_approval = models.BooleanField(default=False)
    reminder_approval = models.BooleanField(default=False)
    products = models.JSONField(default=dict)
    paid_made = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    accomplished = models.BooleanField(default=False)
    assigned_to = models.ManyToManyField(User, default=None)
    created = models.CharField(max_length=255, blank=True)

    class Meta:
        indexes = [models.Index(fields=['type', 'province']), ]


class Applications(models.Model):
    bounded_to = models.IntegerField()
    name_surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    work_region = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    worked_with_children = models.CharField(max_length=255)
    similar_work_experience = models.CharField(max_length=255)
    driver_license = models.CharField(max_length=255)
    car = models.CharField(max_length=255)
    work_24_12 = models.CharField(max_length=255)
    desc_and_experience = models.TextField()
    created = models.CharField(max_length=255, blank=True)
    hired = models.BooleanField(default=False)
    denied = models.BooleanField(default=False)
    score = models.PositiveSmallIntegerField(default=0)
    appointment_made = models.BooleanField(default=False)
    own_notes = models.TextField(blank=True)


CONTRACT_TYPE = [('0', 'Umowa o dzieło stawka godzinowa'),
                 ('1', 'Umowa o dzieło stawka za wizytę')]
TRANSPORT_TYPE = [('0', 'Transport własny'), ('1', 'Transport pracodawcy')]
EMPLOYER = [('0', 'Rimarif Partners Sp. z o.o.')]


# contract employment model
class ContractEmployment(models.Model):
    bounded_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Pracownik',
                                     related_name='bounded_user')
    type = models.CharField(max_length=255, choices=CONTRACT_TYPE, verbose_name='Typ umowy', blank=True, null=True)
    signature_date = models.DateField(auto_created=True, auto_now_add=True, verbose_name='Data podpisania',
                                      blank=True, null=True)
    name_surname = models.CharField(max_length=255, verbose_name='Imię i nazwisko', blank=True, null=True)
    street = models.CharField(max_length=255, verbose_name='Ulica', blank=True, null=True)
    street_number = models.CharField(max_length=20, verbose_name='Numer domu', blank=True, null=True)
    house_number = models.CharField(max_length=20, blank=True, verbose_name='Numer mieszkania', null=True)
    zip_code = models.CharField(max_length=20, verbose_name='Kod pocztowy', blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, verbose_name='Miejscowość', null=True)
    id_number = models.CharField(max_length=255, verbose_name='Numer dowodu osobistego', blank=True, null=True)
    pesel = models.CharField(max_length=255, verbose_name='PESEL', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True, verbose_name='Data rozpoczęcia pracy')
    end_date = models.DateField(blank=True, null=True, verbose_name='Data zakończenia pracy')
    transport_form = models.CharField(max_length=255, choices=TRANSPORT_TYPE, verbose_name='Forma transportu', blank=True, null=True)
    fuel_refund = models.FloatField(default=0.75, help_text='zł/km',
                                    verbose_name='Zwrot kosztów paliwa')
    account_number = models.CharField(max_length=255, verbose_name='Numer konta bankowego', blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name='Numer telefonu', blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name='Adres e-mail')
    signature = JSignatureField(verbose_name='Podpis pracownika', blank=True, null=True)
    employer = models.CharField(max_length=255, choices=EMPLOYER, verbose_name='Nazwa zamawiającego', default='0', blank=True, null=True)
    hourly_rate_own_car = models.FloatField(default=106, help_text='zł brutto', verbose_name='Stawka godzinowa (własny samochód)')
    hourly_rate_company_car = models.FloatField(default=85, help_text='zł brutto', verbose_name='Stawka godzinowa (samochód pracodawcy)')
    visit_rate_own_car_firm = models.FloatField(default=100, verbose_name='Stawka za wizytę w firmach (własny samochód)')
    visit_rate_own_car_private_10min = models.FloatField(default=60, verbose_name='Stawka za wizytę w prywatnych domach - 10min (własny samochód)')
    visit_rate_own_car_private_20min = models.FloatField(default=80, verbose_name='Stawka za wizytę w prywatnych domach - 20min (własny samochód)')
    visit_rate_own_car_private_30min = models.FloatField(default=100, verbose_name='Stawka za wizytę w prywatnych domach - 30min (własny samochód)')
    visit_rate_own_car_private_60min = models.FloatField(default=130, verbose_name='Stawka za wizytę w prywatnych domach - 60min (własny samochód)')
    visit_rate_company_car_firm = models.FloatField(default=85, verbose_name='Stawka za wizytę w firmach (samochód pracoawcy)')
    visit_rate_company_car_private_10min = models.FloatField(default=45, verbose_name='Stawka za wizytę w prywatnych domach - 10min (samochód pracodawcy)')
    visit_rate_company_car_private_20min = models.FloatField(default=65, verbose_name='Stawka za wizytę w prywatnych domach - 20min (samochód pracodawcy)')
    visit_rate_company_car_private_30min = models.FloatField(default=85, verbose_name='Stawka za wizytę w prywatnych domach - 30min (samochód pracodawcy)')
    visit_rate_company_car_private_60min = models.FloatField(default=115, verbose_name='Stawka za wizytę w prywatnych domach - 60min (samochód pracodawcy)')


