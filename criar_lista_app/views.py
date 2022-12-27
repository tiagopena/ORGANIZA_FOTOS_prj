from django.shortcuts import render


def menu(request):
    conteudo = {
        'x' : 'x'
    }

    return render(request, 'menu.html', context=conteudo)

# Create your views here.
