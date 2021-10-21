from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models import Model
from src.services.cards_services import Cards

class CardsController(MethodView):

    def __init__(self):
        self.cards = Cards()

    def get(self):
        return self.cards.serve_cards()

    def post(self):
        user_id = request.json["user_id"]
        dev_card = request.json["dev_card"]
        mod_card = request.json["mod_card"]
        error_card = request.json["error_card"]
        
        return self.cards.question(None, user_id, dev_card, mod_card, error_card, "A")