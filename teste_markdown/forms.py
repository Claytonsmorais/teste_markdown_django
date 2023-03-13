from ckeditor.widgets import CKEditorWidget
from django import forms

class TesteForm(forms.Form):
    your_name = forms.CharField(widget=CKEditorWidget())