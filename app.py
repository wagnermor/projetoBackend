from flask import Flask, redirect, render_template, request, url_for
import repositorio

app = Flask(__name__)

#LEMBRE-SE -> 
# Ao obter dados do servidor, a máquina do cliente usa um GET
# Ao enviar dados para o servidor, a máquina do cliente usa um POST

#É preciso criar rotas que levem em conta as seguintes funcionalidades:
#Listar todos os personagens no template index.html
@app.route("/")
def exibir_personagens():
    return render_template('index.html', personagens = repositorio.retornar_personagens())
#Abrir um personagem específico (carregando seus dados) no template cadastro.html
@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def exibir_personagem(id):

    if request.method == 'POST':
    #Quer dizer que o usuário quer gravar um dado
        if "excluir" in request.form:
           repositorio.remover_personagem(id)
           return redirect(url_for('exibir_personagens'))
        elif "salvar" in request.form: 
            personagem = {}
            personagem['nome'] = request.form["nome"]
            personagem['descricao'] = request.form["descricao"]
            personagem['casa'] = request.form["casa"]
            personagem['imagem'] = request.form["imagem"]

            if id in repositorio.retornar_personagens().keys():
               repositorio.atualizar_personagem(id, personagem)

            return redirect(url_for('exibir_personagens'))
    else:
    #Retorna os dados de um personagem na página de cadastro
     personagem = repositorio.retornar_personagem(id)
     personagem['id'] = id
    return render_template('cadastro.html', **personagem)

@app.route("/personagem", methods=["GET", "POST"])
def criar_personagem():
   if request.method == "POST":
            personagem = {}
            personagem['nome'] = request.form["nome"]
            personagem['descricao'] = request.form["descricao"]
            personagem['casa'] = request.form["casa"]
            personagem['imagem'] = request.form["imagem"]
            repositorio.criar_personagem(**personagem)
            return redirect(url_for('exibir_personagens'))
   else:
      return render_template('cadastro.html', id=repositorio.gerar_id())
#Abrir o template cadastro.html apenas com o id preenchido para permitir novo cadastro
#Dar função aos botões excluir e salvar no template cadastro.html
    


app.run(debug=True)





