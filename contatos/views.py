from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    contatos = Contato.objects.order_by('nome').filter(
        mostrar = True
    )
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, "contatos/index.html",{
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if contato.mostrar == False:
        raise Http404()
    return render(request, "contatos/ver_contato.html",{
        'contato': contato
    })


def buscar(request):
    termo = request.GET.get('termo')
    if termo != "" or None:
        contatos = Contato.objects.all().filter(
            mostrar=True,
            nome__icontains = termo
        )
    else:
        contatos = Contato.objects.all().filter(
            mostrar=True
        )

    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, "contatos/buscar.html", {
        'contatos': contatos
    })
