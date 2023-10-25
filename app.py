from flask import Flask, render_template, request, redirect, url_for
import repositorio as rep


app = Flask(__name__)

#LEMBRE-SE -> 
# Ao obter dados do servidor, a máquina do cliente usa um GET
# Ao enviar dados para o servidor, a máquina do cliente usa um POST

#É preciso criar rotas que levem em conta as seguintes funcionalidades:
#Listar todos os produtos no template index.html

@app.route("/")
def exibir_produtos():
    return render_template('index.html', produtos=rep.retornar_produtos()) 

#Abrir um produto específico (carregando seus dados) no template cadastro.html

@app.route("/produto/<int:id>", methods=["GET"])
def exibir_produto(id):
    if id == 0:
        id = rep.gerar_id()
    produto = rep.retornar_produto(id)
    produto['id'] = id
    return render_template('cadastro.html', **produto)

#Abrir o template cadastro.html apenas com o id preenchido para permitir novo cadastro

@app.route("/produto", methods=["GET"])
def abrir_cadastro():
    return render_template('cadastro.html', id= rep.gerar_id())

#Dar função aos botões excluir e salvar no template cadastro.html

@app.route("/produto/<int:id>", methods=["POST"])
def editar_produto(id):
    if "excluir" in request.form:
        rep.remover_produto(id)
    elif "salvar" in request.form:
        produto = {}
        produto["nome"] = request.form["nome"]
        produto["descricao"] = request.form["descricao"]
        produto["preco"] = request.form["preco"]
        produto["imagem"] = request.form["imagem"]

        produtos = rep.retornar_produtos()

        if id in produtos.keys():
            rep.atualizar_produto(id, produto)
        else:
            rep.criar_produto(**produto)
    return redirect(url_for('exibir_produtos'))        

    


app.run(debug=True)