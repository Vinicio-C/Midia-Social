# Midia-Social
Criação de mídia social em Django

IMPORTANTE
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Se você não conhece django precisa utilizar os seguintes comandos no cmd - Prompt de comando para fazer o banco de dados funcionar.
Na pasta onde está o arquivo manage.py realizar os seguintes comandos

Este comando serve para verificar se foram feitas atualizações no banco de dados
python manage.py makemigrations

Este comando serve para enviar essas atualizações para o banco
python manage.py migrate

E por fim, para fazer o site funcionar
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
