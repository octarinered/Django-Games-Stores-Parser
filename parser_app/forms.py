from django import forms

class searchGameForm(forms.Form):
    gameName = forms.CharField(label = "", widget=forms.TextInput(attrs={"class":"search-input","placeholder":"Search..."}))

