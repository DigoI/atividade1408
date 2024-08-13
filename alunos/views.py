from django.shortcuts import render

# Create your views here.
from .models import Aluno

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': alunos})
