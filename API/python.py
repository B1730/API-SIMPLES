from flask import Flask, jsonify, request


app = Flask(__name__) #Podemos dizer que estou ativando o flask
#Eu escolhi filmes.


filmes = [
    {
        "id": 1,
        "filme": 'A Era do Gelo 2',
        "diretores": 'Carlos Saldanha'
    },
    {
        "id": 2,
        "filme": 'Como Treinar Seu Dragão 1',
        "diretores": 'Chris Sanders e Dean DeBlois'
    },
    {
        "id": 3,
        "filme": 'Meu Malvado Favorito 1',
        "diretores": 'Pierre Coffin e Chris Renaud'
    },
]
@app.route('/filmes', methods = ['GET']) #O methods é para afirmar que essa função é GET.
def obter_filmes():
    return jsonify(filmes)
#Pesquisar o livro por id
@app.route('/filmes/<int:id>', methods = ['GET'])
def filme_id(id):
    for filme in filmes:
        if filme.get('id')==id:
            return jsonify(filme)
#Pra editar
@app.route('/filmes/<int:id>', methods=['PUT'] )
def editar_filme_por_id(id):
    filme_alterado = request.get_json()
    for indice,filme in enumerate(filmes):
        if filme.get('id')==id:
            filmes[indice].update(filme_alterado)
            return jsonify(filmes[indice])
#Criar um filmim
@app.route('/filmes', methods = ['POST'])
def adicionar_novo_filme():
    novo_filme = request.get_json()
    filmes.append(novo_filme)
    return jsonify(filmes)
#Excluir
@app.route('/filmes/<int:id>', methods=['DELETE'])
def excluir_filme(id):
    for indice, filme in enumerate(filmes):
        if filme.get('id') == id:
            del filmes[indice]
    return jsonify(filmes)

app.run(port=5000, host='localhost',debug=True)


