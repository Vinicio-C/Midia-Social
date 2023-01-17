from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount

# Register your models here.
admin.site.register(Profile)#Criando uma tabela com o seguinte nome
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)