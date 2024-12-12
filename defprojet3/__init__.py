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