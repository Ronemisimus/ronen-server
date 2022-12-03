from flask import Flask
from .modules.calculate import calculate_endpoint 
from .modules.stack import stack_size_endpoint


def create_app():
    app = Flask(__name__)

    app.add_url_rule('/independent/calculate',view_func=calculate_endpoint,methods=['POST'])

    app.add_url_rule('/stack/size',view_func=stack_size_endpoint)
    
    return app