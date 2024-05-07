# administrador-usuarios-api-flask-mysql

# API de Gerenciamento de Usuários com Login Integrado

Esta API foi desenvolvida com Flask para gerenciar usuários em um banco de dados MySQL e MongoDB. Além disso, inclui um sistema de login integrado, permitindo que os usuários se autentiquem através da API antes de acessar as funcionalidades CRUD.

## Funcionalidades

- **Login de Usuários:** A API permite que os usuários façam login através da API antes de acessar as funcionalidades CRUD.
- **CRUD de Usuários:** Após o login, os usuários podem criar, ler, atualizar e excluir registros de usuários nos bancos de dados MySQL e MongoDB.

## Configuração e Uso

1. Clone este repositório:
```bash
git git@github.com:luan-brandao/administrador-usuarios-api-flask-mysql.git
```

2. Rode os servidores:
```bash
no ../api:
npm run dev

no ../sistema_flask
python3 app.py
```

## Tela de Login 
O usuario preenche o formulario de login q esta dentro da aplicação node, com a seguinte url: 
```
url: http://localhost:3000/
```

![login: ](https://drive.google.com/uc?id=1JAe8UYU-IoQ1PxtQZeBbCZk9YaaJQKVf)


## Tela de Usuarios

Assim que o login é aceito, voce é direcionado para a tela de lista de usuarios na aplicação flask

A tela de "Lista de Usuários" exibe uma tabela com os registros de usuários armazenados no banco de dados. Cada linha da tabela representa um usuário e exibe as seguintes informações:

ID: O identificador único do usuário.
Nome: O nome do usuário.
Email: O endereço de email do usuário.
Senha: A senha do usuário.
Além disso, cada linha da tabela inclui botões de ação para interagir com os usuários:

Atualizar: Permite atualizar as informações de um usuário específico.

Deletar: Permite excluir um usuário específico do banco de dados.

A URL da lista de usuarios :
````
http://127.0.0.1:5000/users
````


![Usuarios](https://drive.google.com/uc?id=1BwmXqrhCh6qGp7b8ZgWG_SZlZQQfaTkJ)

## Botão de Criar Usuário
O botão de "Criar Usuário" permite adicionar novos usuários ao banco de dados. Ao clicar neste botão, um formulário de criação de usuário é exibido dentro da página.

O formulário de criação de usuário inclui campos para inserir o nome, email e senha do novo usuário. Após preencher os campos necessários e enviar o formulário, os dados são processados pelo servidor Flask, que realiza a inserção do novo usuário no banco de dados.

![Criação de Usuários](https://drive.google.com/uc?id=1YbCI3gD4-FOvlZGIL8pa_APfI_9GOJDt)

## Botão atualizar 
O botão 'Atualizar' permite ao usuário modificar informações de um usuário específico. Ao clicar neste botão, um formulário é exibido com campos para inserir o novo nome, email e senha do usuário. Depois de preencher esses campos e enviar o formulário, os dados são atualizados no banco de dados.

![Atualização de Usuários](https://drive.google.com/uc?id=1yOjLptjqg1BHcp-aXqXxUihby65b-IZC)



## Botão de deletar usuario
A função de deletar usuários permite remover um usuário existente do sistema. Ao clicar no botão "Deletar" associado a um usuário na lista, o sistema solicitará a confirmação e, em seguida, executará a exclusão do usuário selecionado do banco de dados. 

![Deletar Usuário](https://drive.google.com/uc?id=13iLj9Tk4usdSt5FLcVqbi9VznA83xXCE)
