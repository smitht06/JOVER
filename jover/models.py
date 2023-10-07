from django.db import models
from django.db import models
from django.utils import timezone
from localflavor.us.models import USStateField, USZipCodeField
from localflavor.us.us_states import STATE_CHOICES
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    # Personal Info
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    suffix = models.CharField(max_length=255, blank=True)

    email = models.EmailField(blank=True, db_index=True)
    phone = PhoneNumberField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, blank=True) # M, F, or O

    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = USStateField(choices=STATE_CHOICES, blank=True)
    zip5 = USZipCodeField(blank=True)


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    candidate = models.ForeignKey(Person, on_delete=models.CASCADE)
    election_date = models.DateField(null=True, blank=True)
    office = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    manager = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='campaign_manager')
    volunteers = models.ManyToManyField(Person, related_name='campaign_volunteers', blank=True)

class ContactLog(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    method = models.CharField(max_length=255, blank=True)

class Materials(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='materials/')


