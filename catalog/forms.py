from django import forms

class LocationForm(forms.Form):
    location = forms.CharField(label="ENTER LOCATION", max_length=300, strip=True)