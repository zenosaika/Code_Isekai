from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CodeEditorForm
from .models import CodeEditor
import pip._vendor.requests as requests

# Create your views here.
def judge(request):
    if request.method == 'POST':
        code_editor_form = CodeEditorForm(request.POST)
        if code_editor_form.is_valid():
            code_editor_form.save()

            # Create Submission
            url = "https://judge0-ce.p.rapidapi.com/submissions"
            querystring = {"base64_encoded":"false", "fields":"*"}
            payload = {
                "language_id": code_editor_form.cleaned_data['lang'],
                "source_code": code_editor_form.cleaned_data['code'],
                "stdin": "10"
            }
            headers = {
                "content-type": "application/json",
                "Content-Type": "application/json",
                "X-RapidAPI-Key": "e2a57abc68msh4154133e8da5d82p1fe623jsn8ddbcf7ff31b",
                "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
            }
            response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

            # Get Submission
            url = f"https://judge0-ce.p.rapidapi.com/submissions/{response.json()['token']}"
            querystring = {"base64_encoded":"false", "fields":"*"}
            headers = {
                "X-RapidAPI-Key": "e2a57abc68msh4154133e8da5d82p1fe623jsn8ddbcf7ff31b",
                "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)

            messages.success(request, f"RESPONSE: {response.text}")
            return redirect('/judge')
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
    return render(request, 'Judge/judge.html', {'code_editor_form':code_editor_form})
