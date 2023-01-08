from server import create_app
from waitress import serve
import logging
import logging.config
import os

port = 9285

def start_server():
    if "logs" not in os.listdir(os.getcwd()):
        os.mkdir("logs")
    logging.config.fileConfig('logging.config',disable_existing_loggers=True)
    app = create_app()
    print(f'serving app on http://localhost:{port}')
    serve(app,port=port)


if __name__ == '__main__':
    start_server()