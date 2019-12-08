#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import csv

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models.fields import FieldDoesNotExist

class Command(BaseCommand):
    args = '/home/sc4619/project/squirrels/rows.csv'
    help = 'Import `rows`.csv into `rows` database.'

    def handle(self, *args, **options):
        '''
        /home/sc4619/project/squirrels/rows.csv
        '''
        path = args[0]
        reader = csv.reader(open(path, 'rb'), delimiter=',', quotechar="'")
        for line in reader:
            l = reader.line_num # Lines start numbering at 1, not 0
            if line == []:
                line = reader.next() # Check for empty lines

            if l == 1:
                header = line # Get field names
                line = reader.next() # Move on to the first line of data

            data_dict = {}
            for field in header:
                # Reformat the column names for personal preference/system requirements
                model_field = field.lower()

                value = line[header.index(field)] # The value for that field

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'squirrels.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
