from django.shortcuts import render

def homepage(request):
    return render(request, 'Code_Isekai/homepage.html')