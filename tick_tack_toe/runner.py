from game import Game
from player import Player

x = Player("Anton", "human", "x")
o = Player("Antonio", "human", "o")
game = Game(x, o)
game.play()
