from flask import Flask, redirect, render_template, request, url_for
import repositorio

app = Flask(__name__)

#LEMBRE-SE -> 
# Ao obter dados do servidor, a máquina do cliente usa um GET
# Ao enviar dados para o servidor, a máquina do cliente usa um POST

#É preciso criar rotas que levem em conta as seguintes funcionalidades:
#Listar todos os produtos no template index.html
@app.route("/")
def exibir_produtos():
    return render_template('index.html', produtos = repositorio.retornar_produtos())
#Abrir um produto específico (carregando seus dados) no template cadastro.html
@app.route("/produto/<int:id>", methods=['GET', 'POST'])
def exibir_produto(id):

    if request.method == 'POST':
    #Quer dizer que o usuário quer gravar um dado
        if "excluir" in request.form:
           repositorio.remover_produto(id)
           return redirect(url_for('exibir_produtos'))
        elif "salvar" in request.form: 
            produto = {}
            produto['nome'] = request.form["nome"]
            produto['descricao'] = request.form["descricao"]
            produto['casa'] = request.form["casa"]
            produto['imagem'] = request.form["imagem"]

            if id in repositorio.retornar_produtos().keys():
               repositorio.atualizar_produto(id, produto)

            return redirect(url_for('exibir_produtos'))
    else:
    #Retorna os dados de um personagem na página de cadastro
     produto = repositorio.retornar_produto(id)
     produto['id'] = id
    return render_template('cadastro.html', **produto)

@app.route("/personagem", methods=["GET", "POST"])
def criar_produto():
   if request.method == "POST":
            produto = {}
            produto['nome'] = request.form["nome"]
            produto['descricao'] = request.form["descricao"]
            produto['casa'] = request.form["casa"]
            produto['imagem'] = request.form["imagem"]
            repositorio.criar_produto(**produto)
            return redirect(url_for('exibir_produtos'))
   else:
      return render_template('cadastro.html', id=repositorio.gerar_id())
#Abrir o template cadastro.html apenas com o id preenchido para permitir novo cadastro
#Dar função aos botões excluir e salvar no template cadastro.html
    


app.run(debug=True)





# from flask import Flask, render_template
# import repositorio

# app = Flask(__name__)

# #LEMBRE-SE -> 
# # Ao obter dados do servidor, a máquina do cliente usa um GET
# # Ao enviar dados para o servidor, a máquina do cliente usa um POST

# #É preciso criar rotas que levem em conta as seguintes funcionalidades:
# #Listar todos os produtos no template index.html
# @app.route("/")
# def exibir_produtos():
#     return render_template('index.html', produtos = repositorio.retornar_produtos())
# #Abrir um produto específico (carregando seus dados) no template cadastro.html
# @app.route("/produto/<int:id>")
# def exibir_produto(id):
#     produto = repositorio.retornar_produto(id)
#     produto['id'] = id
#     return render_template('cadastro.html', **produto)
# #Abrir o template cadastro.html apenas com o id preenchido para permitir novo cadastro
# #Dar função aos botões excluir e salvar no template cadastro.html
    


# app.run(debug=True)