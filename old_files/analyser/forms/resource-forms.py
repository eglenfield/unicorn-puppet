from django import forms

class ResourceForm(forms.Form):
    resource = forms.CheckboxInput()