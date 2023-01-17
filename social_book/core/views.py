from django.shortcuts import render, redirect
from django.contrib import messages #Permite fazer aparecer mensagens
from django.contrib.auth.models import User, auth #Vai permitir autenticar os usuários
from .models import Profile, Post, LikePost, FollowersCount #Importando a classe profile e post do projeto models
from django.contrib.auth.decorators import login_required #Verifica se o usuário está logado
from django.http import HttpResponse
from itertools import chain
import random

# Create your views here.

#Verifica se o usuário está logado, se não, ele volta para a página de login
@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)#Pegando o nome de usuário do banco de dados
    try:
        user_profile = Profile.objects.get(user=user_object)#Pegando a foto de perfil do banco de dados
    except Exception as ex:
        print(ex)
        user_profile = None

    #Configurando a parte de visualizar somente os posts que a pessoa segue
    user_following_list = []
    feed = []

    #Pegando os usuários que o usuário segue
    user_following = FollowersCount.objects.filter(follower=request.user.username)

    #Colocando em uma list todos os usuários que ele segue
    for users in user_following:
        user_following_list.append(users.user)

    #Autênticando os usuários e colocando em outra lista
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    posts = Post.objects.all()

    #Sugestão de usuários
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(all_users) if(x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if (x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    #Retornando seguinte mensagem
    #return HttpResponse('<h1>Welcome To Social Book</h1>')#Isso será impresso em uma página
    #Abre o seguinte html
    return render(request, 'index.html', {'user_profile': user_profile, 'posts': feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})#Além de abrir o html ele manda a foto do usuário

@login_required(login_url='signin')
def upload(request):
    #Adicionando informações no banco de dados
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def search(request):
    #Pegando os valores contidos no banco de dados
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    #Verifica se foi acessado pelo método POST
    if request.method == 'POST':
        #Pegando os valores do html
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        #Carregando lista de usuários com base no nome
        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)

        username_profile_list = list(chain(*username_profile_list))
    else:
        return redirect('/')

    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})

@login_required(login_url='signin')
def like_post(request):
    #Carregando o banco de dados nas variáveis
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    #Adicionando os likes no banco de dados e retirando-os
    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')

@login_required(login_url='signin')
def profile(request, pk):
    #Pegando com base no nome que foi passado no url as informações do usuário no banco de dados
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    #Pegando informações sobre os followers do usuário
    follower = request.user.username
    user = pk

    #Renomeando o botão se tiver seguido o usuário ou não
    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Parar de seguir'
    else:
        button_text = 'Seguir'

    #Pegando total de seguidores e quem está seguindo
    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }

    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def follow(request):
    #If para o caso de o usuário ter apertado pra dar follow
    if request.method == 'POST':
        #Conseguindo pegar o valor do html
        follower = request.POST['follower']
        user = request.POST['user']

        #Dando follow quando não havia dado e dando unfollow quando já deu follow
        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()

            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')

@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    #Verifica se o site foi aberto pelo método post
    if request.method == 'POST':
        #Verifica se a imagem ta vazia
        if request.FILES.get('image') == None:
            #Pega todas as informações do html e passa para as seguintes variáveis
            #Como não tem imagem ele reescreve como a última imagem mesmo
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            #Salvando informações no banco de dados
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        elif request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            # Salvando informações no banco de dados
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('settings')

    return render(request, 'setting.html', { 'user_profile': user_profile })

def signup(request):
    #Se a pessoa que entrou no site entrou por causa do botão de cadastro ela cai nesse if
    #Caso contrário, ela somente entra no site
    if request.method == 'POST':
        #Recebendo todos os valores entrados nas caixas de texto do cadastro
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Verifica se as duas senhas são iguais
        if password == password2:
            #Verifica se o email já existe no banco de dados
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email já existe')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nome de usuário já existe')
                return redirect('signup')
            else:
                #Salvando usuário no banco de dados
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #Autênticando para entrar na página de configurações da conta
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            #Imprime uma mensagem e redireciona o usuário para a mesma página
            messages.info(request, 'As senhas não batem')
            return redirect('signup')

    else:
        return render(request, 'signup.html')

def signin(request):

    #Verifica se ele entrou na página pelo método POST ou não
    if request.method == 'POST':
        #Pegando os valores das caixas de texto
        username = request.POST['username']
        password = request.POST['password']

        #Autenteicando as variáveis com as variáveis do banco de dados
        user = auth.authenticate(username=username, password=password)

        #Verificando se o usuário é nulo
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'As credenciais estão incorretas')
            return redirect('signin')

    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    #Saindo da conta e voltando para a tela de login
    auth.logout(request)
    return redirect('signin')