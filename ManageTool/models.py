from django.db import models


# Create your models here.

class Vs1YkBaformsSubmissions(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    date_time = models.CharField(max_length=255)
    submission_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vs1yk_baforms_submissions'


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
    arrival_fee = models.CharField(max_length=255, blank=True)
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
    order_details = models.TextField()
    marketing_approval = models.BooleanField(default=False)
    reminder_approval = models.BooleanField(default=False)
    products = models.CharField(max_length=255)

