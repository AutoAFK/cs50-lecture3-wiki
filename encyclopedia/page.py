from django import forms

class NewPageForm(forms.Form):
    topic = forms.CharField(label="Topic",required=True)
    content = forms.CharField(label="Content",widget=forms.Textarea(attrs={
        'placeholder' : 'Enter page content in markdown.',
        'style': 'display:block; height: 400px;'
    }))

class EditPageForm(forms.Form):
    content = forms.CharField(label="Content",widget=forms.Textarea(attrs={
        'style': 'display:block; height: 400px;'
    }),min_length=1)

    def __init__(self, file, *args, **kwargs):
        super(EditPageForm, self).__init__(*args, **kwargs)
        with open(f"./entries/{file}.md", 'r') as f:
            self.fields['content'].initial = f.read()

def save_data_to_file(file,content):
    with open(f'./entries/{file}.md','w') as f:
        f.write(content)
