from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Quem pensa enriquece',
        'autor': 'Napoleon Hill'
    },
    {
        'id': 2,
        'titulo': 'O Manuscristo',
        'autor': 'Napoleon Hill'
    },
    {
        'id': 3,
        'titulo': 'Entendendo Algoritmo',
        'autor': 'Aditya Y. Bhargava'
    },
    {
        'id': 4,
        'titulo': 'Os Segredos da Mente Milionaria',
        'autor': 'T. Harv Eker'
    },
    {
        'id': 5,
        'titulo': 'Racionais Sobrevivendo no Inferno',
        'autor': 'Grupo Racionais'
    },
    {
        'id': 6,
        'titulo': 'O Milagre da Manhã',
        'autor': 'Hal Elrod'
    }               
]

# Consultar (todos)
#O '@app.route' especifica o endpoint onde sera chamado, 'methods' especifica o metodo aceito para esse endpoint que no caso sera somente para ler (GET) 
@app.route('/livros',methods=['GET'])  # Cada endpoint tem que ter uma função
# Função que ira ler todos os livros (GET)
def obter_livros():
    return jsonify(livros) #a função jsonify é para transformar a lista em um formato de JSON

# Consultar(id)
#Função para obter somente um registro em especifico pelo ID utilizando somente o metodo GET
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:  #Loop utilizando o for para obter somente o ID passado no parametro do .get
      if livro.get('id') == id:
            return jsonify(livro)
      
# Editar
#Função para editar um registro aceitando o metodo PUT
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id): #pegando o ID do registro q sera modificado
   livro_alterado = request.get_json() #Pegando o registro requisitado pelo usuario para API
   # Para isso precisamos de 2 coisas, o indice que o livro se encontra e o ID desse registro
   for indice,livro in enumerate(livros): #Loop utilizando enumerate para inumerar esse indice e saber qual registro de fato modificar
       if livro.get('id') == id: #Pega o ID requisitado, se esse ID existir na lista caira aqui
           livros[indice].update(livro_alterado) #Pega o registro do indice e atualiza 
           return jsonify(livros[indice])
       

# Criar
# Função para criar um novo registro utilizando somente o metodo POST
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json() #variavel pega a requisição do usuario e transforma em formato JSON       
    livros.append(novo_livro) #Append é utilizado para criar uma novo registro pela requisição

    return jsonify(livros)
# Excluir

app.run(port=5000,host='localhost',debug=True)