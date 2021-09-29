# GERADOR DE SENHAS
import random
from PySimpleGUI import PySimpleGUI as sg

# Declarando as váriaveis
minusculo = ("abcdefghjklmnopqrstuvwxyz")
maiusculo = ("ABCDEFGHJKLMNOPQRSTUVWXYZ")
numeros = ("0123456789")
simbolos = ("@#$%&*")

# Juntando as variáveis e pegando o tamanho e número de senhas que devem ser geradas
varjuntas = minusculo + maiusculo + numeros + simbolos
tamanho = ("")
nmrsenhas = ("")

# Layout da tela
sg.theme('DarkBlue')
layout = [
    [sg.Text('Tamanho da senha:')],
    [sg.Input(tamanho)],
    [sg.Text('Número de senhas que serão geradas:')],
    [sg.Input(nmrsenhas)],
    [sg.Text('')],
    [sg.Button('Gerar Senha'), sg.Button('Cancelar')]
]

# Janela que abrirá
janela = sg.Window('GERADOR DE SENHAS', layout)

# Ler os eventos que devem ocorrer
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or 'Cancelar':
        break
    if evento == 'Gerar Senha':
        for senha in range(int(valores = nmrsenhas)):
            senha = random.sample(varjuntas, int(valores = tamanho))
            print("".join(senha))

#import PySimpleGUI as sg
#
#def ChatBot():
#    layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],
#              [sg.Output(size=(80, 20))],
#              [sg.Multiline(size=(70, 5), enter_submits=True),
#               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
#               sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
#
#    window = sg.Window('Chat Window', layout, default_element_size=(30, 2))
#
#    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
#    while True:
#        event, value = window.read()
#        if event == 'SEND':
#            print(value)
#        else:
#            break
#    window.close()
#ChatBot()