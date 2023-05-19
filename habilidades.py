from flask_restful import Resource

lista_habiliades = ['Python', 'Java', 'Flask', 'PHP']
class Habilidades(Resource):
    def get(self):
        return lista_habiliades