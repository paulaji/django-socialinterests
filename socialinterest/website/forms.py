from django import forms
from .models import NewLead


class AddNewLead(forms.ModelForm):
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Name"}))
    email = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Email"}))
    phone = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Phone"}))
    country = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Country"}))

    # now we need to add the meta data
    class Meta:
        # specify the model
        model = NewLead
        fields = ("name", "email", "phone", "country")