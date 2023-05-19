from flask import Flask, request
from flask_restful import Resource,Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':'0',
     'nome':'Matheus',
     'habilidades':['Python, SQL'],
     },
     {'id':'1',
      'nome':'Araldi',
      'habilidades':['Java, Python']}]


class Desenvolvedor(Resource):
    """
    devolve um desenvolvedor pelo ID, também deleta ou altera um desenvolvedor.
    """
    def get(self,id):
          
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de Id {} não existe'.format(id)
            response = {'status':'error','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = {'status':'error','mensagem':mensagem}
        return response
   
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
   
    def delete(self,id):
      desenvolvedores.pop(id)
      return {'status':'Sucesso','mensagem':'Registro Excluído'}

class listaDesenvolvedores(Resource):
    """
    Lista todos os desenvolvedores e inclui um novo desenvolvedor.
    """
    def get(self):
        return desenvolvedores
     



api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(listaDesenvolvedores, '/dev/')
if __name__ == '__main__':
    app.run(debug=True)