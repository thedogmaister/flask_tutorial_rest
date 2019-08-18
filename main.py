from flask import Flask
from flask_restful import Resource, Api
from resources.personR import (
    RegisterPerson, 
    UpdatePerson, 
    GetPersonOne, 
    GetAllPerson, 
    DeactivePerson, 
    ActivePerson,
    GetOnlyActives
    )

app = Flask(__name__)
api = Api(app)

# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'root',
#     'db': 'myflask',
#     'host': '127.0.0.1',
#     'port': '5432'
# }

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://%(user)s:\ %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost/myflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE_EXCEPTIONS']=True

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(RegisterPerson, '/api/person/registerP')
api.add_resource(UpdatePerson, '/api/person/<int:id>')
api.add_resource(GetPersonOne, '/api/person/<int:id>')
api.add_resource(GetAllPerson, '/api/persons')
api.add_resource(DeactivePerson, '/api/person/<int:id>/deactive')
api.add_resource(ActivePerson, '/api/person/<int:id>/active')
api.add_resource(GetOnlyActives, '/api/persons/actives')

if __name__=='__main__':
	from db import db
	db.init_app(app)
	app.run(debug=True)