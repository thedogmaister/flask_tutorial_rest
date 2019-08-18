from main import app
from db import db

db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.before_first_request
def create_tables():
    print('hiss')
    db.create_all()
