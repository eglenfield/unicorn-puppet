from django import forms

class OsForm(forms.Form):
    os = forms.CheckboxInput()