import graphene
from graphene_django.types import DjangoObjectType
from .models import Person


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class Query(object):
    all_people = graphene.List(PersonType)

    def resolve_all_people(self, info, **kwargs):
        return Person.objects.all()
