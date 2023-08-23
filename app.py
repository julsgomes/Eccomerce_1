from bd import mysql
from flaskext.mysql import MySQL
from flask import Flask, jsonify, render_template, request, redirect, url_for

<<<<<<< HEAD
app = Flask(__name__, static_url_path='/assets', static_folder='assets')   

#instanciar
@app.route('/')                                                     
def homepage():                                                     
    return render_template("login.html")

@app.route('/Login')                                                
def Login():                                                        
    return render_template("login.html")

@app.route('/Create')                                               
def Register():                                                     
=======
app = Flask(__name__, static_url_path='/assets', static_folder='assets')
nome_usuario = ''

#instanciar
@app.route('/')                                                     #Criando o Rout
def homepage():                                                     #Criando a Função
    return render_template("login.html")

@app.route('/Login')                                                #Criando o Rout
def Login():                                                #Criando a Função
    return render_template("login.html")

@app.route('/Create')                                               #Criando o Rout
def Register():                                             #Criando a Função
>>>>>>> 959edd8bb8c6df61e918163d0b0ec24b6905a752
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
<<<<<<< HEAD
                mysql.commit()
=======
                
>>>>>>> 959edd8bb8c6df61e918163d0b0ec24b6905a752
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
<<<<<<< HEAD
                        return render_template("index.html", email_usuario=resultado[0][0])

        except Exception as e:
            return render_template("login.html")
        
       
@app.route("/InsereAvaliacao", methods = ["POST"])
def insere_avaliacao():
    comentario = request.form['comentario']
    nomeProduto = request.form['nomeProduto']
    email = request.form['emailUsuario']
    
    try:
        with mysql.cursor() as cur:
            comando = "Select cpf from Usuario where email = %s"
            cur.execute(comando, email)
            resultado = cur.fetchall()
            comando  = "Select idProduto from Produto where url = 'assetsImagesProdutos%s.png';" % nomeProduto
            cur.execute(comando)
            id_produto = cur.fetchall()
            cur.execute(f"INSERT INTO Avaliacao (id, comentario, cpfCliente, idProduto) VALUES (1, '{comentario}', '{resultado[0][0]}', {id_produto[0][0]})")
            mysql.commit()
            return render_template("index.html")
               
    except Exception as e:
        return render_template("index.html")
    
@app.route("/CarregaAvaliacoes", methods = ["GET"])
def CarregaAvaliacoes():
    try:
        with mysql.cursor() as cur: 
            comando = "Select * From Avaliacao"
            cur.execute(comando)
            resultado = cur.fetchall()
            return jsonify(resultado)
        
    except Exception as e:
        return render_template("index.html")
    

@app.route("/AdicionaCarrinho", methods = ["POST"])
def AdicionaCarrinho():
    
    idProduto = request.form.get('id')
    email_usuario = request.form.get('emailUsuario')
    try:
        print(idProduto, email_usuario)
        with mysql.cursor() as cur: 
            comando = "Insert into CarrinhoDeCompra(emailUsuario, id) VALUES (%s, %s)"
            cur.execute(comando, email_usuario, 3)
            mysql.commit()         
            # comando = "Insert into Relaciomento_Pedido_Carrinho VALUES (%s, %s)"
            # cur.execute(comando, idProduto, email_usuario)
            # mysql.commit()
            return None
        
    except Exception as e:
        return render_template("index.html")
    

@app.route("/CarregaCarrinho", methods = ["GET"])
def carrega_itens_carrinho():
    nome_usuario = request.form('nomeUsuario')
    try:
        with mysql.cursor() as cur:
            comando = "Select email from Usuario where nome = %s"
            cur.execute(comando, nome_usuario)
            email = cur.fetchall()
            
            comando = "Select * from Produtos P, Relaciomento_Pedido_Carrinho R where p.id = r.id and r.emailUsuario = %s"
            cur.execute(comando, email[0][0])
            resultado = cur.fetchall
            return resultado
        
    except Exception as e:
        return render_template("index.html")
=======
                        nome_usuario = resultado[0][1]
                        return render_template("index.html", nome_usuario = nome_usuario)

        except Exception as e:
            return render_template("login.html")
>>>>>>> 959edd8bb8c6df61e918163d0b0ec24b6905a752


if(__name__ == "__main__"):
    app.run(debug = True)