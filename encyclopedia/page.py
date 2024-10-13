from django import forms

class NewPageForm(forms.Form):
    topic = forms.CharField(label="Topic",required=True)
    content = forms.CharField(label="Content",widget=forms.Textarea(attrs={
        'placeholder' : 'Enter page content in markdown.',
        'style': 'display:block; height: 400px;'
    }))