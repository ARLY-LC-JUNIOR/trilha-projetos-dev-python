import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key = 'usuário')],
    [sg.Text('Senha')],
    [sg.Input(key = 'senha')],
    [sg.Button('login')],
    [sg.Text('', key = 'mensagem')],  
]

window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = '654321'
        usuario_correto = 'alcjunior'
        usuário = values = ['usuário']
        senha = values = ['senha']
        if senha == senha_correta and usuário == usuario_correto:
            window['mensagem'].update('Login realizado com sucesso')
        else: 
             window['mensagem'].update('Senha ou usário incorretos')


           
           


