from django.contrib import admin
from .models import Person, Election, Candidacy, PoliticalBody, Office, PoliticalActionCommittee


class CandidacyInline(admin.TabularInline):
    model = Candidacy

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        CandidacyInline,
    ]

admin.site.register(Person, PersonAdmin)
admin.site.register(Election)
admin.site.register(Candidacy)
admin.site.register(PoliticalBody)
admin.site.register(PoliticalActionCommittee)
admin.site.register(Office)