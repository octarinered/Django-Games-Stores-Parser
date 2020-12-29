from django import forms

class searchGameForm(forms.Form):
    gameName = forms.CharField(label = "", widget=forms.TextInput(attrs={"placeholder":"Search..."}))
