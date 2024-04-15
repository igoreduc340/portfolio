from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def skills(request):
    return render(request,'skills.html')

def projetos(request):
    return render(request,'projetos.html')

def sobre(request):
    return render(request,'sobre.html')

def contatos(request):
    return render(request,'contatos.html')