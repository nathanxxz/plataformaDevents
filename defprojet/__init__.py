import cv2
from time import sleep
def dados_dos_eventos(email, events):
    lupa = email
    existe = False
    evento = 0

    for i in range(0, len(events)):
        if (lupa == events[i][2]):
            print('NUMERO DO EVENTO', i + 1, 'º NOME DO EVENTO: ', events[i][0], '\n''LOCAL:', events[i][3][0],
                  '\n''PREÇO:',
                  events[i][3][1], 'R$' '\n''DATA:', events[i][4][0], '/', events[i][4][1], '/', events[i][4][2],
                  '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
            print('PESSOAS INSCRITAS NOS EVENTOS: ')
            for j in range(5, len(events[i])):
                print(f'NOME: {events[i][j][0]}')
                print(f'EMAIL: {events[i][j][1]}')
                print('------------------------------')
            valor = (float(events[i][3][1]) * (len(events[i]) - 5))
            print(f'NUMERO DE PARTICIPANTES: {len(events[i]) - 5} ')
            print(f'VALOR ARRECADADO: R$ {valor}')
            print('EVENTO ENCONTRADO COM SUCESSO!')
            print('------------------------------')
            existe = True
            evento = events[i][2]
    if (not existe):
        print('EVENTO INVALIDO, CONFIRA O NOME DO SEU EVENTO NOVAMENTE!')
    else:
        return evento

def  buscar_eventos_f_l(email, events):
    lupa = email
    existe = False
    evento = 0
    for i in range(0,len(events)):
        if(lupa == events[i][2]):
             print('NUMERO DO EVENTO',i+1,'º NOME DO EVENTO: ', events[i][0], '\n''LOCAL:',events[i][3][0], '\n''PREÇO: R$ ',
                      events[i][3][1],'\n''DATA:',events[i][4][0],'/',events[i][4][1],'/',events[i][4][2],
                   '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
             print('PESSOAS INSCRITAS NOS EVENTOS: ')
             for j in range(5,len(events[i])):
                 print(f'NOME: {events[i][j][0]}')
                 print(f'EMAIL: {events[i][j][1]}')
             print('EVENTO ENCONTRADO COM SUCESSO!')
             print('------------------------------')
             existe = True
             evento = events[i][2]
    if (not existe):
        print('EVENTO INVALIDO, CONFIRA O NOME DO SEU EVENTO NOVAMENTE!')
    else:
        return evento

def apagar_evento(gmail, events):
    for i in range(len(events)):
        if (gmail == events[i][2]):
            print('NUMERO DO EVENTO', i + 1, 'º NOME DO EVENTO: ', events[i][0], '\n''LOCAL:', events[i][3][0],
                  '\n''PREÇO:',
                  events[i][3][1], 'R$''\n''DATA: ', events[i][4][0], '/', events[i][4][1], '/', events[i][4][2],
                  '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
            print('------------------------------')
            print('EVENTO ENCONTRADO COM SUCESSO!')
            resposta = input('DIGITE O NUMERO DO EVENTO QUE DESEJA APAGAR PARA CONFIRMAR OU OUTRA TECLA PARA CANCELAR E IR PARA O PRÓXIMO EVENTO: ').upper().strip()
            if (resposta.isnumeric()):
                resposta = int(resposta) - 1
                if (resposta >= 0 and resposta < len(events) and events[resposta][0].upper() == events[i][0].upper()):
                    confirma = input('TEM CERTEZA QUE DESEJA APAGAR O EVENTO?: ').upper().strip()
                    if (confirma == 'SIM'):
                        events.pop(resposta)
                        print('EVENTO APAGADO COM SUCESSO')
                        return True
                else:
                    print('OPERAÇÃO CANCELADA, O EVENTO NÃO FOI DELETADO')
    print('NÃO HÁ MAIS EVENTOS CADASTRADOS POR ESSE USUÁRIO')
    return False
def buscar_eventos_f(email, events):
    existe = False
    evento = 0
    op = -1
    while(op == 1):
        lupa = email
        for i in range(0,len(events)):
            if(lupa == events[i][2]):
             print('NUMERO DO EVENTO',i+1,'º NOME DO EVENTO: ',events[i][0], '\n''LOCAL:',events[i][3][0], '\n''PREÇO:',
                      events[i][3][1],'R$''\n''DATA: ',events[i][4][0],'/',events[i][4][1],'/',events[i][4][2],
                   '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
             print('------------------------------')
             print('EVENTO ENCONTRADO COM SUCESSO!')

             existe = True
             email = events[i][2]
        if(not existe):
            print('EVENTO INVALIDO, CONFIRA O EMAIL DO RESPONSAVEL PELO EVENTO NOVAMENTE!')
        else:
         return evento

def inscricao_eventos(nome, gmail, nome_e, events, usersBan):
    for nom in usersBan:
        if (nome == nom):
            print('USUÁRIO BANIDO, NÃO PODE SE INSCREVER EM EVENTOS')
            return False
    for i in range(len(events)):
        if (nome_e.upper() == events[i][0].upper()):
            for j in range(5, len(events[i])):
                if (events[i][j][1] == gmail):
                    print('USUÁRIO JÁ CADASTRADO NESSE EVENTO!')
                    break
    resposta = input('EM QUAL EVENTO DESEJA SE CADASTRAR (DIGITE O NÚMERO PARA CONCLUIR CADASTRO'
                     ' OU OUTRA TECLA PARA CANCELAR)?').upper().strip()
    if resposta.isnumeric():
        resposta = int(resposta) - 1
        if (resposta >= 0 and resposta < len(events) and events[resposta][0].upper() == nome_e.upper()):
            events[resposta].append([nome, gmail])
            file = open(f'N_E= {nome_e}.txt', 'a')
            print('FOTO DE CONFIRMAÇAO DE INSCRIÇAO EM: ')
            for cont in range(3, -1, -1):
                print(cont)
                sleep(0.5)
            webcam = cv2.VideoCapture(0)
            if webcam.isOpened():
                validacao, frame = webcam.read()
                cv2.imshow('foto da webcam', frame)
                key = cv2.waitKey(1000)
                cv2.imwrite(f'E={nome_e} N_P={nome} G_P={gmail}.png', frame)
            file.write(nome + '=' + gmail + '\n')
            file.close()
            webcam.release()
            cv2.destroyAllWindows()
            print('---------------------------')
            print('FOTO FINALIZADA COM SUCESSO')
            print('---------------------------')

            return True
    return False

def buscar_eventos(events):
    existe = False
    evento = 0
    op=-1
    while(op != 0):
        lupa = input('DIGITE O NOME DO EVENTO QUE DESEJA BUSCAR (DIGITE 0 PARA CANCELAR A OPERAÇÃO):')
        if(lupa=='0'):
            return '0'
        for i in range(0,len(events)):
            if(lupa == events[i][0]):
             print('NUMERO DO EVENTO ',i+1,'º NOME DO EVENTO: ',events[i][0],
                   '\nLOCAL: ',events[i][3][0],
                   '\nPREÇO: R$',events[i][3][1],
                   '\nDATA: ',events[i][4][0],'/',events[i][4][1],'/',events[i][4][2],
                   '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
             print('------------------------------')
             print('EVENTO ENCONTRADO COM SUCESSO!')

             existe = True
             evento = events[i][0]
        if(not existe):
            print('EVENTO INVALIDO, CONFIRA O NOME DO SEU EVENTO NOVAMENTE!')
        else:
          return evento

def cadastrar_eventos(gmail, cidadesDisp, events):
    cdd=''
    dia=''
    mes=''
    ano=''
    hora=''
    minuto=''
    valorInscricao = ''
    op = -1
    titulo = input('DIGITE O NOME DO EVENTO QUE DESEJA CRIAR: ')
    descricao = input('INSIRA A DESCRIÇAO NO SEU EVENTO: ')

    while (op != 0 ):
        print('-------------------------------------------------------')
        dia = input('DIGITE O DIA QUE DESEJA REALIZAR O EVENTO: ')
        mes = input('DIGITE O MES QUE DESEJA REALIZAR O EVENTO: ')
        ano = input('DIGITE O ANO QUE DESEJA REALIZAR O EVENTO: ')
        if(dia.isnumeric() and mes.isnumeric() and ano.isnumeric()):
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)

            anoBissexto = False
            if (ano % 100 == 0):
                if (ano % 400 == 0):
                    anoBissexto = True
            elif (ano % 4 == 0):
                anoBissexto = True
            if (ano >= 2024):
                if (dia >= 1 and dia <= 28 and mes >= 1 and mes <= 12):
                    print('DATA VALIDA')
                    break
                elif (dia == 29 and mes == 2 and anoBissexto):
                    print('DATA VALIDA')
                    break
                elif (dia >= 29 and dia <= 30 and mes != 2):
                    print('DATA VALIDA')
                    break
                elif (dia == 31 and (
                        mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)):
                    print('DATA VALIDA')
                    break
                else:
                    print('DATA INVÁLIDA, VERIFIQUE-A E TENTE NOVAMENTE')
            else:
                print('ANO INVALIDO, INSIRA A DATA CORRETAMENTE!')
        else:
            print('DATA INVÁLIDA, VERIFIQUE-A E TENTE NOVAMENTE')
    while (op != 0 ):
        hora=input('DIGITE O HORARIO QUE IRA ACONTECE O EVENTO: ')
        minuto=input('DIGITE O MINUTOS: ')
        if (hora.isnumeric() and minuto.isnumeric()):
            hora = int(hora)
            minuto = int(minuto)
            if(hora >= 0 and hora <=24 and minuto >= 0 and minuto <= 60):
                print('HORARIO VALIDO')
                break
            else:
                print('HORARIO INVALIDO !')
        else:
            print('HORARIO INVALIDO !')
    while (op != 0 ):
        cdd = input('INFORME A CIDADE E O ESTADO QUE DESEJA REALIZAR O EVENTO (EX.: JOAO PESSOA(PB): ').upper().strip()
        if (cdd in cidadesDisp):
            print('CIDADE VALIDADA COM SUCESSO!')
            break
        else:
            print('CIDADE INVÁLIDA, CONFIRA SE NAO DIGITOU ALGO ERRADO')

    while (op != 0 ):
        valorInscricao = input('INSIRA O VALOR DA INSCRIÇAO DO SEU EVENTO: ').replace(',', '.')
        if(valorInscricao.replace('.', '').isnumeric()):
            valorInscricao = float(valorInscricao)
            if (valorInscricao >= 0):
                print('VALOR VALIDO')
                break
            else:
                print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')
        else:
            print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')
    events.append([titulo, descricao, gmail, [ cdd, valorInscricao], [dia, mes, ano,hora,minuto]])

def login_eventos(lista, email):
    ind =-1
    for i in range(len(lista)):
        if (lista[i][2] == email):
            ind = i
            break
    if (ind != -1):
        print('---------------------------')
        print('LOGIN EFETUADO COM SUCESSO')
        print('---------------------------')
        return True
    else:
        return False

def listar_eventos(events):
    listar=input('VOCE DESEJA VER TODOS OS EVENTOS(SIM OU NAO)?: ').upper().strip()
    if(listar=='SIM'):
        for i in range(0, len(events)):
            print('NUMERO DO EVENTO', i + 1, 'º NOME DO EVENTO:', events[i][0], '\n''LOCAL:', events[i][3][0],
                  '\n''PREÇO:',
                  events[i][3][1], 'R$''\n''DATA:', events[i][4][0], '/', events[i][4][1], '/', events[i][4][2],
                  '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
            print('------------------------------')