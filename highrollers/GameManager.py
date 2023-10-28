from random import randrange

from django.http import JsonResponse

from .games.test.TestGame import TestGame
from .games.blackjack.BlackjackGame import BlackjackGame
from .games.BaseGame import BaseGame

from django.core.handlers.wsgi import WSGIRequest

class GameManager:
    def __init__(self) -> None:
        self.games:dict[str, BaseGame] = {}
        self.ID_LENGTH = 10
    
    def new_game(self, game: str):
        """ Register a new game with a unique id"""
        id = ""
        while True:
            id = self._generate_id()
            if id not in self.games.keys():
                break
        
        self.games[id] = self._create_game_by_name(game)
    
    def delete_game(self, id:str) -> BaseGame:
        return self.games.pop(id)
    
    def handle_client_message(self, request:WSGIRequest):
        """Send the client's message to the appropriate game"""
        message = request.GET.dict()
        print(message)
        response_message = ""
        if message["id"] in self.games.keys():
            if message["data"]:
                response_message = self.games[id].handle_client_message(message["data"])
            else:
                response_message = {"Error": "No data given!"}
        else:
            response_message = {"Error": "No game with given ID found!"}
        
        return JsonResponse(response_message)
    
    def _create_game_by_name(self, name: str) -> BaseGame:
        if name == "test":
            return TestGame(self)
        elif name == "blackjack":
            return BlackjackGame(self)
        
    def _generate_id(self) -> str:
        """Generates a random ID for a game"""
        out = ""
        for i in range(self.ID_LENGTH):
            out+=self._generate_id_char()
        return out
    
    def _generate_id_char(self) -> str:
        r = randrange(10+26*2) # 10 numbers, 26*2 letters
        if (r < 10): return ord(r+48)
        elif (r < 10+26): return ord(r+65)
        else: return ord(r+97)