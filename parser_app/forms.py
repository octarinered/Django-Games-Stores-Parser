from django import forms

class searchGameForm(forms.Form):
    gameName = forms.CharField()