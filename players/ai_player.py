from custom.rules import Rules
from players.player_types import PlayerType
from players.player import Player
import random

class AiPlayer(Player):
    def __init__(self, rules: Rules) -> None:
        super().__init__(rules)
        self.PLAYER_TYPE = PlayerType.AI
        
    def do_turn(self, coins: int = -1) -> int:
        return random.randint(self._rules.min_take, self._rules.max_take)
    