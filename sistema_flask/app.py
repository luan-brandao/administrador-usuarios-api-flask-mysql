from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import requests

app = Flask(__name__)

# Função para obter conexão com o banco de dados MySQL
def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="luan",
        password="12345678",
        database="banco"
    )
    cursor = db.cursor()
    return db, cursor

# URL da sua API Node.js para o login
LOGIN_API_URL = 'http://localhost:3000/api/login'

# URL da sua API Node.js para o cadastro
CADASTRO_API_URL = 'http://localhost:3000/api/cad'

# URL da sua API para deletar usuários
DELETE_USER_API_URL = "http://localhost:3000/api/"

# URL da sua API para atualizar um usuário
API_URL = "http://localhost:3000/api/up/"

@app.route('/users')
def show_users():
    # Faz a solicitação HTTP para a API Node.js para obter os usuários
    response = requests.get('http://localhost:3000/api/')
    users = response.json()  # Converte a resposta para JSON
    
    # Conecta ao banco de dados MySQL
    db, cursor = get_db_connection()
    
    # Executa uma consulta SQL para obter os usuários do MySQL
    cursor.execute("SELECT id, name, email, password FROM usuarios")
    mysql_users = cursor.fetchall()  # Obtém todos os registros
    
    # Fecha a conexão e o cursor
    cursor.close()
    db.close()
    
    # Renderiza a página HTML com os dados dos usuários
    return render_template('users.html', users=users, mysql_users=mysql_users)

@app.route('/delete_user', methods=['POST'])
def delete_user():
    # Obtém o ID do usuário a ser deletado do formulário enviado
    user_id = request.form['user_id']
    
    # Constrói a URL completa para deletar o usuário
    delete_url = DELETE_USER_API_URL + user_id
    
    # Envia uma solicitação DELETE para a API para deletar o usuário
    response = requests.delete(delete_url)
    
    # Verifica se a exclusão foi bem-sucedida 
    if response.status_code == 200:
        # Redireciona de volta para a página de lista de usuários após a exclusão bem-sucedida
        return redirect(url_for('show_users'))
    else:
        # exibe uma mensagem de erro
        return 'Erro ao deletar usuário'
    

# Rota para deletar um usuário do MySQL
@app.route('/delete_user_mysql', methods=['POST'])
def delete_user_mysql():
    try:
        # Obtém o ID do usuário a ser deletado do formulário enviado
        user_id = request.form['user_id']
        
        # Estabelece uma conexão com o banco de dados
        db, cursor = get_db_connection()

        # Executa a exclusão do usuário no banco de dados MySQL
        delete_query = "DELETE FROM usuarios WHERE id=%s"
        cursor.execute(delete_query, (user_id,))
        
        # Confirma a transação e fecha a conexão com o banco de dados
        db.commit()
        cursor.close()
        db.close()
        # Após a exclusão bem-sucedida
        return '<script>window.location.href = "/users";</script>', 200
    except Exception as e:
        # Se ocorrer um erro, retorna uma mensagem de erro com o código de status 500
        return f'Erro ao deletar usuário do MySQL: {str(e)}', 500




@app.route('/update_user', methods=['POST'])
def update_user():
    # Obtém os dados do formulário de atualização
    user_id = request.form['user_id']
    new_name = request.form['name']
    new_email = request.form['email']
    new_password = request.form['password']
    
    # Constrói os parâmetros para enviar na atualização
    params = {
        'name': new_name,
        'email': new_email,
        'password': new_password
    }

    # Constrói a URL para atualizar o usuário
    url = f"{API_URL}{user_id}"

    # Envia uma solicitação PUT para atualizar o usuário
    response = requests.put(url, json=params)
    
    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Redireciona para a página de lista de usuários após a atualização bem-sucedida
        return redirect(url_for('show_users'))
    else:
        # Exibe uma mensagem de erro se a atualização falhar
        return 'Erro ao atualizar usuário'
    
@app.route('/update_user_mysql', methods=['POST'])
def update_user_mysql():
    try:
        # Obtém os dados do formulário de atualização
        user_id = request.form['user_id']
        new_name = request.form['name']
        new_email = request.form['email']
        new_password = request.form['password']

        db, cursor = get_db_connection()

        update_query = "UPDATE usuarios SET name=%s, email=%s, password=%s WHERE id=%s"
        cursor.execute(update_query, (new_name, new_email, new_password, user_id))

        # Confirma a transação e fecha a conexão com o banco de dados
        db.commit()
        cursor.close()
        db.close()

        # Retorna um código de status 200 
        return '<script>window.location.href = "/users";</script>', 200
    except Exception as e:
        # Se ocorrer um erro, retorna uma mensagem de erro com o código de status 500
        return f'Erro ao atualizar usuário do MySQL: {str(e)}', 500


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtém os dados do formulário
        name = request.form['name']
        password = request.form['password']
        
        # Dados para enviar para a API Node.js
        data = {
            'name': name,
            'password': password
        }
        
        # Envia uma solicitação POST para a API Node.js para fazer login
        response = requests.post(LOGIN_API_URL, json=data)
        
        # Verifica se o login foi bem-sucedido (código de status 200)
        if response.status_code == 200:
            # Redireciona para a página de lista de usuários após o login bem-sucedido
            return redirect(url_for('show_users'))
        else:
            #  se o login falhar
            return  redirect(url_for('cadastro'))
    else:
        #  renderize o template login.html
        return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Obtém os dados do formulário
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Dados para enviar para a API Node.js
        data = {
            'name': name,
            'email': email,
            'password': password
        }
        
        # Envia uma solicitação POST para a rota de cadastro da API Node.js
        response = requests.post(CADASTRO_API_URL, json=data)
        
        # Verifica se o cadastro foi bem-sucedido (código de status 201)
        if response.status_code == 201:
            # Redireciona para a página de login após o cadastro bem-sucedido
            return redirect(url_for('login'))
        else:
            # Exibe uma mensagem de erro se o cadastro falhar
            return 'Erro ao cadastrar usuário.'
    else:
        # Se a requisição for GET, renderize o template cadastro.html
        return render_template('cadastro.html')
    
@app.route('/create_user_mysql', methods=['POST'])
def create_user_mysql():
    try:
        # Obtém os dados do formulário de criação
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Estabelece uma conexão com o banco de dados MySQL
        db, cursor = get_db_connection()

        # Executa a inserção do novo usuário no banco de dados MySQL
        insert_query = "INSERT INTO usuarios (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, email, password))

        db.commit()
        cursor.close()
        db.close()

        # Redireciona de volta para a página de lista de usuários após a criação bem-sucedida
        return redirect(url_for('show_users'))
    except Exception as e:
        # Se ocorrer um erro, retorna uma mensagem de erro
        return f'Erro ao criar usuário no MySQL: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
