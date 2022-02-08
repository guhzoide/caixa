import PySimpleGUI as sg

def sistema():
    sg.theme('DarkBlue1')
    login = [
        [sg.Text('nome'), sg.Input(key='nome')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Text('Codigo de Segurança'), sg.Input(key='codseg', password_char='*', size=(33,1))],
        [sg.Button('entrar', size=(8,1)), sg.Button('cadastro', size=(8,1)), sg.Button('sair', size=(8,1))]
    ]

    sg.theme('DarkBlue1')
    cadastro = [
        [sg.Text('Nome'), sg.Input(key='nome')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Text('Codigo de Segurança'), sg.Input(key='codseg', password_char='*', size=(33,1))],
        [sg.Button('salvar'), sg.Button('voltar')]
    ]

    sg.theme('DarkBlue1')
    suc = [
        [sg.Text('Cadastro realizado com sucesso')],
        [sg.Button('Voltar')]
    ]
    
    sg.theme('DarkBlue1')
    sair = [
        [sg.Text('Deseja fechar o sistema ?')],
        [sg.Button('sim', size=(8,0)), sg.Button('não', size=(8,0))]
    ]    

    sg.theme('DarkBlue1')
    erro = [[sg.Text('Nome, senha ou cod. de segurança incorretos, faça um cadastro caso não tiver')]]

    janela = sg.Window('tela login', login)

    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        janela.close()

    elif eventos == 'entrar':
        janela.close()
        nome = valores['nome']
        senha = valores['senha']
        codseg = valores['codseg']
        login = nome + "  |  " + senha + "  |  " + codseg
        cadl=r'C:\caixa\bds\cad.txt'
        arq = open(cadl)
        banco = arq.read()
        if login == "":
            janela = sg.Window('tela login', erro)
            janela.read()
        elif login in banco:
            from caixa import EntradaSaida
            
        else:
            janela = sg.Window('tela login', erro)
            janela.read()
            janela.close()
            sistema()
    
    elif eventos == 'cadastro':
        janela.close()
        janela = sg.Window('Cadastro', cadastro)
        eventos, valores = janela.read()
        if eventos == 'salvar':
            janela.close()
            nome = valores['nome']
            senha = valores['senha']
            codseg = valores['codseg']
            login = nome +  "  |  " + senha + "  |  " + codseg
            cadc=r'C:\caixa\bds\cad.txt'
            arq = open(cadc, 'a')
            arq.write(login + '\n')
            arq.close()       
            janela = sg.Window('Cadastro', suc)
            janela.read()
            janela.close()
            sistema()
        elif eventos == 'voltar':
            janela.close()
            sistema()

    elif eventos == 'sair':
        janela.close()
        janela = sg.Window('Despedida', sair)
        eventos = janela.read()
        if eventos == ('sim', {}):
            janela.close()
        elif eventos == ('não', {}):
            janela.close()
            sistema()    
sistema()