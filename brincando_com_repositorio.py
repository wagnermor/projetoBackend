import repositorio as rep

#EXPERIMENTE A FUNÇÃO retornar_produtos(), que retornar um dicionário de dicionários com todos os produtos

#print(rep.retornar_produtos())

#EXPERIMENTE A FUNÇÃO retornar_produto(id), que recebe um id e retorna um único dicionário contendo os detalhes do produto

#print(rep.retornar_produto(2))

#EXPERIMENTE A FUNÇÃO remover_produto(id), que recebe um id e remove um produto do dicionário de dicionários

#rep.remover_produto(1)
#print(rep.retornar_produtos())

#EXPERIMENTE A FUNÇÃO atualizar_produto(id, dados_produto), que recebe um id e um dicionário contendo dados do produto para então atualizar o produto no dicionário de dicionários

#alterado = {
#    "nome" : "Pastilha de Freio",
#    "descricao" : "Pastilha de Freio Civic 99/...",
#    "preco" : 198,
#    "imagem" : "Foto.jpg"
#}

#rep.atualizar_produto(2, alterado)
#print(rep.retornar_produtos())

#EXPERIMENTE A FUNÇÃO criar_produto(nome, descricao, preco, imagem), que recebe um nome, uma descricao, um preço e uma imagem e adiciona o produto no dicionário de dicionário com um novo id

#rep.criar_produto(nome="Cilindro roda", descricao="Cilindro de roda traseiro esquerdo gol", preco=68, imagem="fotoCilindro.jpg")
#print(rep.retornar_produtos())

#EXPERIMENTE A FUNÇÃO gerar_id(), que retornar um novo id à partir dos ids já cadastrados no dicionário de dicionários

