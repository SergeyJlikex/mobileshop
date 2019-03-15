from main import server

@server.route('/')
def index():
    return "Hello Sergey"
