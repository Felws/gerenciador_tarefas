import PySimpleGUI as sg
from PySimpleGUI import (
    Window, Button, Text, Image, Input,
)


def executar():
   
    layout = [ [sg.Text('Informe o número do código de barras:',visible=False, grab=True,key="-TEXT-"), sg.Input(key='-IN-')], 
            [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'), sg.Button('Test Progress bar')],
            [sg.Button('Mostrar', tooltip="Clique para fechar o programa", mouseover_colors=('#f54242', "white"), size=(10, 1), button_color=('white', '#85ab82')), sg.Button('Voltar')]
    ]

    window = sg.Window(" ", layout, finalize=True) 
    
    while True: 
        event, values = window.read() 

        if event == "Mostrar":
            window['-TEXT-'].update(window['-TEXT-'].visible)
        
            

        return window

executar()

projeto = "Projeto"
execucao = "Execução"
gestao = "Gestão"
meioambiente = "Meio Ambiente"
especiais = "Atividades Especiais"
ensino = "Ensino"
seguranca = "Segurança do Trabalho"
sim = True
nao = False
datatermino2 = []

def extemporaneo():
    atividade = int(input('Informe o número do grupo de atividades deste RRT \n Projeto (1)\n Execução (2)\n Gestão (3)\n Meio Ambiente (4)\n Atividades Especiais (5)\n Ensino (6)\n Segurança do Trabalho (7):\n'))
     ####Outras atividades #######
    if atividade == 3 or atividade == 7:
      atividade2 = str(input("O RRT tem as seguintes atividades? \n 3.1.Coordenação e compatibilização de projetos,\n 8.12.Projetos de Sistema de Segurança\n 7.8.13.Projeto de Proteção Contra Incêndios?\n [sim(s) ou não(n)]\n"))
      datacadastro = str(input("Em que data este RRT foi cadastrado?\n"))
      datacadastro2 = "/"
      for i in range(0,len(datacadastro2)):
        datacadastro = datacadastro.replace(datacadastro2[i],"")
        datacadastro = int(datacadastro)
      ######### Bloco Projeto #########
      if atividade2 == "sim" or atividade2 == "s":
        datatermino = str(input("Qual a data de término deste RRT?\n"));
        datatermino2 = "/"
        for i in range(0,len(datacadastro2)):
          datatermino = datatermino.replace(datatermino2[i],"")
          datatermino = int(datatermino)
        if datatermino > datacadastro:
          print('EXTEMPORÂNEO, pois para as atividades 3.1.Coordenação e compatibilização de projetos, 8.12.Projetos de Sistema de Segurança 7.8.13.Projeto de Proteção Contra Incêndios, o RRT deve ser cadastrado antes da data de término.')
        else:
          print("Não é extemporâneo pelas datas, pois foi cadastrado antes da data de término, mas é extemporâneo se ele não foi cadastrado antes de uma destas situações:\n a) até entrega final dos documentos técnicos, objeto do contrato, ao contratante;\n \n b) antes de dar entrada e/ou protocolar em pessoa jurídica, pública ou privada, responsável pela análise e aprovação do projeto e/ou documento técnico, objeto do contrato;\n c) antes da publicação ou divulgação dos documentos técnicos, objeto do contrato, em elementos de comunicação dirigido ao cliente e ao público em geral;")
      elif atividade2 == "nao" or atividade2 == "não" or atividade2 == "n":
        datainicio = str(input("Qual a data de início deste RRT?\n"));
        datainicio2 = "/"
        for i in range(0,len(datainicio2)):
          datainicio = datainicio.replace(datainicio2[i],"")
          datainicio = int(datainicio)
        if (datainicio - datacadastro) < 30:
          print("Não é extemporâneo, pois o RRT foi cadastrado até 30 dias contados a partir da sua data de início.")
      else: 
        print("Esta opção não é válida. Digite 'sim' ou 'não'.")
    #####atribuição das atividades #######
    if atividade == 1:
        atividade = projeto;
    elif atividade == 2:
        atividade = execucao;
    elif atividade == 3:
        atividade = gestao;
    elif atividade == 4:
        atividade = meioambiente;
    elif atividade == 5:
        atividade = especiais;
    elif atividade == 6:
        atividade = ensino;
    elif atividade == 7:
        atividade = seguranca;
  ### Atividade Projeto ou Meio Ambiente #######
    if atividade == 1 or atividade == 4:
      datacadastro = str(input("Em que data este RRT foi cadastrado?\n"))
      datatermino = str(input("Qual a data de término deste RRT?\n"));
      if datatermino > datacadastro:
        print('EXTEMPORÂNEO, pois para a a atividade de', atividade,'o RRT deve ser cadastrado antes da sua data de término.')
      else:
            print("Não é extemporâneo pelas datas, pois foi cadastrado antes da data de término, mas é extemporâneo se ele não foi cadastrado antes de uma destas situações:\n a) até entrega final dos documentos técnicos, objeto do contrato, ao contratante;\n \n b) antes de dar entrada e/ou protocolar em pessoa jurídica, pública ou privada, responsável pela análise e aprovação do projeto e/ou documento técnico, objeto do contrato;\n c) antes da publicação ou divulgação dos documentos técnicos, objeto do contrato, em elementos de comunicação dirigido ao cliente e ao público em geral;")
    ###### Execução ########
    if atividade == 2:
      datainicio = str(input("Qual a data de início deste RRT?\n"));
      if datainicio < datacadastro:
        print("Extemporâneo, pois o RRT de execução deve ser cadastrado antes da data de início")
      else:
        print("Não é extemporâneo, pois foi cadastrado antes da data de início.")
    # else:
    #   datainicio = str(input("Qual a data de término deste RRT?\n"));
    #   if (datainicio - datacadastro) < 30:
    #     print("Não é extemporâneo, pois o RRT foi cadastrado até 30 dias contados a partir da sua data de início.")