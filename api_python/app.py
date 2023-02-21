#Api - é um lugar de disponibilizar recursos e/ou funcionalidades. 
#Objetivo de criar uma Api que disponibiloza consulta, criação, edição e exclusão de livros. 
#URL - Localhost
#Recorsos - Livro
from flask import Flask, jsonify, request

app = Flask(__name__)

livros =[
    {
        'id': 1,
        'titulo': 'Simplesmente Mujica Um Livro Onde o Mito e o Homem São Revelados sem Censuras',
        'autor':  'Alfredo garcia'
    },
    {
        'id': 2,
        'titulo': 'Bob Dylan a voz de uma geração História Discografia Fotos e Documentos',
        'autor':  'Brian Southal'
    },
    {  
        'id': 3,
        'titulo': 'ACDC rock and roll ao máximo A história definitiva da maior banda de rock do mundo',
        'autor':  'Murray Engleheart e Arnaud Durieux'
    },
]
#Uma Api que nos permita, consultar todos livros, por id, editar e excluir.
@app.route('/livros')

def obter_livros():

    return jsonify(livros)

app.run(port=5000, host='localhost',debug=True)




