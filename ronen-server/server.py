from flask import Flask
from .modules.calculate import calculate_endpoint 



def create_app():
    app = Flask(__name__)

    app.add_url_rule('/independent/calculate',view_func=calculate_endpoint,methods=['POST'])
    
    return app