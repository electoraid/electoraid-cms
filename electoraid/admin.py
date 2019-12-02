# vim: set fileencoding=utf-8 :
from django.contrib import admin
from reversion.admin import VersionAdmin

from . import models


class ElectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date', 'city', 'state', 'county')
    list_filter = ('date', 'city', 'state', 'county')


class PoliticalBodyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type_of_body', 'city', 'state', 'county', 'id')
    list_filter = ('id', 'name', 'type_of_body', 'city', 'state', 'county')
    search_fields = ('name',)


class OfficeAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('name', 'slug', 'political_body', 'term_start', 'term_end', 'id')
    readonly_fields = ('slug',)
    list_filter = (
        'political_body',
        'name',
        'term_start',
        'term_end',
    )
    search_fields = ('name',)


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'committee_id')
    list_filter = ('committee_id', 'name')
    search_fields = ('name',)
    readonly_fields = ('slug',)


class CandidacyInline(admin.TabularInline):
    model = models.Candidacy


class OfficeTentureInline(admin.TabularInline):
    model = models.OfficeTenure


class PersonAdmin(VersionAdmin):
    list_display = ('last_name', 'first_name', 'nickname', 'slug', 'tenures', 'candidacies')
    search_fields = ('last_name', 'first_name')
    autocomplete_fields = ['committees']
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
_register(models.Committee, CommitteeAdmin)
_register(models.Person, PersonAdmin)
_register(models.OfficeTenure, OfficeTenureAdmin)
_register(models.Candidacy, CandidacyAdmin)
