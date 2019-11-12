import graphene
from graphene_django.types import DjangoObjectType
from .models import *


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class CandidacyType(DjangoObjectType):
    class Meta:
        model = Candidacy


class OfficeTenureType(DjangoObjectType):
    class Meta:
        model = OfficeTenure


class PoliticalActionCommitteeType(DjangoObjectType):
    class Meta:
        model = PoliticalActionCommittee


class OfficeType(DjangoObjectType):
    class Meta:
        model = Office


class ElectionType(DjangoObjectType):
    class Meta:
        model = Election


class PoliticalBodyType(DjangoObjectType):
    class Meta:
        model = PoliticalBody


class Query(object):
    all_people = graphene.List(PersonType)
    all_candidacies = graphene.List(CandidacyType)
    all_political_action_committees = graphene.List(PoliticalActionCommitteeType)
    all_office_tenures = graphene.List(OfficeTenureType)
    all_offices = graphene.List(OfficeType)
    all_elections = graphene.List(ElectionType)
    all_political_bodies = graphene.List(PoliticalBodyType)

    def resolve_all_people(self, info, **kwargs):
        return Person.objects.select_related('candidacies').all()
    
    def resolve_all_candidacies(self, info, **kwargs):
        return Candidacy.objects.all()

    def resolve_all_political_action_committees(self, info, **kwargs):
        return PoliticalActionCommittee.objects.all()

    def resolve_all_office_tenures(self, info, **kwargs):
        return OfficeTenure.objects.all()