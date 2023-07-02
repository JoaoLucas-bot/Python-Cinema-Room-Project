import sqlite3
import os

def create_connection(db_file):
    conn = None
    try:
        if os.path.exists(db_file):
            conn = sqlite3.connect(db_file)
        else:
            return ("error")
    except:
        return "error"
    return conn

def reserva_auto(dados_sala, lugares_blq, lugares_vip, n_reservas):
    n_lugares_juntos = 0
    lista_linhas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

    if n_reservas <= 2:
        #Pesquisa lado esquerdo
        for linha in lista_linhas:
            n_lugares_juntos = 0
            lugares_juntos = []
            for coluna in range(1, 3):
                lugar = linha + str(coluna)
                if dados_sala[1][lugar] == " " and lugar not in lugares_blq and lugar not in lugares_vip:
                    lugares_juntos.append(lugar)
                    n_lugares_juntos += 1
                    if n_lugares_juntos == n_reservas:
                        codigo = 0
                        return [codigo, lugares_juntos]
                else:
                    lugares_juntos = []
                    n_lugares_juntos = 0
        
        #Pesquisa lado direito
        for linha in lista_linhas:
            n_lugares_juntos = 0
            lugares_juntos = []
            for coluna in range(13, 15):
                lugar = linha + str(coluna)
                if dados_sala[1][lugar] == " " and lugar not in lugares_blq and lugar not in lugares_vip:
                    lugares_juntos.append(lugar)
                    n_lugares_juntos += 1
                    if n_lugares_juntos == n_reservas:
                        codigo = 0
                        return [codigo, lugares_juntos]
                else:
                    lugares_juntos = []
                    n_lugares_juntos = 0

    #Pesquisa Central            
    for linha in lista_linhas:
        lugares_juntos = []
        n_lugares_juntos = 0
        for coluna in range(3, 13):
            lugar = linha + str(coluna)
            if dados_sala[1][lugar] == " " and lugar not in lugares_blq and lugar not in lugares_vip:
                lugares_juntos.append(lugar)
                n_lugares_juntos += 1
                if n_lugares_juntos == n_reservas:
                    codigo = 0
                    return [codigo, lugares_juntos]
            else:
                lugares_juntos = []
                n_lugares_juntos = 0

    #Pesquisa Completa
    todos_lugares_disponiveis = []
    for linha in lista_linhas:
        lugares_juntos = []
        n_lugares_juntos = 0
        for coluna in range(1, 15):
            lugar = linha + str(coluna)
            if dados_sala[1][lugar] == " " and lugar not in lugares_blq and lugar not in lugares_vip:
                lugares_juntos.append(lugar)
                todos_lugares_disponiveis.append(lugar)
                n_lugares_juntos += 1
                if n_lugares_juntos == n_reservas:
                    codigo = 0
                    return [codigo, lugares_juntos]
            else:
                lugares_juntos = []
                n_lugares_juntos = 0

    codigo = 1
    if len(todos_lugares_disponiveis) >= n_reservas:
        return [codigo, todos_lugares_disponiveis[0:n_reservas]]
    else:
        return [2]

def reserva(cursor, sessao, cliente, lista_lugares_vip, reservas):
    for reserva in reservas:
        #Query para termos o id_sessao referente à linha do espetaculo/sessao
        query_idsessao = 'SELECT receita FROM sessoes WHERE id_sessao = ?'
        params = (sessao[3],)
        result_idsessao = cursor.execute(query_idsessao, params).fetchall()
        if reserva in lista_lugares_vip:
            receita = result_idsessao[0][0] + 12
        else:
            receita = result_idsessao[0][0] + 4

        #Registo da nova reserva na BD
        db_update = ['INSERT INTO realizacao_espetaculos (id_lugar, id_sessao, lugar_ocupado, nome_espetador) VALUES (?,?,?,?)']
        params = [(reserva, sessao[3], 'S', cliente)]
        db_update.append('UPDATE sessoes SET receita = ? WHERE id_sessao = ?')
        params.append((receita, sessao[3]))
        for i in range(len(db_update)):
            cursor.execute(db_update[i], params[i])

