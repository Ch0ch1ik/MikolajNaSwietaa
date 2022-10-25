from django.contrib.auth.models import User
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

