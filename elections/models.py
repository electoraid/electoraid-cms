from django.db import models
import graphene


class Election(models.Model):
    name = models.CharField(max_length=4096)
    date = models.DateField()
    city = models.CharField(max_length=512)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=512)
    
    def __str__(self):
        return self.name


class PoliticalBody(models.Model):
    name = models.CharField(max_length=4096)
    type_of_body = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=512)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Political bodies'


class Office(models.Model):
    name = models.CharField(max_length=4096)
    political_body = models.OneToOneField(PoliticalBody, on_delete=models.CASCADE)
    term_start = models.DateField()
    term_end = models.DateField()
    
    def __str__(self):
        return '{name} - {term_start} to {term_end}'.format(**self.__dict__)


class PoliticalActionCommittee(models.Model):
    committee_id = models.CharField(max_length=512, primary_key=True)
    name = models.CharField(max_length=4096)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    nickname = models.CharField(max_length=512, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    # @TODO join through "tenure"
    offices_held = models.ManyToManyField(Office, blank=True, \
                                     related_name='office_holders')
    political_action_committees = models.ManyToManyField(PoliticalActionCommittee, blank=True, \
                                    related_name='people')

    def __str__(self):
        if self.nickname:
            return '{first_name} "{nickname}" {last_name}'.format(**self.__dict__)
        else:
            return '{first_name} {last_name}'.format(**self.__dict__)
    
    class Meta:
        verbose_name_plural = 'People'


class Candidacy(models.Model):
    election = models.OneToOneField(Election, on_delete=models.CASCADE)
    office = models.OneToOneField(Office, on_delete=models.CASCADE)
    candidate = models.OneToOneField(Person, null=True, blank=True, \
                                  related_name='candidacies', on_delete=models.CASCADE)
    ballot_order = models.IntegerField(default=0)
    incumbent = models.BooleanField()
    
    def __str__(self):
        return '{candidate} - {office} - {election}'.format(office=self.office, candidate=self.candidate, election=self.election)
    
    class Meta:
        verbose_name_plural = 'Candidacies'

