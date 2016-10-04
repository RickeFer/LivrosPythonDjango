from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^livros/todos/(?P<num>[0-9]+)/$', views.listaTodosLivros, name='listaTodosLivros'),
    url(r'^autores/todos/(?P<num>[0-9]+)/$', views.listaTodosAutores, name='listaTodosAutores'),
    url(r'^livros/(?P<titulo>\w([A-Za-z-])+)/$', views.detalhes, name='detalhes'),
    url(r'^cadastro/livro$', views.methLivro, name='methLivro'),
    url(r'^cadastro/autor$', views.methAutor, name='methAutor'),
    #url(r'^teste/(?P<pk>[0-9]+)/$', views.teste, name='teste'),
]