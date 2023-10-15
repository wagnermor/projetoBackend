#Criando um dicionário para armazenar dados dos personagens
dicionario = {
    1: {
        "nome": "Harry Potter",
        "raca": "Humano",
        "casa": "Grifinória",
        "cabelo": "preto",
        "olhos": "Azuis",
        "nascimento": "31/07/1990"
    },
    2: {
        "nome": "Ron Wesley",
        "raca": "Humano",
        "casa": "Grifinória",
        "cabelo": "Laranja",
        "olhos": "Verdes",
        "nascimento": "01/03/1980"
    },
    3: {
        "nome": "Hermione",
        "raca": "Humano",
        "casa": "Grifinória",
        "cabelo": "Castanho",
        "olhos": "Castanhos escuros",
        "nascimento": "19/09/1979"
    },
}


#Importando o Flask
from flask import Flask, render_template


app = Flask(__name__)

#criando rotas de acesso aos personagens

@app.route("/harry/<int:personagem_id>")

def mostra_harry(personagem_id ):
    return render_template('harry.html', **dicionario[personagem_id])

@app.route("/ron/<int:personagem_id>")

def mostra_ron(personagem_id):
    return render_template('ron.html', **dicionario[personagem_id])

@app.route("/hermione/<int:personagem_id>")

def mostra_hermione(personagem_id):
    return render_template('hermione.html', **dicionario[personagem_id])


@app.route("/")

def mostra_personagens():
    return render_template('personagens.html', personagens = dicionario)

app.run(debug=True)


