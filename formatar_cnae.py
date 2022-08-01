import PySimpleGUI as sg
from PySimpleGUI import (
    Window, Button, Text, Image, Input,
)


def formata():
   
    layout = [ [sg.Text('Informe o código do CNAE:'), sg.Input(key='-IN-')], 
            [sg.Text('Código Formatado:'), sg.Input('Código', key='-OUTPUT-')],
            [sg.Button('Formatar', mouseover_colors=('#f54242', "white"), size=(10, 1)), sg.Button('Voltar', button_color=('white', '#85ab82'))]
    ]
    window = sg.Window('Formatar Código CNAE',layout, finalize=True) 
    
    while True: 
        event, values = window.read() 
        
        if event == 'Formatar':
            if values["-IN-"] == "":
                sg.popup("Informe um código CNAE")
                continue
            # if len(values['-IN-']) < 29:
            #         sg.popup("Informe um número de código de barras válido")
            #         continue
            else:
                if values["-IN-"]:
                    codigo_cnae = values["-IN-"]
                    codigo_cnae2 = "."
                    for i in range(0,len(codigo_cnae2)):
                        codigo_cnae = codigo_cnae.replace(codigo_cnae2[i],"")
                    novo_codigo = codigo_cnae
                    codigo_cnae2 = novo_codigo[:6] + '/' + novo_codigo[7:]
                    print(codigo_cnae2)
                    window['-OUTPUT-'].update(codigo_cnae2)
                    continue
            

        return window
