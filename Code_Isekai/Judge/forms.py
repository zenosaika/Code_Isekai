from django.forms import ModelForm
from .models import CodeEditor

class CodeEditorForm(ModelForm):
    class Meta:
        model = CodeEditor
        fields = ['lang', 'code']
        