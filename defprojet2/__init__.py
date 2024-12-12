import matplotlib.pyplot as plt
def TabelaPart(events):
    namesEventts=[]
    qtdPart=[]

    for evento in events:
        namesEventts.append(evento[0])
        participantes = (len(evento) - 5)
        qtdPart.append(participantes)

    if(len(namesEventts) == 0):
        print('NENHUM EVENTO ENCONTRADO')
        return

    plt.bar(namesEventts, qtdPart, color='red')
    plt.xlabel('EVENTOS')
    plt.ylabel('QUANTIDADE DE PARTICIPANTES')
    plt.title('QUANTIDADE DE PARTICIPANTES POR EVENTO')
    plt.yticks(range(0,max(qtdPart)+1))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def ListarBanPlataforma(usersBan):
    verBan=input('DESEJA VER A LISTA DE BANIDOS DA PLATAFORMA?(SIM/NAO').upper().strip()
    if (verBan == 'SIM'):
        for i in range(0, len(usersBan)):
            print(i+1,'USUARIOS BANIDOS:', usersBan[i])

def UsersBann(usersBan):
    print('---------------------------')
    print('QUESTIONARIO DE VERIFICAÇAO')
    print('---------------------------')
    while True:
        nome = input('DIGITE SEU NOME COMPLETO: ').upper().strip()
        per = input('VOCE JA COMETEU ALGUM TIPO DE CRIME? (SIM/NAO) ').lower().strip()
        if(per == 'nao'):
            print(f'REDIRECIONANDO O USUARIO(A) {nome} A PAGINA DE CADASTRO')
            return
        print('----------------------------------')
        print('        LISTA DE PROIBIÇAO        ')
        print('----------------------------------')
        crimes = {'ASSASSINATO': 'ASSASSINATO', 'FURTO GRAVE': 'FURTO GRAVE', 'CRIME CIBERNETICO': 'CRIME CIBERNETICO', 'LATROCINIO': 'LATROCINIO','TRAFICO DE DROGAS':'TRAFICO DE DROGAS'}
        for crime in crimes.values():
            print(f'{crime}')
        print('---------------------------------')
        per2 = input('O CRIME COMETIDO FOI? ').upper().strip()
        if(per2 in crimes):
            print(f'INFELIZMENTE O USUARIO(A) {nome} NAO TERA ACESSO A FUNCOES DA PLATAFORMA DEVIDO AO CRIME DE {per2}')
            usersBan.append(nome)
            return


def ad_participante_eventos(gmail,nome_e, events,usersBan):
    for i in range(len(events)):
        if(nome_e.upper() == events[i][0].upper()):
            for j in range(5, len(events[i])):
                if (events[i][j][1] == gmail):
                    print('USUÁRIO JÁ CADASTRADO NESSE EVENTO!')
                    break
    resposta = input('EM QUAL EVENTO DESEJA SE CADASTRAR (DIGITE O NUMERO PARA CONCLUIR CADASTRO'
                     ' OU OUTRA TECLA PARA CANCELAR)?').upper().strip()
    if(resposta.isnumeric()):
        resposta = int(resposta) - 1
        if(resposta >= 0 and resposta < len(events) and events[resposta][0].upper() == nome_e.upper()):
            nome_do_perticipante= input('DIGITE O NOME DE USUARIO QUE DESEJA ADICIONAR:').upper()
            for nom in usersBan:
                if (nome_do_perticipante == nom):
                    print('USUARIO BANIDO, NAO PODE SER ADICIONADO EM EVENTOS')
                    return False
            gmail_do_participante = input('DIGITE O GMAIL D0 USUARIO:').upper()
            events[resposta].append([nome_do_perticipante, gmail_do_participante])
            file = open(f'N_E_=_{nome_e}.txt', 'a')
            file.write(nome_do_perticipante +'='+ gmail_do_participante + '\n')
            file.close()
            print('CADASTRO REALIZADO COM SUCESSO')
            return True
    return False

def calculadora_financeira():
    receit=''
    gastos=''
    op=-1
    while(op!= 0):

        while (op!= 0):
            receit = input('DIGITE A RECEITA DO SEU EVENTO: ').replace(',', '.')
            if (receit.replace('.', '').isnumeric()):
                receit = float(receit)
                if (receit >= 0):
                    print('VALOR VALIDO')
                    break
                else:
                    print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')
            else:
              print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')

        while (op!= 0):
            gastos = input('DIGITE QUANTO VOCE GASTOU PARA CRIAR O EVENTO: ').replace(',', '.')
            if (gastos.replace('.', '').isnumeric()):
                gastos = float(gastos)
                if (gastos >= 0):
                    print('VALOR VALIDO')
                    break
                else:
                    print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')
            else:
              print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')

        lucroTotal=receit-gastos
        if (lucroTotal >= 0):
            print(f'O SEU LUCRO FOI {lucroTotal}')
        else:
            print(f'INFELIZMENTE VOCE TEVE UM PREJUIZO DE {lucroTotal * -1}')

        porc=input('DESEJA VER A PORCENTAGEM DE GASTOS?').lower().strip()
        if(porc=='sim'):
            porcentagem = (gastos / receit) * 100
            print(f'ESSA FOI A PORCENTAGEM DE GASTOS {porcentagem} %')
        porcentagem2=input('DESEJA VER EM FORMA DE PORCENTAGEM OS SEUS LUCROS?').lower().strip()
        if(porcentagem2=='sim'):
            porcentagemLu = (lucroTotal / receit) * 100
            print(f'ESSA FOI A PORCENTAGEM DE LUCROS {porcentagemLu} %')

        exit=input('DESEJA CONTINUAR NA CALCULADORA? ("SIM" PARA CONTINUAR, OUTRA TECLA PARA SAIR)').lower().strip()
        if(exit!='sim'):
            break
def verificar_nome(nome):
    if (len(nome) >= 3):
        return True
    else:
        return False

def verificar_email(email):
    if ('@gmail.com' in email or '@GMAIL.COM' in email):
        return True
    else:
        return False

def verificar_senha(senha1, senha2):
    if (senha1 == senha2 and len(senha1) >= 8 and len(senha2) >= 8):
        return True
    else:
        return False

def verificar_user_existente(email, usuarios):
    existe = False
    for user in usuarios:
        if (user[1] == email):
            existe = True
            break
    return existe

def login(users, email, senha):
    ind = -1
    for i in range(len(users)):
        if (users[i][1] == email and users[i][2] == senha):
            ind = i
    if (ind != -1):
        print(f'LOGIN EFETUADO COM SUCESSO, SEJA BEM VINDO(A) {users[ind][0].upper()}')
        return users[ind]
    else:
        return False