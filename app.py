from flask import Flask, jsonify, request, json

app = Flask(__name__)

desenvolvedores = [
    {'id':'0',
     'nome':'Matheus',
     'habilidades':['Python, SQL'],
     },
     {'id':'1',
      'nome':'Araldi',
      'habilidades':['Java, Python']}
]


@app.route('/dev/<int:id>',methods = ['GET','PUT','DELETE'])
def desenvolvedor(id):
    """
    devolve um desenvolvedor pelo ID, também deleta ou altera um desenvolvedor.
    """
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de Id {} não existe'.format(id)
            response = {'status':'error','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = {'status':'error','mensagem':mensagem}
        return jsonify(response)
    
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso','mensagem':'Registro Excluído'})
@app.route('dev/',methods = ['POST', 'GET'])
def lista_desenvolvedores():
    """
    Lista todos os desenvolvedores e inclui um novo desenvolvedor.
    """
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados[id] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido!'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)