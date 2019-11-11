import graphene
from graphene_django.types import DjangoObjectType
from .models import Person, Candidacy, PoliticalActionCommittee


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class CandidacyType(DjangoObjectType):
    class Meta:
        model = Candidacy


class PoliticalActionCommitteeType(DjangoObjectType):
    class Meta:
        model = PoliticalActionCommittee

class Query(object):
    all_people = graphene.List(PersonType)
    all_candidacies = graphene.List(CandidacyType)
    all_political_action_committees = graphene.List(PoliticalActionCommitteeType)

    def resolve_all_people(self, info, **kwargs):
        return Person.objects.select_related('candidacies').all()
    
    def resolve_all_candidacies(self, info, **kwargs):
        return Candidacy.objects.all()

    def resolve_all_political_action_committees(self, info, **kwargs):
        return PoliticalActionCommittee.objects.all()