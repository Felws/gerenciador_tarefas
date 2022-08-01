from msilib.schema import SelfReg
import PySimpleGUI as sg
from PySimpleGUI import (
    Window, Button, Text, Image, Input,
)


def executar():
   
    layout = [ [sg.Text('Informe o número do código de barras:'), sg.Input(key='-IN-')], 
            [sg.Text('Número do boleto:'), sg.Input('número do boleto', key='-OUTPUT-')],
            [sg.Button('Mostrar', tooltip="Clique para fechar o programa", mouseover_colors=('#f54242', "white"), size=(10, 1)), sg.Button('Voltar', button_color=('white', '#85ab82'))]
    ]
    window = sg.Window('Extrair número do boleto',layout, finalize=True) 
    
    while True: 
        event, values = window.read() 
        
        if event == 'Mostrar':
            if values["-IN-"] == "":
                sg.popup("Informe um número de código de barras")
                continue
            if len(values['-IN-']) < 29:
                    sg.popup("Informe um número de código de barras válido")
                    continue
            else:
                if values["-IN-"]:
                    codigo_barra = values["-IN-"]
                    codigo_barra2 = "."
                    for i in range(0,len(codigo_barra2)):
                        codigo_barra = codigo_barra.replace(codigo_barra2[i],"")
                        codigo_barra2 = " "
                        codigo_barra = codigo_barra.replace(codigo_barra2[i],"")
                        numero_boleto = codigo_barra[21:29]
                        window['-OUTPUT-'].update(numero_boleto)
                    continue
            

        return window