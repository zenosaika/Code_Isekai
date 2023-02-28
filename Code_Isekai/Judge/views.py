from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CodeEditorForm
from .models import CodeEditor

# Create your views here.
def judge_test(request):
    if request.method == 'POST':
        code_editor_form = CodeEditorForm(request.POST)
        if code_editor_form.is_valid():
            code_editor_form.save()
            messages.success(request, 'Submit the code successful. Please wait a second!')
            return redirect('/judge_test')
    try:
        code_editor = list(CodeEditor.objects.all())
        for each_record in code_editor[:-1]:
            each_record.delete()
        code_editor = code_editor[-1]
    except:
        code_editor = CodeEditor(code="print('Hello, world!')", lang=71)
        code_editor.save()
    code_editor_form = CodeEditorForm()
    code_editor_form['code'].initial = code_editor.code
    code_editor_form['lang'].initial = code_editor.lang
    return render(request, 'Judge/judge_test.html', {'code_editor_form':code_editor_form})