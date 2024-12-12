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
