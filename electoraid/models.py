from django.db import models


class Election(models.Model):
    slug = models.SlugField(null=True)
    name = models.CharField(max_length=4096)
    date = models.DateField()
    city = models.CharField(max_length=512)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=512, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class PoliticalBody(models.Model):
    slug = models.SlugField(null=True)
    name = models.CharField(max_length=4096)
    type_of_body = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=512, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Political bodies'


class Office(models.Model):
    slug = models.SlugField(null=True)
    name = models.CharField(max_length=4096)
    political_body = models.ForeignKey(PoliticalBody, on_delete=models.CASCADE)
    term_start = models.DateField()
    term_end = models.DateField(null=True, blank=True)
    
    def __str__(self):
        ordering = ['name', '-term_start']
        return '{name} - {term_start} to {term_end}'.format(**self.__dict__)


class Committee(models.Model):
    slug = models.SlugField(null=True)
    committee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=4096)

    def __str__(self):
        ordering = ['name']
        return self.name


class Person(models.Model):
    slug = models.SlugField(null=True)
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    nickname = models.CharField(max_length=512, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    candidate_id = models.IntegerField(null=True, blank=True)
    committees = models.ManyToManyField(Committee, blank=True, \
                                    related_name='people')

    def __str__(self):
        if self.nickname:
            return '{first_name} "{nickname}" {last_name}'.format(**self.__dict__)
        else:
            return '{first_name} {last_name}'.format(**self.__dict__)
    
    class Meta:
        ordering = ['last_name']
        verbose_name_plural = 'People'


class OfficeTenure(models.Model):
    office = models.OneToOneField(Office, on_delete=models.CASCADE)
    office_holder = models.OneToOneField(Person, null=True, blank=True, \
                                  related_name='tenures', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.office.__str__()

    class Meta:
        ordering = ['start_date']


class Candidacy(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    office = models.OneToOneField(Office, on_delete=models.CASCADE)
    candidate = models.OneToOneField(Person, null=True, blank=True, \
                                  related_name='candidacies', on_delete=models.CASCADE)
    ballot_order = models.IntegerField(default=0)
    incumbent = models.BooleanField()
    
    def __str__(self):
        return '{candidate} - {office} - {election}'.format(office=self.office, candidate=self.candidate, election=self.election)
    
    class Meta:
        ordering = ['election', 'candidate', 'ballot_order']
        verbose_name_plural = 'Candidacies'

