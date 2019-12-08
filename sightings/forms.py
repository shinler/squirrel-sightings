from django.forms import ModelForm
from sightings.models import Sighting

# Create the form class
class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
        #fields = ['X', 'Y', 'unique_squirrel_id', 'Shift', 'Date', 'Age', 'Primary_Fur_Color', 'Location', 'Specific_Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other_Activities', 'Kuks', 'Quaas', 'Moans', 'Tail_Flags', 'Tail_Twitches', 'Approaches', 'Indifferent', 'Runs_From']
