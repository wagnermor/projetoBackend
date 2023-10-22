personagens = {
    1: {
        "nome": "Harry Potter",
        "descricao": "Harry Tiago Potter (31 de julho de 1980) é um bruxo inglês mestiço, e um dos mais famosos da atualidade. Ele é o único filho de Tiago e Lílian Potter, ambos membros da Ordem da Fênix original. Seu nascimento foi ofuscado por uma profecia, nomeando ele mesmo ou Neville Longbottom como aquele que possuía o poder de derrotar Lorde Voldemort. Depois da metade da profecia ser relatada para o Lorde das Trevas, em cortesia de Severo Snape, Harry foi escolhido como alvo devido às muitas semelhanças entre ele e Voldemort.",
        "casa": "Grifinória",
        "imagem": "https://gifs.eco.br/wp-content/uploads/2023/08/imagens-do-harry-potter-png-0.png"
    },
    2: {
        "nome": "Hermione",
        "descricao": "Hermione Jean Granger, nascida em 19 de setembro de 1979, é uma bruxa inglesa nascida trouxa e a única filha do Sr. e da Sra. Granger. Aos onze anos de idade, quando aprendeu sobre sua natureza mágica, Hermione foi aceita na Escola de Magia e Bruxaria de Hogwarts. Ela iniciou seus estudos em 1991 e foi classificada para a Casa Grifinória. Hermione possuía uma mente acadêmica brilhante e se provou uma estudante talentosa em quase todas as matérias que estudou, a ponto de ser considerada à Casa Corvinal quando classificada pelo Chapéu Seletor. No entanto, sua disposição cética e lógica foi uma das características que o fez mudar de ideia.",
        "casa": "Grifinória",
        "imagem": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/be769842-4769-47ac-aea0-dec66652d6e1/d4pcqbp-01e56094-029a-446a-93d8-1be1db69ec24.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2JlNzY5ODQyLTQ3NjktNDdhYy1hZWEwLWRlYzY2NjUyZDZlMVwvZDRwY3FicC0wMWU1NjA5NC0wMjlhLTQ0NmEtOTNkOC0xYmUxZGI2OWVjMjQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.X24W0m5JuJQiUiFouyLeiZb-k6DpeOTvnj-qaVVNlrI"
    },
    3: {
        "nome": "Voldemort",
        "descricao": "Tom Servolo Riddle (31 de dezembro de 1926 - 2 de maio de 1998), mais tarde (e mais) conhecido como Lorde Voldemort, foi um bruxo mestiço considerado o mais poderoso bruxo das trevas de todos os tempos. Ele era filho do rico trouxa Tom Riddle e da bruxa Mérope Gaunt, que morreu pouco após o parto. Tom Riddle pai deixou sua esposa logo depois que ela ficou grávida de seu filho, tendo sido liberado do encantamento de uma poção do amor com a qual tinham iniciado a sua relação. Tom Servolo Riddle nasceu e cresceu em um orfanato trouxa. Mais tarde ingressou na Escola de Magia e Bruxaria de Hogwarts e foi selecionado para a casa Sonserina.",
        "casa": "Sonserina",
        "imagem": "https://4.bp.blogspot.com/-Lmked0j6A60/V1a3TmI-wcI/AAAAAAAAGes/vlIQWMv22RAjVS2dAiFITmUkGJCJ5az_wCLcB/s1600/Harry%2BPotter%2BLord%2BVoldemort%25C2%25B2.png"
    },
}


#id generator
def gerar_id():
    id = max(personagens.keys()) + 1
    return id

#create
def criar_personagem(nome:str, descricao:str, casa:str, imagem:str):
    personagens[gerar_id()] = {"nome":nome, "descricao":descricao, "casa":casa, "imagem":imagem}


#update
def atualizar_personagem(id:int, dados_personagem:dict):
    personagens[id] = dados_personagem
    
#delete
def remover_personagem(id:int):
    if id in personagens.keys():
        del personagens[id]

#read
def retornar_personagem(id:int) -> dict: 
    if id in personagens.keys():
        return personagens[id]
    else:
        return {}

def retornar_personagens() -> dict:
    return personagens



