from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///shop.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    orders = relationship("Order", back_populates="product")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")

Base.metadata.create_all(engine)

existing_users = session.query(User).count()
existing_users = session.query(User).count()

if existing_users == 0:
    
    user1 = User(name="jamal", email="jamal@example.com")
    user2 = User(name="grant", email="grant@example.com")

    product1 = Product(name="Laptop", price=1000)
    product2 = Product(name="Smartphone", price=500)
    product3 = Product(name="Tablet", price=300)

    order1 = Order(user=user1, product=product1, quantity=1)
    order2 = Order(user=user1, product=product2, quantity=2)
    order3 = Order(user=user2, product=product2, quantity=1)
    order4 = Order(user=user2, product=product3, quantity=3)

    session.add_all([user1, user2, product1, product2, product3, order1, order2, order3, order4])
    session.commit()
    print("Data inserted successfully!")
else:
    print("Data already exists, skipping insertion.")

all_users = session.query(User).all()

print("All Users:")
print("-" * 50)
for user in all_users:
    print(f"ID: {user.id}")
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print(f"Number of orders: {len(user.orders)}")
    print("-" * 50)

all_products = session.query(Product).all()

print("All Products:")
print("-" * 50)
for product in all_products:
    print(f"ID: {product.id}")
    print(f"Name: {product.name}")
    print(f"Price: {product.price}")
    print(f"Number of orders: {len(product.orders)}")
    print("-" * 50)

all_orders = session.query(Order).all()

print("All Orders:")
print("-" * 50)
for order in all_orders:
    print(f"Order ID: {order.id}")
    print(f"User Name: {order.user.name}")
    print(f"Product Name: {order.product.name}")
    print(f"Quantity: {order.quantity}")
    print("-" * 50)

product_to_update = session.query(Product).filter_by(name="Laptop").first()
if product_to_update:
    product_to_update.price = 1200
    session.commit()
    print("Product price updated successfully!")
else:
    print("Product not found.")

user_to_delete = session.query(User).filter_by(id=1).first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print("User deleted successfully!")
else:
    print("User not found.")

