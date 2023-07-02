import os
import time
import datetime
import controllers.controller as ctl

def mostrar_sala(cursor, sessao):
    query_ocup = []
    lista_linhas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    lista_colunas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    lista_todos_lugares = []
    dict_ocup = {}
    dict_ocup_retr = {}

    #Query para termos os lugares referentes ao espetaculo/sessao, que já se encontram registados na BD
    query = f'SELECT realizacao_espetaculos.id_lugar FROM realizacao_espetaculos INNER JOIN sessoes ON realizacao_espetaculos.id_sessao = sessoes.id_sessao WHERE sessoes.id_sessao = ?'
    params = (sessao[3],)
    result = cursor.execute(query, params).fetchall()
    
    #Apenas queremos index 0 (id_sala) dos tuplos retornados pela query
    for i in result:
        query_ocup.append(i[0])

    #Juntar strings dos for's que formam um id de lugar e marcar cada um como ocupado ou livre
    #conforme info retornada pela query
    for line in lista_linhas:
        for column in lista_colunas:
            lugar = line + column
            lista_todos_lugares.append(lugar)
            if lugar in query_ocup:
                dict_ocup_retr[lugar] = "X"
                dict_ocup[lugar] = "\033[1;31m" "X" "\033[0;0m"
            else:
                dict_ocup_retr[lugar] = ' '
                dict_ocup[lugar] = ' '

    #Apresentar sala com dados da query
    print("     1   2          3    4    5    6    7    8    9    10   11  12        13   14")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"K  |_{dict_ocup['K1']}_||_{dict_ocup['K2']}_|     |_{dict_ocup['K3']}_||_{dict_ocup['K4']}_||_{dict_ocup['K5']}_||_{dict_ocup['K6']}_||_{dict_ocup['K7']}_||_{dict_ocup['K8']}_||_{dict_ocup['K9']}_||_{dict_ocup['K10']}_||_{dict_ocup['K11']}_||_{dict_ocup['K12']}_|     |_{dict_ocup['K13']}_||_{dict_ocup['K14']}_|")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"J  |_{dict_ocup['J1']}_||_{dict_ocup['J2']}_|     |_{dict_ocup['J3']}_||_{dict_ocup['J4']}_||_{dict_ocup['J5']}_||_{dict_ocup['J6']}_||_{dict_ocup['J7']}_||_{dict_ocup['J8']}_||_{dict_ocup['J9']}_||_{dict_ocup['J10']}_||_{dict_ocup['J11']}_||_{dict_ocup['J12']}_|     |_{dict_ocup['J13']}_||_{dict_ocup['J14']}_|")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"I  |_{dict_ocup['I1']}_||_{dict_ocup['I2']}_|     |_{dict_ocup['I3']}_||_{dict_ocup['I4']}_||_{dict_ocup['I5']}_||_{dict_ocup['I6']}_||_{dict_ocup['I7']}_||_{dict_ocup['I8']}_||_{dict_ocup['I9']}_||_{dict_ocup['I10']}_||_{dict_ocup['I11']}_||_{dict_ocup['I12']}_|     |_{dict_ocup['I13']}_||_{dict_ocup['I14']}_|")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"H  |_{dict_ocup['H1']}_||_{dict_ocup['H2']}_|     |_{dict_ocup['H3']}_||_{dict_ocup['H4']}_||_{dict_ocup['H5']}_||_{dict_ocup['H6']}_||_{dict_ocup['H7']}_||_{dict_ocup['H8']}_||_{dict_ocup['H9']}_||_{dict_ocup['H10']}_||_{dict_ocup['H11']}_||_{dict_ocup['H12']}_|     |_{dict_ocup['H13']}_||_{dict_ocup['H14']}_|")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"G  |_{dict_ocup['G1']}_||_{dict_ocup['G2']}_|     |_{dict_ocup['G3']}_||_{dict_ocup['G4']}_||_{dict_ocup['G5']}_||_{dict_ocup['G6']}_||_{dict_ocup['G7']}_||_{dict_ocup['G8']}_||_{dict_ocup['G9']}_||_{dict_ocup['G10']}_||_{dict_ocup['G11']}_||_{dict_ocup['G12']}_|     |_{dict_ocup['G13']}_||_{dict_ocup['G14']}_|")
    print("    ___  ___                      ___  ___  ___  ___                      ___  ___")
    print(f"F  |_{dict_ocup['F1']}_||_{dict_ocup['F2']}_|                \VIP|_{dict_ocup['F6']}_||_{dict_ocup['F7']}_||_{dict_ocup['F8']}_||_{dict_ocup['F9']}_|VIP/                |_{dict_ocup['F13']}_||_{dict_ocup['F14']}_|")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"E  |_{dict_ocup['E1']}_||_{dict_ocup['E2']}_|     |_{dict_ocup['E3']}_||_{dict_ocup['E4']}_||_{dict_ocup['E5']}_||_{dict_ocup['E6']}_||_{dict_ocup['E7']}_||_{dict_ocup['E8']}_||_{dict_ocup['E9']}_||_{dict_ocup['E10']}_||_{dict_ocup['E11']}_||_{dict_ocup['E12']}_|     |_{dict_ocup['E13']}_||_{dict_ocup['E14']}_|")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"D  |_{dict_ocup['D1']}_||_{dict_ocup['D2']}_|     |_{dict_ocup['D3']}_||_{dict_ocup['D4']}_||_{dict_ocup['D5']}_||_{dict_ocup['D6']}_||_{dict_ocup['D7']}_||_{dict_ocup['D8']}_||_{dict_ocup['D9']}_||_{dict_ocup['D10']}_||_{dict_ocup['D11']}_||_{dict_ocup['D12']}_|     |_{dict_ocup['D13']}_||_{dict_ocup['D14']}_|")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"C  |_{dict_ocup['C1']}_||_{dict_ocup['C2']}_|     |_{dict_ocup['C3']}_||_{dict_ocup['C4']}_||_{dict_ocup['C5']}_||_{dict_ocup['C6']}_||_{dict_ocup['C7']}_||_{dict_ocup['C8']}_||_{dict_ocup['C9']}_||_{dict_ocup['C10']}_||_{dict_ocup['C11']}_||_{dict_ocup['C12']}_|     |_{dict_ocup['C13']}_||_{dict_ocup['C14']}_|")
    print("    ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"B  |_{dict_ocup['B1']}_||_{dict_ocup['B2']}_|     |_{dict_ocup['B3']}_||_{dict_ocup['B4']}_||_{dict_ocup['B5']}_||_{dict_ocup['B6']}_||_{dict_ocup['B7']}_||_{dict_ocup['B8']}_||_{dict_ocup['B9']}_||_{dict_ocup['B10']}_||_{dict_ocup['B11']}_||_{dict_ocup['B12']}_|     |_{dict_ocup['B13']}_||_{dict_ocup['B14']}_|")
    print("    ___  ___                      ___  ___  ___  ___                      ___  ___")
    print(f"A  |_{dict_ocup['A1']}_||_{dict_ocup['A2']}_|                \VIP|_{dict_ocup['A6']}_||_{dict_ocup['A7']}_||_{dict_ocup['A8']}_||_{dict_ocup['A9']}_|VIP/                |_{dict_ocup['A13']}_||_{dict_ocup['A14']}_|")
    
    print("         ___________________________________________________________________")
    print("        |                                                                   |")
    print("        |                               PALCO                               |")
    print("        |___________________________________________________________________|")

    return [lista_todos_lugares, dict_ocup_retr]

#Apresentar sessões para o espetaculo selecionado na função 'em exibição'
def apresentar_sessoes(cursor, id_espetaculo):
    hora_sessao = ["21h00", "22h00", "23h00"]
    count = 1
    info_sessoes = []

    query_sessoes = f'SELECT sessao, data, id_sessao FROM sessoes WHERE id_espetaculo = {id_espetaculo};'
    result_sessoes = cursor.execute(query_sessoes).fetchall()

    for i in result_sessoes:
        print(f"{count} - {i[1]} às {hora_sessao[i[0]-1]}")
        info_sessoes.append((count, i[0], i[1], i[2]))
        count += 1
    
    return info_sessoes

#Apresentar lista de espetaculos registados na DB
def apresentar_espetaculos(cursor):
    count = 0
    
    query = 'SELECT id_espetaculo, nome FROM espetaculos;'
    query_espetaculos = cursor.execute(query).fetchall()
    
    for show_name in query_espetaculos:
        count += 1
        print(f"{show_name[0]} - {show_name[1]}")
    
    return query_espetaculos

#Eliminar uma reserva
def eliminar_reserva(db, cursor, sessao, id_espetaculo, nome_espetaculo, prox_menu):
    lista_lugares_blq = ['A3','A4','A5','A10','A11','A12','F3','F4','F5','F10','F11','F12']
    lista_lugares_vip = ['A6','A7','A8','A9','F6','F7','F8','F9']
    hora_sessao = ["21h00", "22h00", "23h00"]
    loop_check = 1

    #Rodar até o user indicar um lugar como deve ser
    while loop_check == 1:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("---Eliminar Reserva---")
        print("")
        print(f"{nome_espetaculo}, Sessão de dia {sessao[2]} às {hora_sessao[sessao[1]-1]} ")
        print("")

        #Printar a sala
        dados_sala = mostrar_sala(cursor, sessao)

        print("")
        print("0 - Voltar ao menu anterior.")
        print("")
        reserva = input('Indique o lugar reservado a cancelar: ')
        if reserva == "0":
            prox_menu[0] = "3_sessao"
            loop_check = 0
        elif reserva not in dados_sala[0] or reserva in lista_lugares_blq: #Lugar não reconhecido ou bloqueado?
            input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
        elif dados_sala[1][reserva] == ' ': #Lugar não ocupado?
            input("\033[1;31m" + "O lugar selecionado não se encontra reservado." + "\033[0;0m")
        else:   
            query_info_reserva = f"""SELECT realizacao_espetaculos.id_realizacao_esp, realizacao_espetaculos.nome_espetador, sessoes.id_sessao, sessoes.receita
                                    FROM realizacao_espetaculos 
                                    INNER JOIN sessoes 
                                    ON realizacao_espetaculos.id_sessao = sessoes.id_sessao 
                                    WHERE realizacao_espetaculos.id_sessao = ? AND realizacao_espetaculos.id_lugar = ?"""
            params = (sessao[3], reserva)
            result_info_reserva = cursor.execute(query_info_reserva, params).fetchall()


            print(f"O lugar {reserva} encontra-se reservado pelo cliente {result_info_reserva[0][1]}")
            confirmar_elim = input("Pretende eliminar esta reserva? (S/N): ")
            if confirmar_elim.lower() == "n" :
                pass
            elif confirmar_elim.lower() == "s":
                loop_check = 0
                prox_menu[0] = "main"

                if reserva in lista_lugares_vip:
                    receita_del = result_info_reserva[0][3] - 12

                else:
                    receita_del = result_info_reserva[0][3] - 4

                db_update = ['DELETE FROM realizacao_espetaculos WHERE id_realizacao_esp = ?']
                params = [(result_info_reserva[0][0],)]
                db_update.append('UPDATE sessoes SET receita = ? WHERE id_sessao = ?')
                params.append((receita_del, result_info_reserva[0][2]))

                for i in range(len(db_update)):
                    cursor.execute(db_update[i], params[i])
                    db.commit()

                input("\033[1;32m" + "Reserva eliminada com sucesso." + "\033[0;0m")
    return 

# Menu Contabilidade Diaria
def contabilidade(cursor, prox_menu):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---Contabilidade---")
    print("")
    print("0 - Voltar ao menu anterior.")
    print("")
    data_inicial = input("Indique a data inicial (aaaa-mm-dd): ")
    if data_inicial == "0":
        prox_menu[0] = "main"
        return

    data_final = input("Indique a data final (aaaa-mm-dd): ")
    if data_final == "0":
        prox_menu[0] = "main"
        return

    try: 
        data_inicial_formatada = time.strptime(data_inicial, "%Y-%m-%d")
        data_final_formatada = time.strptime(data_final, "%Y-%m-%d")
    except:
        input("\033[1;31m" + "As datas inseridas são inválidas." + "\033[0;0m")
    else:
        if (data_inicial_formatada > data_final_formatada):
            input("\033[1;31m" + "Data final superior à data inicial." + "\033[0;0m")
        else:

            query_cont = """SELECT SUM(receita) 
                            FROM sessoes 
                            WHERE data BETWEEN ? AND ?"""
            params = (data_inicial, data_final)
            result_query_cont = cursor.execute(query_cont, params).fetchall()

            if result_query_cont[0][0] == None:
                input("\033[1;31m" + "Não foram encontradas sessões nas datas indicadas." + "\033[0;0m")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                input(f"Valor total da bilheteira entre {data_inicial} e {data_final}: {result_query_cont[0][0]}€")

            prox_menu[0] = "main"

            return

#Alterar lugar reservado para outro
def alterar_reserva(db, cursor, sessao, id_espetaculo, nome_espetaculo, prox_menu):
    lista_lugares_blq = ['A3','A4','A5','A10','A11','A12','F3','F4','F5','F10','F11','F12']
    lista_lugares_vip = ['A6','A7','A8','A9','F6','F7','F8','F9']
    hora_sessao = ["21h00", "22h00", "23h00"]
    loop_check = 1

    #Rodar até o user indicar um lugar como deve ser
    while loop_check == 1:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("---Alterar Reserva---")
        print("")
        print(f"{nome_espetaculo}, Sessão de dia {sessao[2]} às {hora_sessao[sessao[1]-1]} ")
        print("")

        #Printar a sala
        dados_sala = mostrar_sala(cursor, sessao)

        print("")
        print("0 - Voltar ao menu anterior.")
        print("")
        reserva = input('Indique o lugar reservado a alterar: ')
        if reserva == "0":
            prox_menu[0] = "2_sessao"
            loop_check = 0
        elif reserva not in dados_sala[0] or reserva in lista_lugares_blq: #Lugar não reconhecido ou bloqueado?
            input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
        elif dados_sala[1][reserva] == ' ': #Lugar não ocupado?
            input("\033[1;31m" + "O lugar indicado não se encontra reservado." + "\033[0;0m")

        else:   
            query_info_reserva = f"""SELECT realizacao_espetaculos.id_realizacao_esp, realizacao_espetaculos.nome_espetador, sessoes.id_sessao, sessoes.receita
                                    FROM realizacao_espetaculos 
                                    INNER JOIN sessoes 
                                    ON realizacao_espetaculos.id_sessao = sessoes.id_sessao 
                                    WHERE realizacao_espetaculos.id_sessao = ? AND realizacao_espetaculos.id_lugar = ?"""
            params = (sessao[3], reserva)
            result_info_reserva = cursor.execute(query_info_reserva, params).fetchall()

            print(f"O lugar {reserva} encontra-se reservado pelo cliente {result_info_reserva[0][1]}")
            novo_lugar = input("Indique o novo lugar a reservar: ")
            if novo_lugar not in dados_sala[0] or novo_lugar in lista_lugares_blq:
                input("\033[1;31m" + "O lugar indicado não é válido." + "\033[0;0m")
            elif dados_sala[1][novo_lugar] == 'X':
                input("\033[1;31m" + "O novo lugar já se encontra ocupado." + "\033[0;0m")
            else:
                loop_check = 0
                prox_menu[0] = "main"

                if novo_lugar in lista_lugares_vip and reserva not in lista_lugares_vip:
                    receita_alt = result_info_reserva[0][3] + 8
                    db_update = ['UPDATE realizacao_espetaculos SET id_lugar = ? WHERE id_realizacao_esp = ?', 'UPDATE sessoes SET receita = ? WHERE id_sessao = ?']
                    params = [(novo_lugar, result_info_reserva[0][0]), (receita_alt, result_info_reserva[0][2])]

                    for i in range(len(db_update)):
                        cursor.execute(db_update[i], params[i])
                        db.commit()

                elif novo_lugar not in lista_lugares_vip and reserva in lista_lugares_vip:
                    receita_alt = result_info_reserva[0][3] - 8
                    db_update = ['UPDATE realizacao_espetaculos SET id_lugar = ? WHERE id_realizacao_esp = ?']
                    params = [(novo_lugar, result_info_reserva[0][0])]
                    db_update.append('UPDATE sessoes SET receita = ? WHERE id_sessao = ?')
                    params.append((receita_alt, result_info_reserva[0][2]))

                    for i in range(len(db_update)):
                        cursor.execute(db_update[i], params[i])
                        db.commit()

                db_update = 'UPDATE realizacao_espetaculos SET id_lugar = ? WHERE id_realizacao_esp = ?'
                params = (novo_lugar, result_info_reserva[0][0])

                cursor.execute(db_update, params)
                db.commit()

                input("\033[1;32m" + "Reserva alterada com sucesso." + "\033[0;0m")
    return 

#Menu de reserva de lugar
def reserva_lugares(db, cursor, sessao, id_espetaculo, nome_espetaculo, prox_menu):
    lista_lugares_blq = ['A3','A4','A5','A10','A11','A12','F3','F4','F5','F10','F11','F12']
    lista_lugares_vip = ['A6','A7','A8','A9','F6','F7','F8','F9']
    hora_sessao = ["21h00", "22h00", "23h00"]
    loop_check = 1

    #Rodar até o user indicar um lugar como deve ser
    while loop_check == 1:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("---Reserva de Lugares---")
        print("")
        print(f"{nome_espetaculo}, Sessão de dia {sessao[2]} às {hora_sessao[sessao[1]-1]} ")
        print("")

        #Printar a sala
        dados_sala = mostrar_sala(cursor, sessao)

        print("")
        print("0 - Voltar ao menu anterior.")
        print("")

        opcao_reserva = input("Reserva automática (S/N)? ")
        
        if opcao_reserva == "0":
            prox_menu[0] = "sessao"
            loop_check = 0

        elif opcao_reserva.lower() == "s":
            try:
                n_reservas = int(input("Indique o número de reservas a efetuar: "))
                if n_reservas == 0:
                    prox_menu[0] = "sessao"
                    loop_check = 0
                else:
                    reservas = ctl.reserva_auto(dados_sala, lista_lugares_blq, lista_lugares_vip, n_reservas)
                    
                    if reservas[0] == 0:
                        print(f"Lugares a reservar: {', '.join(reservas[1])}")
                        cliente = input('Insira o numero de telefone do cliente: ')
                        int(cliente)
                        if (cliente[0] != "2" or cliente[0] != "9") and len(cliente) != 9:
                            raise ValueError
                        else:
                            ctl.reserva(cursor, sessao, cliente, lista_lugares_vip, reservas[1])
                            db.commit()
                            loop_check = 0
                            input("\033[1;32m" + "Lugares reservados com sucesso." + "\033[0;0m")
                            prox_menu[0] = "main"
                    elif reservas[0] == 1:
                        print("\033[93m" + "Encontrados lugares suficiente mas separados." + "\033[0;0m")
                        print(f"Lugares a reservar: {', '.join(reservas[1])}")

                        cliente = input('Insira o numero de telefone do cliente: ')
                        int(cliente)
                        if (cliente[0] != "2" or cliente[0] != "9") and len(cliente) != 9:
                            raise ValueError
                        else:
                            ctl.reserva(cursor, sessao, cliente, lista_lugares_vip, reservas[1])
                            db.commit()
                            loop_check = 0
                            input("\033[1;32m" + "Lugares reservados com sucesso." + "\033[0;0m")
                            prox_menu[0] = "main"
                    elif reservas[0] == 2:
                        input("\033[1;31m" + "Sem lugares suficientes para satisfazer o pedido." + "\033[0;0m")
            except:
                input("\033[1;31m" + "O número de telefone inserido é inválido." + "\033[0;0m")
        elif opcao_reserva.lower() == "n":
            reservas = input('Indique os lugares a reservar (separados por virgulas): ').split(",") 
            if reservas[0] == "0":
                prox_menu[0] = "sessao"
                loop_check = 0
            else:
                iniciar_reserva = 0
                for reserva in reservas:
                    if reserva not in dados_sala[0] or reserva in lista_lugares_blq: #Lugar não reconhecido ou bloqueado?
                        input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
                        iniciar_reserva = 1
                        break
                    elif dados_sala[1][reserva] == 'X': #Lugar ocupado?
                        input("\033[1;31m" + "Não foi possivel reservar o lugar porque o mesmo já se encontra ocupado." + "\033[0;0m")
                        iniciar_reserva = 1
                        break
                if iniciar_reserva == 0:
                    try:
                        cliente = input('Insira o numero de telefone do cliente: ')
                        int(cliente)
                        if not (cliente[0] == "2" or cliente[0] == "9") and not len(cliente) == 9:
                            raise Exception
                    except:
                        input("\033[1;31m" + "O número de telefone inserido é inválido." + "\033[0;0m")
                    else:
                        ctl.reserva(cursor, sessao, cliente, lista_lugares_vip, reservas)
                        db.commit()
                        loop_check = 0
                        input("\033[1;32m" + "Lugar(es) reservado(s) com sucesso." + "\033[0;0m")
                        prox_menu[0] = "main"

#Menu de sessões disponiveis
def selecao_sessoes(cursor, id_espetaculo, nome_espetaculo, prox_menu):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"---Sessões para o espetáculo {nome_espetaculo}---")
    print("")

    esp_sessoes = apresentar_sessoes(cursor, id_espetaculo)

    print("0 - Voltar ao menu anterior.")
    print("")

    try:
        opcao_sessao = int(input("Indique uma das opções: "))
    except:
        input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
        return

    if opcao_sessao == 0:
        if prox_menu[0] == "sessao":
            prox_menu[0] = "exibicao"
        elif prox_menu[0] == "2_sessao":
            prox_menu[0] = "2_exibicao"
        elif prox_menu[0] == "3_sessao":
            prox_menu[0] = "3_exibicao"
        return
    elif opcao_sessao not in range(1,len(esp_sessoes)+1) :
        input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
    else:
        if prox_menu[0] == "sessao":
            prox_menu[0] = "reserva"
        elif prox_menu[0] == "2_sessao":
            prox_menu[0] = "alterar"
        elif prox_menu[0] == "3_sessao":
            prox_menu[0] = "eliminar"
        print(esp_sessoes[int(opcao_sessao)-1])
        return esp_sessoes[int(opcao_sessao)-1]

#Menu de espetaculos em exibição
def em_exibicao(cursor, prox_menu):
    os.system('cls' if os.name == 'nt' else 'clear')
    opcao = -1
    
    print("---Em Exibição---")
    print("")

    esp_exibicao = apresentar_espetaculos(cursor)

    print("0 - Voltar ao menu anterior.")
    print("")
    try:
        opcao = int(input("Indique uma das opções: "))
    except:
        input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
        return
    
    if opcao < 0 or opcao > len(esp_exibicao):
        input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
    elif opcao == 0:
        prox_menu[0] = "main"
        return
    else:
        if prox_menu[0] == "exibicao":
            prox_menu[0] = "sessao"
        elif prox_menu[0] == "2_exibicao":
            prox_menu[0] = "2_sessao"
        elif prox_menu[0] == "3_exibicao":
            prox_menu[0] = "3_sessao"
        return [esp_exibicao[opcao-1][0], esp_exibicao[opcao-1][1]]     

#Menu seleção de espetáculo para criar sessão
def criar_sessao_exibicao(cursor, prox_menu):
    opcao = -1
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("---Espetáculos Disponíveis---")
    print("")

    esp_exibicao = apresentar_espetaculos(cursor)

    print("0 - Voltar ao menu anterior.")
    print("")

    try:
        opcao = int(input("Indique uma das opções: "))
    except:
        input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
        return

    if opcao < 0 or opcao > len(esp_exibicao):
        input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
    elif opcao == 0:
        prox_menu[0] = "main"
        return
    else:
        prox_menu[0] = "5_sessao"
        return [esp_exibicao[opcao-1][0], esp_exibicao[opcao-1][1]]  

def criar_nova_sessao(db, cursor, id_espetaculo, prox_menu):
    today = datetime.datetime.today()
    sessoes_validas = [1, 2, 3]
    print_horas_sessoes = ["1 - Sessão das 21h00", "2 - Sessão das 22h00", "3 - Sessão das 23h00"]
    datas_ocup = []

    print("")
    data_sessao = input("Indique a data da nova sessão (aaaa-mm-dd): ")

    if data_sessao == "0":
        prox_menu[0] = "main"
        return

    try: 
        time.strptime(data_sessao, "%Y-%m-%d")
        comp_data = data_sessao.split("-")
    except:
        input("\033[1;31m" + "A data inserida é inválida." + "\033[0;0m")
        prox_menu[0] = "5_exibicao"
        return
    else:
        if datetime.datetime(today.year, today.month, today.day) > datetime.datetime(int(comp_data[0]),int(comp_data[1]),int(comp_data[2])):
            input("\033[1;31m" + "A data da nova sessão não pode ser no passado." + "\033[0;0m")
            prox_menu[0] = "5_exibicao"
            return
        else:
            query_sessoes = """SELECT sessao 
                                FROM sessoes 
                                WHERE data = ?"""
            params = (data_sessao,)
            result_query_sessao = cursor.execute(query_sessoes, params).fetchall()

            if len(result_query_sessao) == 3:
                input("\033[1;31m" + "Já não existem sessões disponíveis para a data indicada." + "\033[0;0m")
                prox_menu[0] = "5_exibicao"
                return
            else:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"---Sessões disponíveis para a data {data_sessao}")
                    print("")

                    if result_query_sessao != None:
                        for i in range(len(result_query_sessao)):
                            datas_ocup.append(result_query_sessao[i][0])
                        n_opcoes = []
                        for i in sessoes_validas:
                            if i not in datas_ocup:
                                print(print_horas_sessoes[i-1])
                                n_opcoes.append(i)
                        try:
                            print("")
                            opcao_nova_sessao = int(input("Indique uma das opções: "))
                            if opcao_nova_sessao == 0:
                                prox_menu[0] = "5_exibicao"
                                return
                            
                            elif opcao_nova_sessao not in n_opcoes:
                                raise Exception
                        except:
                            input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")
                        else:
                            break
                db_insert_sessao = """INSERT INTO sessoes (id_espetaculo, data, sessao, ativo, finalizado, receita, vendidos_vip, vendidos_normal) 
                                    VALUES (?,?,?,?,?,?,?,?)"""
                params_insert = (id_espetaculo,data_sessao,opcao_nova_sessao,1,0,0,None,None)
                cursor.execute(db_insert_sessao,params_insert)
                db.commit()
                input("\033[1;32m" + "Nova sessão criada com sucesso." + "\033[0;0m")
                prox_menu[0] = "main"

#Menu principal
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    opcao = -1
    db = ctl.create_connection('bilheteira.db')
    if db == "error":
        input("\033[1;31m" + "Erro ao ligar à base de dados. Por favor, verifique se o ficheiro 'bilheteira.db' se encontra na mesma pasta que program.py." + "\033[0;0m")
        opcao = 0
    else:
        cursor = db.cursor()
        while opcao != 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---Menu Principal---")
            print("")
            print("1 - Reservar lugares")
            print("2 - Alterar reserva")
            print("3 - Eliminar reserva")
            print("4 - Consultar valor da bilheteira")
            print("5 - Criar sessão")
            print("0 - Fechar programa")
            print("")
            opcao = input("Indique uma das opções: ")
            match opcao:
                case "1":
                    prox_menu = ["exibicao"] #Menu a apresentar. Valor irá ser alterado nas funções de forma a controlar o proximo menu a apresentar
                    while prox_menu[0] != "main":
                        match prox_menu[0]:
                            case "exibicao":
                                dados_exibicao = em_exibicao(cursor, prox_menu)
                            case "sessao":
                                dados_sessao = selecao_sessoes(cursor, dados_exibicao[0], dados_exibicao[1], prox_menu)
                            case "reserva":
                                reserva_lugares(db, cursor, dados_sessao, dados_exibicao[0], dados_exibicao[1], prox_menu)
                case "2":
                    prox_menu = ["2_exibicao"] #Menu a apresentar. Valor irá ser alterado nas funções de forma a controlar o proximo menu a apresentar
                    while prox_menu[0] != "main":
                        match prox_menu[0]:
                            case "2_exibicao":
                                dados_exibicao = em_exibicao(cursor, prox_menu)
                            case "2_sessao":
                                dados_sessao = selecao_sessoes(cursor, dados_exibicao[0], dados_exibicao[1], prox_menu)
                            case "alterar":
                                alterar_reserva(db, cursor, dados_sessao, dados_exibicao[0], dados_exibicao[1], prox_menu)
                case "3":
                    prox_menu = ["3_exibicao"] #Menu a apresentar. Valor irá ser alterado nas funções de forma a controlar o proximo menu a apresentar
                    while prox_menu[0] != "main":
                        match prox_menu[0]:
                            case "3_exibicao":
                                dados_exibicao = em_exibicao(cursor, prox_menu)
                            case "3_sessao":
                                dados_sessao = selecao_sessoes(cursor, dados_exibicao[0], dados_exibicao[1], prox_menu)
                            case "eliminar":
                                eliminar_reserva(db, cursor, dados_sessao, dados_exibicao[0], dados_exibicao[1], prox_menu)
                case "4":
                    prox_menu = ["4_menu_contabilidade"] #Menu a apresentar. Valor irá ser alterado nas funções de forma a controlar o proximo menu a apresentar
                    while prox_menu[0] != "main":
                        match prox_menu[0]:
                            case "4_menu_contabilidade":
                                contabilidade(cursor, prox_menu)
                case "5":
                    prox_menu = ["5_exibicao"]
                    while prox_menu[0] != "main":
                        match prox_menu[0]:
                            case "5_exibicao":
                                dados_exibicao = criar_sessao_exibicao(cursor, prox_menu)
                            case "5_sessao":
                                criar_nova_sessao(db, cursor, dados_exibicao[0], prox_menu)
                case "0":
                    db.close()
                    return
                case default:
                    input("\033[1;31m" + "A opção inserida é inválida." + "\033[0;0m")