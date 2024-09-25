from flask import Blueprint, jsonify, request, make_response
from models.music_model import MusicModel
from enum import Enum
from bson import ObjectId

musics_controller = Blueprint("musics", __name__)

class HttpStatus(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_FOUND = 404


@musics_controller.route(
    "/", methods=["POST"]
)
def music_post():
    new_music = MusicModel(request.json)
    new_music.save()
    return make_response(
        jsonify(
        new_music.to_dict()
    ), HttpStatus.OK.value
    )


@musics_controller.route(
    "/random", methods=["GET"]
)
def music_random_get():
    random_music = MusicModel.get_random()
    if random_music is None:
        return make_response(
            jsonify({"error": "No music available"}),
            HttpStatus.NOT_FOUND.value
        )
    return make_response(
        jsonify(random_music.to_dict()),
        HttpStatus.OK.value
    )

@musics_controller.route(
    "/", methods=["GET"]
)
def get_all_musics():
    musics = MusicModel.find()
    return [music.to_dict() for music in musics]

@musics_controller.route(
    "/<id>", methods=["GET"]
)
def get_music(id: str):
    music = MusicModel.find_one({"_id": ObjectId(id)})
    if music is None:
        return make_response(
            jsonify({"error": "Music not found"}),
            HttpStatus.NOT_FOUND.value
        )
    return make_response(
        jsonify(music.to_dict()),
        HttpStatus.OK.value
    )