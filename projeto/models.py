from tabnanny import verbose
from django.db import models

# Create your models here.

class Inicio (models.Model):
    image = models.ImageField (verbose_name= 'Imagem da logo', upload_to ='fotos', default='')
    titulo1 = models.CharField(verbose_name= 'Titulo inicial parte 1', max_length=250)
    titulo2 = models.CharField(verbose_name= 'Titulo inicial parte 2', max_length=250)
    descricao1 = models.TextField(verbose_name= 'Mensagem de efeito parte 1', max_length=500, default='')
    descricao2 = models.TextField(verbose_name= 'Mensagem de efeito parte 2', max_length=500, default='')
    text_button = models.CharField(verbose_name= 'Texto-Botão', max_length=100)

def __str__ (self):
    return f'{self.titulo1}'

class QuemSomos(models.Model):
    titulo = models.CharField(verbose_name= 'Titulo de Quem Somos', max_length=250)
    image = models.ImageField(verbose_name= 'Imagem', upload_to ='fotos')
    descricao1 = models.TextField(verbose_name= 'Descrição de Quem Somos parte 1', max_length=250, default='')
    descricao2 = models.TextField(verbose_name= 'Descrição de Quem Somos parte 2', max_length=250, default='')

    def __str__ (self):
        return f'{self.titulo}'

class Servicos(models.Model):
    titulo = models.CharField(verbose_name= 'Titulo de Serviços', max_length=250)
    descricao1 = models.TextField(verbose_name= 'Descrição para decoração', max_length=250 , default='')
    descricao2 = models.TextField(verbose_name= 'Descrição para Segurança', max_length=250, default='')
    descricao3 = models.TextField(verbose_name= 'Descrição de Logistica', max_length=250, default='')
    descricao4 = models.TextField(verbose_name= 'Descrição de Comercialização', max_length=250, default='')
    descricao5 = models.TextField(verbose_name= 'Descrição de Planejamento', max_length=250, default='')
    descricao6 = models.TextField(verbose_name= 'Descrição de Infraestrutura', max_length=250 , default='')

    def __str__ (self):
        return f'{self.titulo}'

class Portfolio(models.Model):
    titulo = models.CharField(verbose_name= 'Titulo de Portfólio',max_length=250)
    image1 = models.ImageField(verbose_name= 'Imagem 1', upload_to ='fotos')
    image2 = models.ImageField(verbose_name= 'Imagem 2', upload_to ='fotos')
    image3 = models.ImageField(verbose_name= 'Imagem 3', upload_to ='fotos')
    image4 = models.ImageField(verbose_name= 'Imagem 4', upload_to ='fotos')
    image5 = models.ImageField(verbose_name= 'Imagem 5', upload_to ='fotos')
    image6 = models.ImageField(verbose_name= 'Imagem 6', upload_to ='fotos')
    
    comentario1 = models.TextField(verbose_name= 'Comentario 1', max_length=250)
    autor1 = models.CharField(verbose_name= 'Autor 1', max_length=50)
    comentario2 = models.TextField(verbose_name= 'Comentario 2', max_length=250)
    autor2 = models.CharField(verbose_name= 'Autor 2', max_length=50)
    comentario3 = models.TextField(verbose_name= 'Comentario 3', max_length=250)
    autor3 = models.CharField(verbose_name= 'Autor 3', max_length=50)
    comentario4 = models.TextField(verbose_name= 'Comentario 4', max_length=250)
    autor4 = models.CharField(verbose_name= 'Autor 4', max_length=50)
    def __str__ (self):
        return f'{self.titulo}'

class Contato(models.Model):
    titulo1 = models.CharField(verbose_name= 'Titulo de contato', max_length=250)
    whatsapp = models.CharField(verbose_name= 'Whatsapp', max_length=250)
    instagram = models.CharField(verbose_name= 'Instagram', max_length=250)
    email = models.EmailField(verbose_name= 'Email' )
    localizacao = models.CharField(verbose_name= 'Localização', max_length=250)
    def __str__ (self):
        return f'{self.email}'
        
class Formulario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=12)
    mensagem = models.CharField(max_length=500)
    def __str__ (self):
        return f'{self.nome}'

