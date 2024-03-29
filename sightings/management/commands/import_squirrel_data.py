import csv
import pandas as pd
import re
from sightings.models import Sighting
from django.core.management.base import BaseCommand, CommandError
import dateutil.parser
from datetime import date
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csvfile',nargs='+', type=str)

    def handle(self, *args, **options):
        filepath = options['csvfile'][0]
        import os
        import csv
        #import datetime
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')
        with open(filepath, 'r') as csvFile:
            reader = csv.DictReader(csvFile, delimiter=',')
            list_ = []
            count = 0
            for line in reader:
               # line['Date'] = datetime.datetime.strptime(line['Date'],'%m%d%Y')
               # l = reader.line_num # Lines start numbering at 1, not 0
               # if line == []:
                #    line = next(reader) # Check for empty lines
               # if l == 1:
                #    header = line # Get field names
                 #   line = next(reader) # Move on to the first line of data
               # while line['Unique Squirrel ID'] in Sighting.objects.values_list('Unique_Squirrel_ID', flat=True):
                #    line['Unique Squirrel ID'] += '-R'
                m,d,y = re.match(pattern, line['Date']).groups()
                if line['Unique Squirrel ID'] in list_:
                    continue
                else:
                    list_.append(line['Unique Squirrel ID'])

                    s = Sighting(X=line['X'],
                        Y=line['Y'],
                        unique_squirrel_id=line['Unique Squirrel ID'],
                        Shift=line['Shift'],
                        Date=date(int(y),int(m),int(d)),
                        Age = line['Age'],
                        Primary_Fur_Color = line['Primary Fur Color'],
                        Location = line['Location'],
                        Specific_Location = line['Specific Location'],
                        Running = line['Running'],
                        Chasing = line['Chasing'],
                        Climbing = line['Climbing'],
                        Eating = line['Eating'],
                        Foraging = line['Foraging'],
                        Other_Activities = line['Other Activities'],
                        Kuks = line['Kuks'],
                        Quaas = line['Quaas'],
                        Moans = line['Moans'],
                        Tail_Flags = line['Tail flags'],
                        Tail_Twitches = line['Tail twitches'],
                        Approaches = line['Approaches'],
                        Indifferent = line['Indifferent'],
                        Runs_From = line['Runs from'])
                    s.save()
                    count = count+1
            print(count)
