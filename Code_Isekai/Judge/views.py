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
            form = code_editor_form.cleaned_data

            # Create Submission
            url = "https://judge0-ce.p.rapidapi.com/submissions"
            querystring = {"base64_encoded":"false", "fields":"*"}
            payload = {
                "language_id": form['lang'],
                "source_code": form['code'],
                "stdin": "10"
            }
            headers = {
                "content-type": "application/json",
                "Content-Type": "application/json",
                "X-RapidAPI-Key": "e2a57abc68msh4154133e8da5d82p1fe623jsn8ddbcf7ff31b",
                "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
            }
            response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
            token = response.json()['token']

            code_editor = CodeEditor.objects.filter(user=request.user)
            if code_editor:
                code_editor = code_editor[0]
            else:
                code_editor = CodeEditor(user=request.user)
            
            code_editor.lang = form['lang']
            code_editor.code = form['code']
            code_editor.token = token
            code_editor.is_token_used = False
            code_editor.save()

            return redirect('/judge')
        
    code_editor_form = CodeEditorForm()
    code_editor = CodeEditor.objects.filter(user=request.user)
    
    if code_editor:
        code_editor = code_editor[0]

        if code_editor.is_token_used == False:
            token = code_editor.token

            # Get Submission
            url = f"https://judge0-ce.p.rapidapi.com/submissions/{token}"
            querystring = {"base64_encoded":"false", "fields":"*"}
            headers = {
                "X-RapidAPI-Key": "e2a57abc68msh4154133e8da5d82p1fe623jsn8ddbcf7ff31b",
                "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            code_editor.response = response.json()
            code_editor.stdout = response.json()['stdout']
            code_editor.is_token_used = True
            code_editor.save()

        stdout = code_editor.stdout
        code_editor_form['code'].initial = code_editor.code
        code_editor_form['lang'].initial = code_editor.lang
        return render(request, 'Judge/judge.html', {'code_editor_form':code_editor_form, 'stdout':stdout})
    
    return render(request, 'Judge/judge.html', {'code_editor_form':code_editor_form})
