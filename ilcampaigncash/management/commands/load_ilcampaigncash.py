import requests
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from electoraid.models import Committee, Person

ILCAMPAIGNCASHURL = 'https://il-campaign-finance-api.herokuapp.com/v1/graphql'

# Uncomment the following to play with caching
#ILCAMPAIGNCASHURL = 'https://cdn.fastql.io/v1/thechicagoreporter'


PERSONQUERY = """
    {
        candidates {
            id
            first_name
            last_name
        }
    }
"""

COMMITTEEQUERY = """
    {
        committees {
            id
            name
        }
    }
"""

class Command(BaseCommand):
    help = 'Fetch data from the Illinois Campaign Cash API'

    # def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)

    def run_query(self, query):
        resp = requests.post(url=ILCAMPAIGNCASHURL, json={'query': query})
        return resp.json().get('data')

    def load_people(self):
        data = self.run_query(PERSONQUERY)
        for candidate in data.get('candidates'):
            candidate['candidate_id'] = candidate.pop('id')
            person, created = Person.objects.get_or_create(**candidate)
            if created:
                self.stdout.write('created {first_name} {last_name} ({candidate_id})'.format(**candidate))
            else:
                self.stdout.write('skipped {first_name} {last_name} ({candidate_id})'.format(**candidate)) 
        
    def load_committees(self):
        data = self.run_query(COMMITTEEQUERY)
        for committee in data.get('committees'):
            committee['committee_id'] = committee.pop('id')
            db_committee, created = Committee.objects.get_or_create(**committee)
            if created:
                self.stdout.write('created {name} ({committee_id})'.format(**committee))
            else:
                self.stdout.write('skipped {name} ({committee_id})'.format(**committee)) 

    def handle(self, *args, **options):
        self.stdout.write('--- loading committees ---\n')    
        self.load_committees()

        self.stdout.write('--- loading people ---\n')    
        self.load_people()