#geradro de senhas. As senha de exemplo de conceito e foi 
#inserida apenas para mostrar o conceito. 
#Não recomendado para produção, é apenas aprendizado.

import sqlite3

MASTER_PASSWORD = "123456"

senha = input ("Insira sua senha master:  ")
if senha != MASTER_PASSWORD:
    print("Senha inválida! Encerrando...")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("******************************")
    print("* i : inserir nova senha     *")
    print("* l : listar serviços salvos *")
    print("* r : recuperar uma senha    *")
    print("* s : sair                   *")
    print("******************************")

def get_password(service):
    cursor.execute(f'''
    SELECT username, passwordr FROM users
    WHERE service = '{service}'
    ''')
    if cursor.rowcount == 0:
        print("Serviço não cadastrado (use 'l' para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)


def insert_passaword(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password) 
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT sevice FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)
        
    
while True:
    menu()
    op = input ("O que deseja fazer? ")
    if op not in ['l', 'i', 'r', 's']:
        print("Opção invalida!")
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome do usuário? ')
        password = input('Qual a senha? ')
        insert_passaword(service, username, password)

    if op == 'l':
        show_services()

    if op == 'r':
        service = input('Qual serviço que deseja a senha? ')
        get_password(service)
 
conn.close()