import PySimpleGUI as sg
from PySimpleGUI import (
    Window, Button, Text, Image, Input,
)


def capitalizar():
   
    layout = [ [sg.Text('Cole o texto que deseja formatar'), sg.Multiline(size=(70,4), key='-IN-')], 
            [sg.Text('Resposta:', size=(24,1)), sg.Multiline("Texto formatado", size=(70,4), key='-OUTPUT-')],
            [sg.Button('Maiúsculo', mouseover_colors=('#f54242', "white"), size=(10, 1)), sg.Button('Minúsculo'),  sg.Button('Primeira Letra'), sg.Button('Justificar'), sg.Button("Voltar", button_color=('white', '#85ab82'))]
    ]
    window = sg.Window('Formatar texto', layout, size=(850,200), finalize=True) 
    
    while True: 
        event, values = window.read() 

        if event == "Maiúsculo":
            if values["-IN-"] == "":
                sg.popup("Cole um texto no campo indicado para formatá-lo.")
                continue
            else:
                if values["-IN-"]:
                    texto = values["-IN-"]
                    maisculo = texto.upper()
                    window['-OUTPUT-'].update(maisculo)
                    continue
        if event == "Minúsculo":
            if values["-IN-"] == "":
                sg.popup("Cole um texto no campo indicado para formatá-lo.")
                continue
            if type(values["-IN-"]) == int:
                sg.popup("Só é possível formatar textos.")
                continue
            else:
                if values["-IN-"]:
                    texto = values["-IN-"]
                    minusculo = texto.lower()
                    window['-OUTPUT-'].update(minusculo)
                    continue
        
        if event == "Primeira Letra":
            if values["-IN-"] == "":
                sg.popup("Cole um texto no campo indicado para formatá-lo.")
                continue
            if type(values["-IN-"]) == int:
                sg.popup("Só é possível formatar textos.")
                continue
            else:
                if values["-IN-"]:
                    texto = values["-IN-"]
                    minusculo = texto.lower()
                    primeira = minusculo.capitalize()
                    window['-OUTPUT-'].update(primeira)
                    continue
        if event == "Justificar":
            if values["-IN-"] == "":
                sg.popup("Cole um texto no campo indicado para formatá-lo.")
                continue
            if type(values["-IN-"]) == int:
                sg.popup("Só é possível formatar textos.")
                continue
            else:
                if values["-IN-"]:
                    texto = values["-IN-"]
                    texto2 = " "
                    for i in range(0,len(texto2)):
                        texto = texto.replace(texto2[i],"")
                    window['-OUTPUT-'].update(texto)
                    continue
            

        return window

