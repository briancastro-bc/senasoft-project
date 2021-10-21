from flask import json, request, make_response, jsonify
from flask.views import MethodView
from flask_socketio import rooms
from src.services.rooms_service import RoomsService
from src.namespaces import RoomNamespace

class RoomController(MethodView):

    rooms: dict = {}

    def __init__(self) -> None:
        self.room_service: RoomsService = RoomsService()    
    
    def get(self):
        if request.args.get("code") in RoomNamespace.rooms:
            response = make_response(jsonify({
                "statusCode": 200,
                # Mostrar código de la sala, usuarios asociados, Cartas secretas -> ID, Cartas, Cartas descubiertas, 
                "message": "Joining room"
            }), 200)
            return response
        response = make_response(jsonify({
            "error": True,
            "statusCode": 404,
            "message": "Room isn't found"
        }), 404)
        return response

    def post(self):
        if request.is_json:
            owner = request.json['owner']
            return self.room_service.create_room(owner)
        response = make_response(jsonify({
            "message": "Bad request. Please send a Json format",
            "statusCode": 400
        }), 400)
        return response