# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ElectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'city', 'state', 'county')
    list_filter = ('date', 'city', 'state', 'county')


class PoliticalBodyAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'type_of_body', 'city', 'state', 'county')
    list_filter = ('id', 'name', 'type_of_body', 'city', 'state', 'county')
    search_fields = ('name',)


class OfficeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'political_body', 'term_start', 'term_end')
    list_filter = (
        'political_body',
        'term_start',
        'term_end',
        'id',
        'name',
        'political_body',
        'term_start',
        'term_end',
    )
    search_fields = ('name',)


class PoliticalActionCommitteeAdmin(admin.ModelAdmin):

    list_display = ('committee_id', 'name')
    list_filter = ('committee_id', 'name')
    search_fields = ('name',)


class CandidacyInline(admin.TabularInline):
    model = models.Candidacy


class OfficeTentureInline(admin.TabularInline):
    model = models.OfficeTenure


class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'nickname', 'tenures', 'candidacies')
    search_fields = ('last_name', 'first_name')
    inlines = [
        CandidacyInline,
        OfficeTentureInline,
    ]


class OfficeTenureAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'office',
        'office_holder',
        'start_date',
        'end_date',
    )
    list_filter = (
        'office',
        'office_holder',
        'start_date',
        'end_date',
        'id',
        'office',
        'office_holder',
        'start_date',
        'end_date',
    )


class CandidacyAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'election',
        'office',
        'candidate',
        'ballot_order',
        'incumbent',
    )
    list_filter = (
        'election',
        'office',
        'candidate',
        'incumbent',
        'id',
        'election',
        'office',
        'candidate',
        'ballot_order',
        'incumbent',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Election, ElectionAdmin)
_register(models.PoliticalBody, PoliticalBodyAdmin)
_register(models.Office, OfficeAdmin)
_register(models.PoliticalActionCommittee, PoliticalActionCommitteeAdmin)
_register(models.Person, PersonAdmin)
_register(models.OfficeTenure, OfficeTenureAdmin)
_register(models.Candidacy, CandidacyAdmin)
