import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import BLUES, theme_text_color

sg.theme('DarkBlue')

layout = [
    [sg.Text('GERADOR DE SENHAS')],
    [sg.Text('Insira o tamanho da senha:'), sg.InputText()],
    [sg.Text('Insira o número de senhas que deve ser gerada:'), sg.InputText()],    
    [sg.Button('Gerar Senha'), sg.Button('Cancelar')]]

window = sg.Window('Gerador de Senhas', layout)
event, values = window.read()
window.close()
print(event, values[0], values[1])