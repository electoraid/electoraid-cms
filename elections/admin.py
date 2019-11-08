from django.contrib import admin
from .models import Person, Election, Candidacy, PoliticalBody, Office, PoliticalActionCommittee

# Register your models here.
admin.site.register(Person)
admin.site.register(Election)
admin.site.register(Candidacy)
admin.site.register(PoliticalBody)
admin.site.register(PoliticalActionCommittee)
admin.site.register(Office)