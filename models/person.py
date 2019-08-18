from db import db

class PersonModel(db.Model):
    __tablename__='person'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    apellido = db.Column(db.String(90))
    estado = db.Column(db.String(10))

    def __init__(self, nombre, apellido, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.estado = estado
    
    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'estado': self.estado
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_person(cls, id, data):
        person = cls.query.filter_by(id=id).first()
        person.nombre = data.nombre
        person.apellido = data.apellido
        db.session.commit()

    @classmethod
    def deactive_and_active_person(cls, id, estado):
        person = cls.query.filter_by(id=id).first()
        person.estado = estado
        db.session.commit()

    @classmethod
    def get_person(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_person(cls):
        return cls.query.all()
