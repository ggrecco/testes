from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ggrecco/Documentos/python/testes/flask/admin.db'
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)

admin = Admin(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


class Teste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teste = db.Column(db.String(30))
    email = db.Column(db.String(30))


admin.add_view(ModelView(Person, db.session))
admin.add_view(ModelView(Teste, db.session))

if __name__ == '__main__':
    app.run(debug=True)
