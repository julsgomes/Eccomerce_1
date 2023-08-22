from bd import mysql
from models.user import Usuario
from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

user_global = Usuario()
email_global = ""

#instanciar
@app.route('/')                                                     #Criando o Rout
def homepage():                                                     #Criando a Função
    return render_template("login.html")

@app.route('/Login')                                                #Criando o Rout
def Login():                                                #Criando a Função
    return render_template("login.html")

@app.route('/Create')                                               #Criando o Rout
def Register():                                             #Criando a Função
    return render_template("create.html")


#Funções
@app.route('/Adicionar', methods=['POST', 'GET'])
def adicionar_usuario():

    if request.method=='POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        senha = request.form['password']


        if(nome and cpf and email and senha):
            with mysql.cursor() as cur:
                cur.execute('INSERT INTO Usuario (nome, email, senha, cpf) VALUES (%s,%s,%s,%s)', (nome, email, senha, cpf))
                cur.connection.commit()
                
                return render_template("login.html")
        else:
            return render_template("create.html")

    return render_template("create.html")

@app.route('/verificar', methods=['POST', 'GET'])
def verificar_usuario():

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        try:
            with mysql.cursor() as cur:
                comando = "SELECT email, nome, senha FROM Usuario WHERE	email = %s;"
                cur.execute(comando, email)
                resultado = cur.fetchall()
                if(resultado[0][0] != None):
                    if(resultado[0][2] != senha):
                        return render_template("login.html")
                    else:
                        email_global = resultado[0][1]
                        return render_template("index.html")

        except Exception as e:
            return render_template("login.html")

@app.route('/getUserByEmail', methods = ['GET'])
def getUserByEmail():
    args = request.args.get('email')
    try:
        with mysql.cursor() as cur:
            comando = "SELECT * FROM Usuario WHERE	email = %s;"
            cur.execute(comando, args)
            resultado = cur.fetchall()
            user_global.cria(resultado[0][0], resultado[0][1], resultado[0][2], resultado[0][3])
            return 

    except Exception as e:
        print("Deu ruim")
        return render_template("login.html")

if(__name__ == "__main__"):
    app.run(debug = True)