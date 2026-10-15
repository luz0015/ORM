from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Product<ID:{self.id}, Name:{self.name}, Price:{self.price}, Stock:{self.stock}>"

def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada")

def create_product(name, price, stock=0):
    with app.app_context():
        product = Product(name=name, price=price, stock=stock)
        db.session.add(product)
        db.session.commit()
        print(f"Producto creado: {product}")
        return product.id

def get_product(product_id):
    with app.app_context():
        product = db.session.get(Product, product_id)
        if product:
            print(f"Producto encontrado: {product}")
        else:
            print(f"No existe producto con id {product_id}")
        return product

def get_all_products():
    with app.app_context():
        products = Product.query.all()
        for p in products:
            print(p)
        return products

def update_product(product_id, name=None, price=None, stock=None):
    with app.app_context():
        product = db.session.get(Product, product_id)
        if not product:
            print(f"No existe producto con id {product_id}")
            return False

        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if stock is not None:
            product.stock = stock

        db.session.commit()
        print(f"Producto actualizado: {product}")
        return True

def delete_product(product_id):
    with app.app_context():
        product = db.session.get(Product, product_id)
        if not product:
            print(f"No existe producto con id {product_id}")
            return False

        db.session.delete(product)
        db.session.commit()
        print(f"Producto eliminado: id {product_id}")
        return True









if __name__ == '__main__':
    init_db()


    #INSERT
    
    #create_product("cursos python", 25.50, 50)
    #create_product("cursos java", 35.50, 40)
    #create_product("cursos c# ", 25.50,60)  

    
    get_all_products()

    get_product(1)  


    #update_product(1, price=50.80, stock=45)
    #update_product(3, price=65.20, stock=58)
    
    #delete_product(3)