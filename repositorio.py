produtos = {
    1: {
        "nome": "Caixa JBL Pro Sound",
        "descricao": "Potente JBL Original Pro Sound Quatro drivers e dois radiadores de graves JBL oferecem um som simplesmente potente e imersivo, com graves profundos e nitidez nos detalhes. Você vai ser levado pela música onde quer que esteja.",
        "preco": 699.00,
        "imagem": "jbl.jpg"
    },
    2: {
        "nome": "Echo Dot 5a geração",
        "descricao": "SUAS MÚSICAS E CONTEÚDOS FAVORITOS - Reproduza músicas e podcasts do Amazon Music, Apple Music, Spotify, entre outros, ou por Bluetooth em todos os ambientes da sua casa.",
        "preco": 390.00,
        "imagem": "dot.png"
    },
    3: {
        "nome": "Mini Projetor",
        "descricao": "Mini Projetor Portatil 5G Wifi 6 Bluetooth 5.0 Android 11, Projetor 4K 1080P Full HD Suporte 8000 Lumens, Projetor Led Auto de Correcção Trapezóide Horizontal, 180°Girável Projector para Telefónico (US Plug)",
        "preco": 399.00,
        "imagem": "projetor.jpg"
    },
    4: {
        "nome": "Beats Pro",
        "descricao": "Fone de ouvido supra-auricular Beats Pro - Prateado",
        "preco": 2300.00,
        "imagem": "beats.jpg"
    },
    5: {
        "nome": "Relogio Watch 4 Pro",
        "descricao": "2023 nfc relógio inteligente masculino gt4 pro 390*390 tela hd freqüência cardíaca bluetooth chamada ip67 à prova dip67 água smartwatch para huawei xiaomi + caixa",
        "preco": 699.00,
        "imagem": "relogio.jpg"
    },
    6: {
        "nome": "Roteador WDS",
        "descricao": "Roteador, WDS Bridge TP-Link Archer C5400X V1 preto e vermelho 100V/240V",
        "preco": 2600.00,
        "imagem": "roteador.jpg"
    }
}


#id generator
def gerar_id():
    id = max(produtos.keys()) + 1
    return id

#create
def criar_produto(nome:str, descricao:str, preco:float, imagem:str):
    produtos[gerar_id()] = {"nome":nome, "descricao":descricao, "preco":preco, "imagem":imagem}


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



