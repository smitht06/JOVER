from django.contrib import admin

# Register your models here.

from .models import Person, Campaign, ContactLog, Materials

admin.site.register(Person)
admin.site.register(Campaign)
admin.site.register(ContactLog)
admin.site.register(Materials)

