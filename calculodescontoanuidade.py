import datetime
import PySimpleGUI as sg
from PySimpleGUI import (
    Window, Button, Text, Image, Input,
)

datalist = [];
data_datetime = datetime.date.today()
data = datetime.date.today()
ano = data.year
mes = data.month
dia = data.day

ano = str(ano)
mes = str(mes)
dia = str(dia)
ano_int = int(ano)
mes_int = int(mes)
dia_int = int(ano)

datalist.append(dia)
datalist.append(mes)
datalist.append(ano)

data = "".join(datalist)
data_int = int(data)

data_mes = data_datetime.strftime("%m")



def calcular():

    layout = [ [sg.Text('Informe a data de formação do profissional:'), sg.Input(key='-FORMACAO-')], 
            [sg.Text('Resposta:'), sg.Multiline("Desconto", size=(70,3), key='-OUTPUT-')],
             [sg.Button('Calcular', tooltip="Clique para calcular o desconto", mouseover_colors=('#f54242', "white"), size=(10, 1)), sg.Button('Voltar', button_color=('white', '#85ab82'))]
    ]
    window = sg.Window('Calcular desconto de anuidade', layout, finalize=True) 

    while True: 
        event, values = window.read()
        
        if event == "Calcular":
            if values["-FORMACAO-"] == "":
                sg.popup("Informe uma data")

            
            if values["-FORMACAO-"]:
                if len(values["-FORMACAO-"]) > 10:
                    sg.popup("Formato de data inválido. Preencha como XX/XX/XXXX ou XXXXXXXX")
                    continue
                if len(values["-FORMACAO-"]) < 8:
                    sg.popup("Formato de data inválido. Preencha como XX/XX/XXXX ou XXXXXXXX")
                    continue
                else:
                    dataformacao = values['-FORMACAO-']
                    dataformacao2 = "/"
                    for i in range(0,len(dataformacao2)):
                        dataformacao = dataformacao.replace(dataformacao2[i],"")
                    dataformacao_mes = dataformacao[3:4]
                    dataformacao_mes_int = int(dataformacao_mes)
                    if dataformacao_mes_int == 1:
                        dataformacao_mes = "janeiro"
                    elif dataformacao_mes_int == 2:
                        dataformacao_mes = "fevereiro"
                    elif dataformacao_mes_int == 3:
                        dataformacao_mes = "março"
                    elif dataformacao_mes_int == 4:
                        dataformacao_mes = "abril"
                    elif dataformacao_mes_int == 5:
                        dataformacao_mes = "maio"
                    elif dataformacao_mes_int == 6:
                        dataformacao_mes = "junho"
                    elif dataformacao_mes_int == 7:
                        dataformacao_mes = "julho"
                    elif dataformacao_mes_int == 8:
                        dataformacao_mes = "agosto"
                    elif dataformacao_mes_int == 9:
                        dataformacao_mes = "setembro"
                    elif dataformacao_mes_int == 10 or dataformacao_mes_int == 0:
                        dataformacao_mes = "outubro"
                    elif dataformacao_mes_int == 11:
                        dataformacao_mes = "novembro"
                    elif dataformacao_mes_int == 12:
                        dataformacao_mes = "dezembro"
                    dataformacao_ano = dataformacao[4:8]
                    dataformacao_ano_int = int(dataformacao[4:8])
                    dataformacao_int = int(dataformacao)
                    dataformacao_50_desc = dataformacao_ano_int + 2
                            ####desconto 50% ######
                    if ano_int - dataformacao_ano_int < 2 and dataformacao_ano_int < data_int:
                        values['-FORMACAO-'] = ""
                        window['-OUTPUT-'].update(values['-FORMACAO-'] + f"Profissional tem direito ao desconto de 50% até {dataformacao_mes} de {dataformacao_50_desc}.")
                            ##### desconto 30% ########
                    elif ano_int - dataformacao_ano_int == 3 and dataformacao_mes_int <= 6:
                        values['-FORMACAO-'] = ""
                        window['-OUTPUT-'].update(values['-FORMACAO-'] + f"Profissional possui desconto de 30% até {dataformacao_mes} de {ano}. Valor integral: R$634,04 Valor com desconto: R$443,82")
                    elif ano_int - dataformacao_ano_int == 3 and dataformacao_mes_int >= 6:
                        values['-FORMACAO-'] = ""
                        window['-OUTPUT-'].update(values['-FORMACAO-'] + f"Profissional não possui mais direito ao desconto de formação este ano. Terá direito ao desconto de 20% em {ano_int + 1}.")
                            ###### desconto 20% ######
                    elif ano_int - dataformacao_ano_int == 4 and dataformacao_mes_int <= 6:
                        values['-FORMACAO-'] = ""
                        window['-OUTPUT-'].update(values['-FORMACAO-'] + f"Profissional possui desconto de 20% até {dataformacao_mes} de {ano}. Valor integral: R$634,04 Valor com desconto: R$507,23")
                    elif ano_int - dataformacao_ano_int == 4 and dataformacao_mes_int >= 6:
                        values['-FORMACAO-'] = ""
                        window['-OUTPUT-'].update(values['-FORMACAO-'] + f"Profissional não possui mais direito ao desconto de formação este ano. Terá direito ao desconto de 10% em {ano_int + 1}.")
                                ###### desconto 10% ######
                    elif ano_int - dataformacao_ano_int == 5 and dataformacao_mes_int <= 6:
                        values['-FORMACAO-'] = ""
                        window['-OUTPUT-'].update(values['-FORMACAO-'] + f"Profissional possui desconto de 10% até {dataformacao_mes} de {ano}.Valor integral:    R$634,04 Valor com desconto: R$570,63")
                    elif ano_int - dataformacao_ano_int == 5 and dataformacao_mes_int >= 6:
                        values['-FORMACAO-'] = ""
                        window['-OUTPUT-'].update(values['-FORMACAO-'] + f"Profissional não possui mais direito aos descontos de formação este ano.")
                            ####### mais de 5 anos de formado ########
                    elif ano_int - dataformacao_ano_int > 5:
                        values['-FORMACAO-'] = ""
                        window['-OUTPUT-'].update(values['-FORMACAO-'] + f"Profissional não tem direito a descontos de formação pois está formado há {ano_int - dataformacao_ano_int} anos.")
                    continue

        return window       