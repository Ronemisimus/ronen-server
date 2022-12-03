from .server import create_app
from waitress import serve

def start_server():
    app = create_app()
    port = 8496
    print('serving app on http://localhost:8496')
    serve(app,port=port)