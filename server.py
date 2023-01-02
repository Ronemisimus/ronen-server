from flask import Flask
from calculate import calculate_endpoint 
from stack import stack_size_endpoint, stack_add_argument, stack_operate_endpoint, stack_delete_endpoint
from log_manager import logger_level_read_endpoint, logger_level_write_endpoint

def create_app():
    app = Flask(__name__)

    app.add_url_rule('/independent/calculate',view_func=calculate_endpoint,methods=['POST'])

    app.add_url_rule('/stack/size',view_func=stack_size_endpoint)

    app.add_url_rule('/stack/arguments',view_func=stack_add_argument, methods=['PUT'])

    app.add_url_rule('/stack/operate', view_func=stack_operate_endpoint)

    app.add_url_rule('/stack/arguments',view_func=stack_delete_endpoint, methods=['DELETE'])

    app.add_url_rule('/logs/level',view_func=logger_level_read_endpoint)

    app.add_url_rule('/logs/level',view_func=logger_level_write_endpoint, methods=['PUT'])
    
    return app