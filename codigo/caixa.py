from datetime import date
import PySimpleGUI as sg
import shutil
import telepot

def EntradaSaida():
    sg.theme('LightBrown10')
    escolha = [
        [sg.Text('')],
        [sg.Text('Bem vindo(a) ao', font='Arial 15')],
        [sg.Image(r"C:\caixa\bds\teste.png")],
        [sg.Text('O que deseja fazer ?', font='Arial 15' ,size=(0,2))],
        [sg.Button('Dar entrada', font='Arial 12', size=(15,0)), sg.Button('Dar saida', font='Arial 12', size=(15,0)), sg.Button('Valor atual no caixa', font='Arial 12', size=(15,0)), sg.Button('Sair', font='Arial 12', size=(15,0))]
    ]

    entrada = [
        [sg.Text('Data de entrada'), sg.Input(key='datae')],
        [sg.Text('Detalhes', size=(12,1)), sg.Input(key='detalhes')],
        [sg.Text('Valor de entrada'), sg.Input(key='entrada')],
        [sg.Button('Salvar', size=(15,0)), sg.Button('Voltar', size=(15,0))]
    ]

    saida = [
        [sg.Text('Data de saida'), sg.Input(key='datas')],
        [sg.Text('Detalhes', size=(10,1)), sg.Input(key='detalhes')],
        [sg.Text('Valor de saida'), sg.Input(key='saida')],
        [sg.Button('Salvar', size=(15,0)), sg.Button('Voltar', size=(15,0))]
    ]

    janelamain = sg.Window('Menu', escolha, element_justification='c', size=(650,400))
    eventos, valores = janelamain.read()
    if eventos == sg.WINDOW_CLOSED:
        janelamain.close()

    elif eventos == 'Dar entrada':
        janelamain.close()
        janela = sg.Window('Dar entrada', entrada)
        eventos, valores = janela.read()
        if eventos == 'Salvar':
            save=r'C:\caixa\bds\dados.txt'
            with open(save, 'r') as arq:
                for line in arq:
                    pass
                last = line
            valor = float(last)
            finane = 'Entrada dia:'
            datae = valores['datae']
            entrada = valores['entrada']
            detalhes = valores['detalhes']

            if datae == '' and entrada == '' and detalhes == '':
                janela.close()
                sg.popup_auto_close('ERRO - Preencha todos os campos')
                EntradaSaida()
            else:       
                valor1 = float(entrada)
                total = ('%.2f' %(valor + valor1))
                total = str(total)
                arq = open(save, 'a')
                arq.write('\n' + finane + '\n')
                arq.write(datae + '\n')
                arq.write('Referente a:\n' + detalhes + '\n')
                arq.write('valor de entrada' + '\n')
                arq.write(entrada + '\n')
                arq.write('Restando no caixa\n')
                arq.write(total + '\n')
                arq.close()
                janela.close()
                EntradaSaida()

        elif eventos == 'Voltar':
            janela.close()
            EntradaSaida()
    
    elif eventos == 'Dar saida':
        janelamain.close()
        janela = sg.Window('Dar saida', saida)
        eventos, valores = janela.read()
        if eventos == 'Salvar':
            save=r'C:\caixa\bds\dados.txt'
            with open(save, 'r') as arq:
                for line in arq:
                    pass
                last = line
            valor = float(last)
            finans = 'Saida dia:'
            datas = valores['datas']
            saida = valores['saida']
            detalhes = valores['detalhes']

            if datas == '' and saida == '' and detalhes == '':
                janela.close()
                sg.popup_auto_close('ERRO - Preencha todos os campos')
                EntradaSaida()
            else:
                valor1 = float(saida)
                resto = ('%.2f' %(valor - valor1))
                total = str(resto)
                arq = open(save, 'a')
                arq.write('\n' + finans + '\n')
                arq.write(datas + '\n')
                arq.write('Referente a:\n' + detalhes + '\n')
                arq.write('valor de saida' + '\n')
                arq.write(saida + '\n')
                arq.write('Restando no caixa\n')
                arq.write(total + '\n')
                arq.close()
                janela.close()
                EntradaSaida()
        if eventos == 'Voltar':
            janela.close()
            EntradaSaida()

    elif eventos == 'Valor atual no caixa':
        janelamain.close()
        save=r'C:\caixa\bds\dados.txt'
        arq = open(save, 'r')
        banco = arq.read()
        dados = [
            [sg.Multiline(banco, size=(95,35))],
            [sg.Button('Voltar', size=(15,0)), sg.Button('Salvar caixa', size=(15,0)), sg.Button('Enviar caixa', size=(15,0)), sg.Button('Esvaziar o caixa', size=(15,0)), sg.Button('Recuperar caixa', size=(15,0))]
        ]
        janela = sg.Window('Valor atual no caixa', dados, resizable=True)
        arq.close()
        eventos, valores = janela.read()
        if eventos == 'Esvaziar o caixa':
            save=r'C:\caixa\bds\dados.txt'
            with open(save, "r+") as f:
                f.truncate(0)
                f.close()
            arq = open(save, "a")
            zero = '0'
            arq.write(zero)
            arq.close()
            janela.close()
            sg.popup_auto_close("Acao realizada com sucesso")
            EntradaSaida()

        elif eventos == 'Salvar caixa':
            janela.close()
            file=r'C:\caixa\bds\dados.txt'
            destino = sg.popup_get_folder('Onde deseja salvar o caixa?')
            if destino == None:
                EntradaSaida()
            elif destino == '':
                sg.popup_auto_close("Selecione um local")
                EntradaSaida()
            else:
                shutil.copy(file, destino)
                sg.popup_auto_close("Acao realizada com sucesso")
                EntradaSaida()
        
        elif eventos == 'Enviar caixa':
            janela.close()
            data = date.today()
            data = str(data)
            bot = telepot.Bot("5194360512:AAGLG1EG8MfoMeXnhVyrbx0anCZL5WJ1Ayw")
            file = sg.popup_get_file('Selecione o arquivo do dados do caixa')
            if file == None:
                EntradaSaida()
            elif file == '':
                sg.popup_auto_close("Selecione um local")
                EntradaSaida()
            else:
                arq = open(file, 'r')
                dados = arq.read()
                id = sg.popup_get_text('Digite o seu chat id do telegram')
                if id == None:
                    EntradaSaida()
                elif id == '':
                    sg.popup_auto_close("Necessario informar o chat id")
                    EntradaSaida()
                else:
                    bot.sendMessage(id, data)
                    bot.sendMessage(id, dados)
                    sg.popup_auto_close("Acao realizada com sucesso")
                    EntradaSaida()
        
        elif eventos == 'Recuperar caixa':
            janela.close()
            file = sg.popup_get_file('Selecione o arquivo do dados do caixa?')
            destino=r"C:\caixa\bds"
            shutil.copy(file, destino)
            sg.popup_auto_close("Acao realizada com sucesso")
            EntradaSaida()

        elif eventos == 'Voltar':
            janela.close()
            EntradaSaida()

    elif eventos == 'Sair':
        choose = sg.popup_yes_no('Deseja sair do caixa?')
        if choose == 'Yes':
            janelamain.close()
        else:
            janelamain.close()
            EntradaSaida()
