# Midia-Social
Criação de mídia social em Django

IMPORTANTE
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Se você não conhece django precisa utilizar os seguintes comandos no cmd - Prompt de comando para fazer o banco de dados funcionar.
Na pasta onde está o arquivo manage.py realizar os seguintes comandos

Este comando serve para verificar se foram feitas atualizações no banco de dados:
python manage.py makemigrations

Este comando serve para enviar essas atualizações para o banco:
python manage.py migrate

E por fim, para fazer o site funcionar:
python manage.py runserver

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Projeto realizado em Python utilizando o framework Django, foi um projeto bem básico até porque não tem as mesmas funções que normalmente teria um site de mídia social, nele existe diversas telas, começando pela primeira:

signup.html
Criado para cadastro de usuários com os seguintes requerimentos - Nome de usuário, email, senha e confirmação de senha

signin.html
Utilizado para logar em uma conta com os requerimentos - Nome de usuário e senha

Todos apartir de agora exigem uma confirmação de login de usuário

setting.html
Configura o perfil do usuário com: foto de perfil, biografia e localização.

profile.html
Aqui temos os posts do usuário, foto de perfil, biografia, localização, quantos posts ele tem, quantos perfis ele segue e quantos seguem ele

search.html
Sistema de procura de usuários cadastrados em banco de dados, mostrando os perfis dos usuários com base no nome de usuário pesquisado

index.html
Mostra os posts de pessoas que você segue, sugestões de usuários para seguir, sistema de curtidas de posts, download da imagem do post, upload de post, sistemas para sair da conta, configurações da conta e ver seu próprio perfil

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Inglish version:

# Social media
Creating Social Media in Django

IMPORTANT
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
If you don't know django you need to use the following commands in cmd - Command Prompt to make the database work.
In the folder where the manage.py file is, run the following commands

This command is used to check if updates have been made to the database:
python manage.py makemigrations

This command is used to send these updates to the database:
python manage.py migrate

And finally, to make the site work:
python manage.py runserver

-------------------------------------------------- -------------------------------------------------- -------------------------------------------------- ----------

Project carried out in Python using the Django framework, it was a very basic project because it does not have the same functions that a social media site would normally have, it has several screens, starting with the first one:

signup.html
Created for user registration with the following requirements - Username, email, password and password confirmation

signin.html
Used to log into an account with the requirements - Username and Password

All from now on require a user login confirmation

setting.html
Configure user profile with: profile picture, biography and location.

profile.html
Here we have the user's posts, profile picture, biography, location, how many posts he has, how many profiles he follows and how many follow him

search.html
Search system for users registered in the database, showing user profiles based on the searched user name

index.html
Shows the posts of people you follow, suggested users to follow, post likes system, post image download, post upload, account logout systems, account settings and view your own profile
