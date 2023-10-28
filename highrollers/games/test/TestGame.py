from ..BaseGame import BaseGame

class TestGame(BaseGame):
    def __init__(self, manager) -> None:
        super().__init__(manager)

    def handle_client_message(self, message):
        return {"data":message}