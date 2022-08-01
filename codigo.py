from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, Push
)
import PySimpleGUI as sg

import codigodebarras
import calculodescontoanuidade
import capitalize
import formatar_cnae



#cria o menu inicial
def tela_menu():
    sg.theme("Reddit")
    layout_direita = [
        [sg.Text("Gerenciador", font=("bold",30))],
        [sg.Text("de Tarefas", font=("bold",30))]
    ]

    layout_esquerda = [
        [sg.Text('Selecione um dos programas abaixo:', pad=(10, 8), text_color="#474747", font = ('bold', 14))],
        [sg.Button('Código de Barras', button_color=('white', '#474747'), size=(18,1))], 
        [sg.Button('Descontos de Anuidade', button_color=('white', '#474747'), size=(18,1))],
        [sg.Button('Formatar Texto', button_color=('white', '#474747'), size=(18,1))], 
        [sg.Button('Formatar CNAE', button_color=('white', '#474747'), size=(18,1))], 
        [sg.Button("Sair", tooltip="Clique para fechar o programa", mouseover_colors=('#f54242', "white"), size=(18,1), button_color=('white', '#f54242'))],
    ]

    layout = [
        [Column(layout_direita), VSeparator(), Column(layout_esquerda)]
    ]

    window = Window(
        'Tela de menu',
        layout=layout, finalize=True
    )

    #maximizar a tela
    # window.Maximize()

    return window


#cria as janelas iniciais
janela1, janela2, janela4, janela3, janela5  = tela_menu(), None, None, None, None

#lógica para leitura das múltiplas janelas
while True:
    window, event, values = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == "Sair":
        break
    if window == janela1 and event == 'Código de Barras':
        janela1.hide()
        janela2 = codigodebarras.executar()
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == "Voltar":
        janela2.hide()
        janela1.un_hide()
    if window == janela1 and event == 'Descontos de Anuidade':
        janela1.hide()
        janela3 = calculodescontoanuidade.calcular()
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == "Voltar":
        janela1.un_hide()
        janela3.hide()
    if window == janela1 and event == 'Formatar Texto':
        janela1.hide()
        janela4 = capitalize.capitalizar()
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == "Voltar":
        janela1.un_hide()
        janela4.hide()
    if window == janela1 and event == 'Formatar CNAE':
        janela1.hide()
        janela5 = formatar_cnae.formata()
    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == "Voltar":
        janela1.un_hide()
        janela5.hide()
    

    # window.close()