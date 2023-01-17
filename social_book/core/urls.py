from django.urls import path
from . import views

#Colocando o nome de uma url
#precisa ser [
urlpatterns = [
    #criando url para página príncipal
    path('', views.index, name='index'),
    # criando um url para configurações da conta
    path('settings', views.settings, name='settings'),
    # criando um url para uploads de posts
    path('upload', views.upload, name='upload'),
    # criando url para a página de perfil com o nome de usuário depois da barra
    path('profile/<str:pk>', views.profile, name='profile'),
    # criando url para a adicionar/remover um follow
    path('follow', views.follow, name='follow'),
    # criando url para pesquisa de usuário
    path('search', views.search, name='search'),
    # criando um url para like dos posts
    path('like-post', views.like_post, name='like-post'),
    #criando um url para cadastro
    path('signup', views.signup, name='signup'),
    #criando um url para login
    path('signin', views.signin, name='signin'),
    #criando um url para sair da conta
    path('logout', views.logout, name='logout')
]