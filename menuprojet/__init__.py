from defprojet import *
from defprojet2 import *
from defprojet3 import *
users = [['rene', 'rene@gmail.com', 'rene1234'], ['samuel', 'samuel@gmail.com', 'samuel1234'], ['jose', 'jose@gmail.com', 'jose1234'],['pedro','pedro@gmail.com','pedro1234'],['pedro2','pedro2@gmail.com','pedro1234']]
events = [['BatmanEvent','ai','pedro2@gmail.com',['joao pessoa',10],[1,2,2024,18,30],['batman','batman@gmail.com'],['pikachu','pikachu@gmail.com']],['RobinEvent','ai','pedro2@gmail.com',['joao pessoa',20],[1,2,2024, 17, 0],['Jotaro Kujo', 'jojo@gmail.com']],['CoringaEvent','ai','pedro2@gmail.com',['joao pessoa',10],[1,2,2024, 8, 20]],]
cidadesDisp = ['RIO BRANCO(AC)','MACEIO(AL)','MACAPA(AP)','MANAUS(AM)','SALVADOR(BA)','FORTALEZA(CE)','BRASILIA(DF)','VITORIA(ES)','GOIANIA(GO)','SAO LUIS(MA)','CUIABA(MT)','CAMPO GRANDE(MS)','BELO HORIZONTE(MG)','BELEM(PA)','JOAO PESSOA(PB)','CURITIBA(PR)','RECIFE(PE)','TERESINA(PI)','RIO DE JANEIRO(RJ)','NATAL(RN)','PORTO ALEGRE(RS)','PORTO VELHO(RO)','BOA VISTA(RR)','FLORIANOPOLIS(SC)','SAO PAULO(SP)','ARACAJU(SE)','PALMAS(TO)']
usersBan=[]

op = -1
while (op != 0):
    print('-----------------------------------')
    print('  SEJA BEM-VINDO AO GADELHAEVENTS  ')
    print('-----------------------------------')
    print('1-CRIAR CONTA NA PLATAFORMA ')
    print('2-EFETUAR LOGIN')
    print('0-SAIR DO PROGRAMA')

    print('-----------------------------------')
    opcoes = ['0','1','2']
    op = input('DIGITE A OPÇAO DESEJADA: ').strip()
    while(op not in opcoes):
        op = input('DIGITE UMA OPÇÃO VÁLIDA: ').strip()
    op = int(op)
    print('-----------------------------------')
    if (op == 1):
        UsersBann(usersBan)
        nome1 = input('PORFAVOR, INSIRA SEU NOME COMPLETO NOVAMENTE: ').upper().strip()
        while (not verificar_nome(nome1)):
            print('NOME SO PODE TER 3 OU MAIS CARACTERES ')
            print('--------------------------------------')
            nome1 = input('PORFAVOR, INSIRA SEU NOME NOVAMENTE: ')
        email = input('DIGITE SEU EMAIL PRINCIPAL: ').strip()
        while (not verificar_email(email)):
            print('EMAIL INVALIDO!!')
            print('------------------------')
            email = input('PORFAVOR, INSIRA SEU EMAIL VALIDO: ').strip()
            while (verificar_user_existente(email, users)):
                print('------------------------------------')
                print('ESSE EMAIL JA ESTA SENDO UTILIZADO ')
                print('------------------------------------')
                email = input('PORFAVOR, INSIRA SEU EMAIL NOVAMENTE: ').strip()
        senha = input('DIGITE SUA SENHA COM 8 OU MAIS CARACTERES: ')
        senha2 = input('PORFAVOR, CONFIRME SUA SENHA: ')
        while (not verificar_senha(senha, senha2)):
            print('DESTA VEZ, DIGITE SENHAS QUE SEJAM IGUAIS E TENHAM 8 OU MAIS CARACTERES ')
            print('----------------------------------------------------------')
            senha = input('DIGITE SUA SENHA: ')
            senha2 = input('CONFIRME SUA SENHA: ')

        users.append([nome1, email, senha])

    elif(op == 2):
        email = input('DIGITE SEU EMAIL CADASTRADO: ')
        senha = input('DIGITE SUA SENHA: ')
        userAtual = login(users, email, senha)
        while (not userAtual):
            print('ERRO!!! A SENHA OU O EMAIL ESTAO INCORRETOS')
            print('-----------------------------------')
            email = input('DIGITE SEU EMAIL: ')
            senha = input('DIGITE SUA SENHA: ')
            userAtual = login(users, email, senha)

        ope = -1
        while (ope != 0):
            print('---------------------------------------------------')
            print(f' OLA {userAtual[0].upper()}, O QUE VOCE GOSTARIA DE REALIZAR HOJE ')
            print('---------------------------------------------------')
            print('1-PARTICIPAR DE UM EVENTO')
            print('2-CRIAR UM EVENTO')
            print('3-MENU DE CRIADOR')
            print('4-VER LISTA DE EVENTOS')
            print('0-ENCERRAR SESSÃO')
            print('---------------------------------------------------')

            opcoes = ['0', '1', '2', '3', '4']
            ope = input('DIGITE A OPÇAO DESEJADA: ').strip()
            while (ope not in opcoes):
                ope = input('DIGITE UMA OPÇÃO VÁLIDA: ').strip()
            ope = int(ope)
            print('--------------------------------------------------')
            if(ope == 1):
                nome_e=buscar_eventos(events)
                nome = userAtual[0]
                gmail = userAtual[1]

                while (nome_e!='0' and not inscricao_eventos(nome,gmail,nome_e, events,usersBan)):
                    nome_e = buscar_eventos(events)

            if (ope == 2):
                gmail = userAtual[1].strip()
                cadastrar_eventos(gmail, cidadesDisp, events)

            if (ope == 3):
                email = userAtual[1]
                if (not login_eventos(events, email)):
                    print('ERRO!!! VOCÊ NAO TEM NENHUM EVENTO CADASTRADO')
                    print('-------------------------------------------------------')
                    opi = 0
                else:
                    opi = -1
                while (opi != 0):
                    print('-------------------------------------------------------')
                    print(f'  OLA {userAtual[0].upper()} O QUE DESEJA FAZER HOJE: ')
                    print('-------------------------------------------------------')
                    print('1-REMOVER EVENTO')
                    print('2-LISTAR PARTICIPANTES DO EVENTO')
                    print('3-LISTAR DADOS DOS EVENTOS')
                    print('4-CALCULAR FINANÇAS')
                    print('5-INSCREVER PARTICIPANTE')
                    print('6-MOSTRAR TABELA EVENTOS')
                    print('7-LISTAR BANIDOS DA PLATAFORMA')
                    print('0-VOLTAR PARA O MENU PRINCIPAL')
                    print('--------------------------------------------------------')

                    print('---------------------------------------------------')

                    opcoes = ['0', '1', '2', '3', '4','5','6','7']
                    opi = input('DIGITE A OPÇAO DESEJADA: ').strip()
                    while (opi not in opcoes):
                        opi = input('DIGITE UMA OPÇÃO VÁLIDA: ').strip()
                    opi = int(opi)
                    print('--------------------------------------------------')
                    if(opi == 1 ):
                        print('EVENTOS CADASTRADOS COM SEU GMAIL: ')
                        apagar_evento(userAtual[1], events)
                    if(opi == 2 ):
                        buscar_eventos_f_l(userAtual[1], events)
                    if(opi == 3 ):
                        dados_dos_eventos(userAtual[1], events)
                    if(opi==4):
                        calculadora_financeira()
                    if(opi == 5):
                        nome_e = buscar_eventos(events)
                        gmail = userAtual[1]

                        ad_participante_eventos(gmail, nome_e, events,usersBan)
                    if(opi==6):
                        TabelaPart(events)
                    if(opi==7):
                        ListarBanPlataforma(usersBan)

                    if(opi == 0):
                        break
            if (ope == 4):
                listar_eventos(events)
    if(op == 0):
        print('PROGRAMA FECHADO')