from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"User<Name:{self.name}, Email: {self.email}>"


def init_db():
    with app.app_context():
        db.create_all()
        print("base de datos creada")




def insert_users():
    with app.app_context():
        user1=User(name="alan brito",
        email="alan@mail.com")
        user2=User(name="sacria flores",
        email="flores@mail.com" )      
        user3=User(name="elsa",
        email="elsa@mail.com")

        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)

        db.session.commit()
        print("usuarios insertados")
if __name__ == '__main__':
   # init_db()
   insert_users()