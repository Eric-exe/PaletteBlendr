"""The main API for the flask project."""

from flask import Blueprint, request

api_bp = Blueprint("api", __name__)

@api_bp.route('/color_lerp', methods=['POST'])
def color_lerp():
    """The color lerp API."""
    data = request.json

    colors = data['colors']

    return colors
