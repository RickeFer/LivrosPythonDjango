from django.db import models
import PIL 
from PIL import Image
from stdimage import StdImageField

class Autor(models.Model):
    nome = models.CharField('Autor', max_length=50)
    anoNasc = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField('Editora', max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    ano = models.PositiveSmallIntegerField()
    descricao = models.CharField(max_length=1500)
    capa = StdImageField(upload_to='capas', variations={'normal': (370, 530, True), 'thumbnail': (170, 230, True), 'minithumb': (100, 160)})
    
    def ChamarUrl(self):
        aux = self.titulo
        return aux.replace(' ', '-')

    def Resumo(self):
        if len(self.descricao) > 300:
            aux = ''
            for c in range(300):
                aux += self.descricao[c]
            return aux + '...'
        else:
            return self.descricao

    def __str__(self):
        return self.titulo

class AutorLivro(models.Model):
    autor = models.ForeignKey(Autor)
    livro = models.ForeignKey(Livro)

class EditoraLivro(models.Model):
    editora = models.ForeignKey(Editora)
    livro = models.ForeignKey(Livro)
