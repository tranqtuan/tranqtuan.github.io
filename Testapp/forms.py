# coding=utf-8
from django import forms


OPTION_CHOICES = (('1', 'Positive'),
                  ('2', 'Negative'),
                  ('3', 'Neither'))


class TestForm(forms.Form):
    subject = forms.CharField(max_length=100, label="Type or paste your text here:")
    message = forms.CharField(max_length=500, label="Enter the name of the target brand or product here:", required=False, widget=forms.Textarea)
    option = forms.ChoiceField(label='What is your assessment of the text’s attitude towards the target?', widget=forms.RadioSelect, choices=OPTION_CHOICES)
