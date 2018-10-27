from django import forms
from django.core.exceptions import ValidationError
from .choices import *

class NewProjectForm (forms.Form):
    def __init__(self, data = None, *args, **kwargs):
        super(NewProjectForm, self).__init__(data = data, *args, **kwargs)
        self.action = data.get('add_project') if data else None
        if self.action == 'Add':
            self.fields['project_name'].required = True

    project_name = forms.CharField(required = False)

    def clean_project_name(self):
        data = self.cleaned_data['project_name']
        return data

class NonRadioactiveParameters(forms.Form):

    waste_type = forms.ChoiceField(choices = WASTE_TYPE_CHOICES, label = "", initial = "", widget = forms.Select(), required = True)
    weight_net = forms.FloatField(min_value = 0.001)
    volume_net = forms.FloatField(min_value = 0.001)

    # Cleaning data
    def clean_waste_type(self):
        data = self.cleaned_data['waste_type']
        return data

    def clean_weight_net(self):
        data = self.cleaned_data['weight_net']
        return data

    def clean_volume_net(self):
        data = self.cleaned_data['volume_net']
        return data

class RadioactiveParameters(forms.Form):

    rn_name = forms.CharField(required=False)
