#from tkinter.constants import CENTER
from datetime import date
import PySimpleGUI as sg
import shutil
import telepot
import os

from PySimpleGUI.PySimpleGUI import Save

def EntradaSaida():
    sg.theme('LightBrown10')
    escolha = [
        [sg.Text('')],
        [sg.Text('                                                       '), sg.Text('Bem vindo(a) ao', font='Arial 15')],
        [sg.Text('        '), sg.Image(r"C:\caixa\bds\teste.png")],
        [sg.Text('                                               '), sg.Text('O que deseja fazer ?', font='Arial 15' ,size=(0,2))],
        [sg.Button('Dar entrada', font='Arial 12', size=(15,0)), sg.Button('Dar saida', font='Arial 12', size=(15,0)), sg.Button('Valor atual no caixa', font='Arial 12', size=(15,0)), sg.Button('Sair', font='Arial 12', size=(15,0))]
    ]

    sg.theme('LightBrown10')
    entrada = [
        [sg.Text('Data de entrada'), sg.Input(key='datae')],
        [sg.Text('Detalhes', size=(12,1)), sg.Input(key='detalhes')],
        [sg.Text('Valor de entrada'), sg.Input(key='entrada')],
        [sg.Button('Salvar', size=(15,0)), sg.Button('Voltar', size=(15,0))]
    ]

    sg.theme('LightBrown10')
    saida = [
        [sg.Text('Data de saida'), sg.Input(key='datas')],
        [sg.Text('Detalhes', size=(10,1)), sg.Input(key='detalhes')],
        [sg.Text('Valor de saida'), sg.Input(key='saida')],
        [sg.Button('Salvar', size=(15,0)), sg.Button('Voltar', size=(15,0))]
    ]

    sg.theme('LightBrown10')
    suc = [
        [sg.Text('Ação realizada com sucesso')],
        [sg.Button('Voltar')]
    ]

    sg.theme('LightBrown10')
    sair = [
        [sg.Text('Deseja fechar o sistema ?', font='Arial 12')],
        [sg.Button('sim', font='Arial 12', size=(8,0)), sg.Button('não', font='Arial 12', size=(8,0))]
    ]

    sg.theme('LightBrown10')
    erro = [[sg.Text('ERRO - Preencha todos os campos')], [sg.Button('Voltar')]]

    janelamain = sg.Window('Escolha', escolha, size=(650,400))
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
            finane = 'Entrada'
            datae = valores['datae']
            entrada = valores['entrada']
            detalhes = valores['detalhes']

            if datae == '' and entrada == '' and detalhes == '':
                janela.close()
                janela = sg.Window('ERRO', erro)
                eventos, valores = janela.read()
                if eventos == 'Voltar':
                    janela.close()
                    EntradaSaida()
            else:       
                valor1 = float(entrada)
                total = ('%.2f' %(valor + valor1))
                total = str(total)
                arq = open(save, 'a')
                arq.write('\n' + finane + '\n')
                arq.write(datae + '\n')
                arq.write(detalhes + '\n')
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
            finans = 'Saida'
            datas = valores['datas']
            saida = valores['saida']
            detalhes = valores['detalhes']

            if datas == '' and saida == '' and detalhes == '':
                janela.close()
                janela = sg.Window('ERRO', erro)
                eventos, valores = janela.read()
                if eventos == 'Voltar':
                    janela.close()
            else:
                valor1 = float(saida)
                resto = ('%.2f' %(valor - valor1))
                total = str(resto)
                arq = open(save, 'a')
                arq.write('\n' + finans + '\n')
                arq.write(datas + '\n')
                arq.write(detalhes + '\n')
                arq.write(saida + '\n')
                arq.write('\n')
                arq.write('Restando\n')
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
        sg.theme('LightBrown10')
        dados = [
            [sg.Multiline(banco, size=(95,35))],
            [sg.Button('Voltar', size=(15,0)), sg.Button('Esvaziar o caixa', size=(15,0)), sg.Button('Salvar caixa', size=(15,0)), sg.Button('Excuir caixa', size=(15,0)), sg.Button('Enviar caixa', size=(15,0))]
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
            janela = sg.Window('Sucesso', suc)
            eventos, valores = janela.read()
            if eventos == 'Voltar':
                janela.close()
                EntradaSaida()

        elif eventos == 'Salvar caixa':
            janela.close()
            file=r'C:\caixa\bds\dados.txt'
            destino=r'C:\caixa'
            shutil.copy(file, destino)
            janela = sg.Window('Sucesso', suc)
            eventos, valores = janela.read()
            if eventos == 'Voltar':
                janela.close()
                EntradaSaida()

        elif eventos == 'Excuir caixa':
            os.remove('dados.txt')
            janela.close()
            janela = sg.Window('Sucesso', suc)
            eventos, valores = janela.read()
            if eventos == 'Voltar':
                janela.close()
                EntradaSaida()

        
        elif eventos == 'Enviar caixa':
            from bot import enviacx
            janela.close()
            data = date.today()
            data = str(data)
            bot = telepot.Bot("5091884786:AAHB5kyw8mevUTgBy3p6ypfGWqItlBKLZ7k")
            arq = open('dados.txt', 'r')
            dados = arq.read()
            bot.sendMessage(-682841708, data)
            bot.sendMessage(-682841708, dados)
            janela = sg.Window('Sucesso', suc)
            eventos, valores = janela.read()
            if eventos == 'Voltar':
                janela.close()
                EntradaSaida()

        elif eventos == 'Voltar':
            janela.close()
            EntradaSaida()

    elif eventos == 'Sair':
        janelamain.close()
        janela = sg.Window('', sair)
        eventos = janela.read()
        if eventos == ('sim', {}):
            janela.close()
        elif eventos == ('não', {}):
            janela.close()
            EntradaSaida()
EntradaSaida()