import sqlite3

def gerar_id():
    conn = sqlite3.connect("personagens.db")
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='personagens'")
    proximo_id = cursor.fetchone()[0]
    return proximo_id + 1

def criar_personagem(nome, descricao, casa, imagem):
    try:
        conn = sqlite3.connect("personagens.db")
        cursor = conn.cursor()
        sql_insert = "INSERT INTO personagens (nome, descricao, casa, imagem) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_insert, (nome, descricao, casa, imagem))
        id = cursor.lastrowid
        conn.commit()
        conn.close()
        return id
    except Exception as ex:
        print(ex)
        return 0
    
def atualizar_personagem(id:int, nome, descricao, casa, imagem):
    try:
        conn = sqlite3.connect("personagens.db")
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET nome = ?, descricao = ?, casa = ?, imagem = ? WHERE id = ?"
        cursor.execute(sql_update, (nome, descricao, casa, imagem, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
    
def remover_personagem(id: int):
    try:
        conn = sqlite3.connect("personagens.db")
        cursor = conn.cursor()
        sql_delete = "DELETE FROM personagens WHERE id = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

def retornar_personagem(id:int):
    try:
        # adicionar
        if id == 0: 
            return gerar_id(), "", "", "", ""
        # editar
        conn = sqlite3.connect("personagens.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM personagens WHERE id = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, descricao, casa, imagem = cursor.fetchone()
        conn.close()
        return id, nome, descricao, casa, imagem
    except:
        return False
    
def retornar_personagens():
    try:
        conn = sqlite3.connect("personagens.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personagens")
        personagens = cursor.fetchall()
        conn.close()
        return personagens
    except:
        return False
    