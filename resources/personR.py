from models.person import PersonModel
from flask_restful import Resource, reqparse

_person_parse = reqparse.RequestParser()
_person_parse.add_argument('nombre',
    type= str,
    required= False,
)
_person_parse.add_argument('apellido',
    type= str,
    required= False,
)

_person_parse.add_argument('estado',
    type= str,
    required= False,    
)

class RegisterPerson(Resource):
    def post(self):
        data = _person_parse.parse_args()
        person = PersonModel(**data)
        person.estado = 'ACTIVO'
        person.save_to_db()
        try:
            person.save_to_db()
            return {'message': 'user created'}, 201
        except:
            return {"message":"Ocurrio un error al ingresar un dato a la base de datos."}, 500

class UpdatePerson(Resource):
    def put(cls, id):
        data =_person_parse.parse_args()
        person = PersonModel(**data)
        try:
            person.update_person(id, person)
            return{'message' : 'user updated'}, 202
        except:
            return {"message":"Ocurrio un error al ingresar un dato a la base de datos."}, 500

class DeactivePerson(Resource):
    def put(cls, id):
        data = PersonModel.get_person(id)
        if data.estado == 'ACTIVO':
            PersonModel.deactive_and_active_person(id, 'DESACTIVO')
            return {'message': 'person deactived'}, 202
        else:
            return {'message': 'person already deactived'}, 500

class ActivePerson(Resource):
    def put(cls, id):
        data = PersonModel.get_person(id)
        if data.estado =='DESACTIVO':
            PersonModel.deactive_and_active_person(id, 'ACTIVO')
            return {'message': 'person actived'}, 202
        else:
            return {'message': 'person already actived'}, 500


class GetPersonOne(Resource):
    def get(cls, id):
        person = PersonModel.get_person(id)
        if not person:
            return {'message': 'person whit id: {} not exist'.format(id)}
        return person.json()

class GetAllPerson(Resource):
    def get(self):
        person = PersonModel.get_all_person()
        persons = [x.json() for x in person]
        return {'values:': persons}

class GetOnlyActives(Resource):
    def get(self):
        person = PersonModel.get_all_person()
        persons = [x.json() for x in person if x.estado != 'DESACTIVO']
        return {'values': persons}

        