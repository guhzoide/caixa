import PySimpleGUI as sg

def sistema():
    sg.theme('LightBrown10')
    login = [
        [sg.Text('nome'), sg.Input(key='nome', size=(50,1))],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(50,1))],
        [sg.Text('Cod. de Seg.'), sg.Input(key='codseg', password_char='*')],
        [sg.Button('entrar', size=(8,1)), sg.Button('cadastro', size=(8,1)), sg.Button('sair', size=(8,1))]
    ]

    sg.theme('LightBrown10')
    cadastro = [
        [sg.Text('Nome'), sg.Input(key='nome')],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
        [sg.Text('Codigo de Segurança'), sg.Input(key='codseg', password_char='*', size=(33,1))],
        [sg.Button('salvar'), sg.Button('voltar')]
    ] 

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
            sg.popup_auto_close('Nome, senha ou cod. de segurança incorretos')
            sistema()
        elif login in banco:
            from caixa import EntradaSaida
            
        else:
            sg.popup_auto_close('Nome, senha ou cod. de segurança incorretos')
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
            sg.popup_auto_close("Acao realizada com sucesso")
            sistema()
        elif eventos == 'voltar':
            janela.close()
            sistema()

    elif eventos == 'sair':
        choose = sg.popup_yes_no('Deseja sair do caixa?')
        if choose == 'Yes':
            janela.close()
        else:
            janela.close()
            sistema()    
sistema()
