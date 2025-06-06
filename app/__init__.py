from flask import Flask
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_mail import Mail

# bcrypt object
bcrypt = Bcrypt()
mail = Mail()


client = None
Users_first_collection = None

def create_app():
    app = Flask(__name__)
    # Secret Key
    app.secret_key = "$anika202!$#"
    load_dotenv()
    
    bcrypt.init_app(app)

    # Default Routes
    from .routes.default_routes import default_route
    app.register_blueprint(default_route)

    # User Routes
    from .routes.user_routes import user_route
    app.register_blueprint(user_route)

    # Category Routes
    from .routes.category_routes import category_route
    app.register_blueprint(category_route)
    
    # Admin Routes
    from .routes.admin_routes import admin_route
    app.register_blueprint(admin_route)
    
    # Cart Routes
    from .routes.cart_route import cart_route
    app.register_blueprint(cart_route)
    
    #Checkout route
    from .routes.checkout_routes import checkout_route
    app.register_blueprint(checkout_route)
    
    # orders route
    from .routes.orders_route import order_route
    app.register_blueprint(order_route)
    
    #stripe route
    from .routes.payment_routes import payment_route
    app.register_blueprint(payment_route)

    # sslcommerz route
    from .routes.ssl_commerz_routes import sslcommerz_route
    app.register_blueprint(sslcommerz_route)
    
    
    # Mail Configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # set in .env
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # set in .env
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')
    
    mail.init_app(app)
    return app