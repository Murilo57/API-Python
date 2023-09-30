from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Quem pensa enriquece',
        'auto': 'Napoleon Hill'
    },
    {
        'id': 2,
        'titulo': 'O Manuscristo',
        'auto': 'Napoleon Hill'
    },
    {
        'id': 3,
        'titulo': 'Entendendo Algoritmo',
        'auto': 'Aditya Y. Bhargava'
    },
    {
        'id': 4,
        'titulo': 'Os Segredos da Mente Milionaria',
        'auto': 'T. Harv Eker'
    },
    {
        'id': 5,
        'titulo': 'Racionais Sobrevivendo no Inferno',
        'auto': 'Grupo Racionais'
    },
    {
        'id': 6,
        'titulo': 'O Milagre da Manhã',
        'auto': 'Hal Elrod'
    }               
]

# Consultar (todos)
# Cada endpoint tem que ter uma função
@app.route('/livros') #O '@app.route' especifica o endpoint onde sera chamado 
# Função que ira ler todos os livros (GET)
def obter_livros():
    return jsonify(livros) #a função jsonify é para transformar a lista em um formato de JSON

# Consultar(id)
# Editar
# Excluir

app.run(port=5000,host='localhost/livros',debug=True)