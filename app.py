import flask
import os
import waitress
app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!t'

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 5000))
     waitress.serve(app, port=port)
