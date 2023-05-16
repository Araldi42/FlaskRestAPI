from flask import Flask, jsonify, request, json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Matheus',
     'habilidades':['Python, SQL'],
     },
     {'nome':'Araldi',
      'habilidades':['Java, Python']}
]

@app.route('/dev/<int:id>',methods = ['GET','PUT','DELETE'])
def desenvolvedor(id):
    """
    nome do desenvolver
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

if __name__ == '__main__':
    app.run(debug=True)