from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Livro, Autor, AutorLivro

def index(request):
    aux = Livro.objects.all()
    livros = []
    if len(aux) <= 6:
        livros = aux
    else:
        for i in range(6):
            livros.append(aux[i])

    context = {'livros': livros, 'pag': 'index'}
    template = loader.get_template('app/header.html')
    return HttpResponse(template.render(context, request))

def detalhes(request, titulo):
    if '-' in titulo:
        titulo = titulo.replace('-', ' ')

    livro = Livro.objects.get(titulo=titulo)
    try:
        autor = AutorLivro.objects.get(livro=livro)
    except:
        autor = None
    
    context = {'livro': livro, 'autor': autor, 'pag': 'detalhes'}
    template = loader.get_template('app/header.html')
    return HttpResponse(template.render(context, request))
    
def methAutor(request):
    if request.method == 'POST':
        op = request.POST['frmOp']
        if op == 'cadastrar':
            Pnome = request.POST['txtNome']
            Pano = request.POST['txtAno']

            autor = Autor(nome=Pnome, anoNasc=Pano)
            autor.save()

    context = {'pag': 'cadastroAutor'}
    template = loader.get_template('app/header.html')
    return HttpResponse(template.render(context, request))

def methLivro(request):
    if request.method == 'POST':
        op = request.POST['frmOp']
        if op == 'cadastrar':
            Ptitulo = request.POST['txtTitulo']; Ptitulo = Ptitulo.replace('-', ' ').replace(':', '')
            Pano = request.POST['txtAno'] + '-01-01'
            Pdescricao = request.POST['txtDescricao']
            Pcapa = request.POST['imgCapa']
            Pautor = request.POST['cbxAutor']
            Pautor = Autor.objects.get(nome=Pautor)
            
            livro = Livro(titulo=Ptitulo, ano=Pano, descricao=Pdescricao, capa=Pcapa)
            livro.save()

            AutorLivro(autor=Pautor, livro=livro).save()

    autores = Autor.objects.all()
    context = {'pag': 'cadastroLivro', 'autores': autores}
    template = loader.get_template('app/header.html')
    return HttpResponse(template.render(context, request))

def listaTodosLivros(request, num=1):
    livros = Livro.objects.all()

    pagination = []
    if len(livros) > 5:
        aux = []
        for i in range(len(livros)):
            if len(aux) == 5:
                pagination.append(aux)
                aux = []
            else:
                aux.append(livros[i])
        pagination.append(aux)

        dic = {}
        for i in reversed(range(len(pagination))):
            dic[str(i+1)] = pagination[i]

        total = list(range(1, len(dic)+1))
        livros = dic[num]
    else:
        total = [1]

    context = {'livros': livros, 'pag': 'todosLivros', 'ultimo': total[-1], 'atual': int(num), 'total': total, 'prox': int(num)+1, 'ant': int(num)-1}
    template = loader.get_template('app/header.html')
    return HttpResponse(template.render(context, request))

def listaTodosAutores(request, num=1):
    autores = Autor.objects.all()
    autLivr = AutorLivro.objects.all()

    pagination = []
    if len(autores) > 10:
        aux = []
        for i in range(len(autores)):
            if len(aux) == 10:
                pagination.append(aux)
                aux = []
            else:
                aux.append(autores[i])
        pagination.append(aux)

        dic = {}
        for i in reversed(range(len(pagination))):
            dic[str(i+1)] = pagination[i]

        total = list(range(1, len(dic)+1))
        autores = dic[num]
    else:
        total = [1]

    quant = {}
    for autor in autores:
        aux = 0
        for item in autLivr:
            if item.autor == autor:
                aux += 1
        quant[autor] = aux

    context = {'autores': autores, 'quant': quant, 'pag': 'todosAutores', 'ultimo': total[-1], 'atual': int(num), 'total': total, 'prox': int(num)+1, 'ant': int(num)-1}
    template = loader.get_template('app/header.html')
    return HttpResponse(template.render(context, request))