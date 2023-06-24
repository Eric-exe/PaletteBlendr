"""The main flask app."""

from flask import Flask
from client.client import client_bp

app = Flask(__name__)

# register blueprints
app.register_blueprint(client_bp)

if __name__ == "__main__":
    app.run(debug=False, threaded=True)
