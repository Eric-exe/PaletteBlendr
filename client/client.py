"""The main entry point for the client application."""

from flask import Blueprint, render_template

client_bp = Blueprint("client", __name__)

client_bp.static_folder = "static"
client_bp.template_folder = "templates"

@client_bp.route('/')
def index():
    """The main page of the client application."""
    return render_template('index.html')

@client_bp.route('/styles.css')
def styles():
    """The CSS styles for the client application."""
    return client_bp.send_static_file('styles.css')

@client_bp.route('/script.js')
def script():
    """The JavaScript for the client application."""
    return client_bp.send_static_file('script.js')

@client_bp.route('/pickr.js')
def pickr():
    """The JavaScript for the color picker."""
    return client_bp.send_static_file('pickr.js')
