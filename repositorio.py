produtos = {
    1: {
        "nome": "Harry Potter",
        "descricao": "Harry Tiago Potter (31 de julho de 1980) é um bruxo inglês mestiço, e um dos mais famosos da atualidade. Ele é o único filho de Tiago e Lílian Potter, ambos membros da Ordem da Fênix original. Seu nascimento foi ofuscado por uma profecia, nomeando ele mesmo ou Neville Longbottom como aquele que possuía o poder de derrotar Lorde Voldemort. Depois da metade da profecia ser relatada para o Lorde das Trevas, em cortesia de Severo Snape, Harry foi escolhido como alvo devido às muitas semelhanças entre ele e Voldemort.",
        "casa": "Grifinória",
        "imagem": "https://p2.trrsf.com/image/fget/cf/1200/1600/middle/images.terra.com/2023/04/14/594335823-harry-potter.jpg"
    },
    2: {
        "nome": "Hermione",
        "descricao": "Hermione Jean Granger, nascida em 19 de setembro de 1979, é uma bruxa inglesa nascida trouxa e a única filha do Sr. e da Sra. Granger. Aos onze anos de idade, quando aprendeu sobre sua natureza mágica, Hermione foi aceita na Escola de Magia e Bruxaria de Hogwarts. Ela iniciou seus estudos em 1991 e foi classificada para a Casa Grifinória. Hermione possuía uma mente acadêmica brilhante e se provou uma estudante talentosa em quase todas as matérias que estudou, a ponto de ser considerada à Casa Corvinal quando classificada pelo Chapéu Seletor. No entanto, sua disposição cética e lógica foi uma das características que o fez mudar de ideia.",
        "casa": "Grifinória",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCvY6FQqSv-KcXHy8dsfDyt23A6DtgcmxDjfEsqSJC&s"
    }
    ,
    3: {
        "nome": "Ron",
        "descricao": "Ronald Abílio[33] Weasley, mais conhecido como Rony, é um bruxo inglês sangue puro[1] nascido em 1 de março de 1980 e o sexto filho de Arthur e Molly Weasley. Ele também é o irmão mais novo de Gui, Carlinhos, Percy, Fred e Jorge e o irmão mais velho de Gina. Rony cresceu junto de seus irmãos n'A Toca, pelos arredores de Ottery St. Catchpole em Devon.",
        "casa": "Grifinória",
        "imagem": "https://i.pinimg.com/originals/18/fe/63/18fe634da34814e7dd1b6dcaa6e93091.jpg"
    },
    4: {
        "nome": "Draco Malfoy",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Excepturi rerum omnis, labore veniam beatae unde quod fuga et ut iure blanditiis vel aut nesciunt consequuntur inventore, quis maxime autem animi?",
        "casa": "Lorem",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/thumb/1/16/Draco_Mal.JPG/220px-Draco_Mal.JPG"
    },
    5: {
        "nome": "Ginevra Weasley",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Excepturi rerum omnis, labore veniam beatae unde quod fuga et ut iure blanditiis vel aut nesciunt consequuntur inventore, quis maxime autem animi?",
        "casa": "Lorem",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU8DmrPxw8bBXSW0h1CSWVqZ4NScdnqRcqwVGd5RCQmj708OY0TUSkVAR-HDk6hd0_3QU"
    },
    6: {
        "nome": "Neville Longbottom",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Excepturi rerum omnis, labore veniam beatae unde quod fuga et ut iure blanditiis vel aut nesciunt consequuntur inventore, quis maxime autem animi?",
        "casa": "Lorem",
        "imagem": "https://i2-prod.mylondon.news/incoming/article22014262.ece/ALTERNATES/s1200e/1_GD14477555.jpg"
    },
    
}


#id generator
def gerar_id():
    id = max(produtos.keys()) + 1
    return id

#create
def criar_produto(nome:str, descricao:str, casa:str, imagem:str):
    produtos[gerar_id()] = {"nome":nome, "descricao":descricao, "casa":casa, "imagem":imagem}


#update
def atualizar_produto(id:int, dados_produto:dict):
    produtos[id] = dados_produto
    
#delete
def remover_produto(id:int):
    if id in produtos.keys():
        del produtos[id]

#read
def retornar_produto(id:int) -> dict: 
    if id in produtos.keys():
        return produtos[id]
    else:
        return {}

def retornar_produtos() -> dict:
    return produtos



