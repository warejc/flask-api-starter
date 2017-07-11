from flask import Blueprint
from flask import request, jsonify
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_author import Author, AuthorSchema

picture_blueprint = Blueprint("picture", __name__, url_prefix='/picture')

@picture_blueprint.route('/', methods=['GET'])
def get_picture():
    picture = picture_service.get_picture()

    return jsonify({'picture': picture}), 200

