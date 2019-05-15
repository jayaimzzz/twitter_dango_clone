from django import forms

class WriteTweetForm(forms.Form):
    body = forms.CharField(max_length=140)