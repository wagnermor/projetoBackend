#Importando o Flask
from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

# Página inicial
@app.route("/")
def home():
    lista_personagens = repositorio.retornar_personagens()
    return render_template("tabela.html", dados=lista_personagens)

@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editar_personagem(id):
    if request.method == "POST":
        if "excluir" in request.form:
            repositorio.remover_personagem(id)
            return redirect(url_for('home'))
        elif "salvar" in request.form:
            id = request.form["id"]
            nome = request.form["nome"]
            descricao = request.form["descricao"]
            casa = request.form["casa"]
            imagem = request.form["imagem"]
        dados_retornados = repositorio.retornar_personagem(id)
        if dados_retornados:
            repositorio.atualizar_personagem(id=id, nome=nome, descricao=descricao, casa=casa, imagem=imagem)
        else:
            repositorio.criar_personagem(nome=nome, descricao=descricao, casa=casa, imagem=imagem)
        return redirect(url_for('home'))
    else:
        id, nome, descricao, casa, imagem = repositorio.retornar_personagem(id)
        return render_template("cadastro.html", id=id, nome=nome, descricao=descricao, casa=casa, imagem=imagem)
    


app.run(debug=True)


