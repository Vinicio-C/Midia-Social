from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
# Criando autênticador de usuário
class Profile(models.Model):
    objects = models.Manager()#Se torna os objetos desta classe
    #Isso tudo estará no banco de dados
    #Conectando o usuário a uma primarykey
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Denominando como uma variável inteira
    id_user = models.IntegerField()
    #Variável sendo do tipo texto e começando como padrão em branco
    bio = models.TextField(blank=True)
                                  #Aqui diz que, se nenhuma foto for carregada ele carrega a que está no default
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile.png')#Usando biblioteca para carregar a imagem
    #Denominando variável do tipo char, com o máximo de caracteres sendo 100 e começando em branco
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username #Retornando o nome de usuário

#Criando informações para o banco de dados que iremos criar para as postagens
class Post(models.Model):
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

# Criando banco de dados para as curtidas dos posts
class LikePost(models.Model):
    objects = models.Manager()
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Criando banco de dados para follows
class FollowersCount(models.Model):
    objects = models.Manager()
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user