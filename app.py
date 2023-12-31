"""The main flask app."""

from flask import Flask
from client.client import client_bp
from api.api import api_bp

app = Flask(__name__)

# register blueprints
app.register_blueprint(client_bp)
app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=False, threaded=True)
