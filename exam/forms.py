from django import forms
from .models import *


class TestForm(forms.Form):
    Test=(  ('------------','-------------'),
            ('WT','WEEKLY-TEST'),
            ('ST','SPECIAL-TEST'),)
    test = forms.ChoiceField(
        choices=Test,
        label='test',
        # widget=forms.Select(
        #     attrs={'class': 'form-control'}
        # )
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.none(),
        required=False
    )
    testid = forms.ModelChoiceField(
        queryset=Testid.objects.none(),
        required=False
    )

    class Meta:
        fields = ('test', 'subject', 'testid')

    def __init__(self, test=None, subject=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(tname=test)
        if subject:
            self.fields['testid'].queryset = Testid.objects.filter(
                sub=subject)
