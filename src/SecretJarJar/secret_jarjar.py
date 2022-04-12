from player import Player
from game_board import GameBoard


class SecretJarJar:
    """
    Class that will control the game Secret JarJar
    :param players: the players who are part of the game
    """
    def __init__(self, players):
        self.players = players
        self.roles = ['jedi', 'sith', 'jarjar']
        self.teams = ['jedi', 'sith']
        self.game_board = GameBoard(len(players))
