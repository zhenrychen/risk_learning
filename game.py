from board import Board, Territory
from player import Player
import math
from random import shuffle, randint
from enum import Enum, auto


class GameStates(Enum):
    ALLOT = auto()
    ATTACK = auto()
    FORTIFY = auto()


class Game:
    def __init__(self, board="boards/Mini.yaml", agents=None, num_armies=100, players=None):
        self.board = Board(board)
        # change this to instantiate real agents
        if players is None:
            self.players = [Player(), Player()]  # type: [Player]
        else:
            self.players = players
        self.num_armies = int(math.floor(num_armies/len(agents)))

        self.agent_to_territories = {}  # type: dict(Player, [Territory])

        # gameplay flags
        self.distributed = False

    def __distribute(self):
        """
        Distributes territories evenly and randomly amongst players
        """
        if not self.distributed:
            territories_list = self.board.territories.keys()
            shuffle(territories_list)
            territories_per_player = int(math.floor(len(territories_list) / len(self.players)))
            for player in self.players:
                for _ in range(territories_per_player):
                    territory = self.board.territories[territories_list.pop()]
                    territory.owner = player

    def __allot(self, player):
        """
        Gets allotment from player and allots as requested
        :param Player player:
        :return:
        """
        valid_allotments = [(territory, player.unallocated_armies)
                            for territory in self.agent_to_territories[player]]
        allotments = player.get_allotments(valid_allotments)
        for territory, num_armies in allotments:
            territory.add_armies(num_armies)

    def __attack(self, player):
        """
        Gets attacks from player and modifies board based on attacks
        :param Player player:
        :return:
        """
        # Player must have at least 2 armies in territory to attack
        valid_attacks = [(territory, neighbor) for territory in self.board.territories.values() for neighbor in
                         territory.neighbors if territory.num_armies >= 2]
        attacks = player.get_attacks(valid_attacks)
        for territory_from, territory_to in attacks:  # type: Territory, Territory
            num_attacking = min(territory_from.num_armies - 1, 3)  # Leave one army behind in home
            num_defending = min(min(territory_to.num_armies, 2), num_attacking)
            attacking_dice = sorted([randint(1, 6) for _ in range(num_attacking)], reverse=True)
            defending_dice = sorted([randint(1, 6) for _ in range(num_defending)], reverse=True)

            for i in range(num_defending):
                if attacking_dice[i] > defending_dice[i]:  # attacker is higher
                    territory_to.num_armies -= 1
                    # Check if territory is defeated
                    # If territory is defeated, switch owner,
                    if territory_to.num_armies <= 0:
                        territory_to.owner = player
                        territory_to.num_armies = num_attacking
                        territory_from.num_armies -= num_attacking
                else:
                    territory_from.num_armies -= 1

    def __fortify(self, player):
        """
        Gets fortifications from player and modifies board based on fortification
        :param Player player:
        :return:
        """
        valid_fortifications = [(t_from, t_to) for t_from in self.board.territories.values()
                                for t_to in self.board.territories.values() if t_from is not t_to]
        fortifications = player.get_fortifications(valid_fortifications)
        for territory_from, territory_to, num in fortifications:  # type: Territory, Territory, int
            territory_from -= num
            territory_to += num

    def __check_end(self):
        """
        Checks if game has ended
        :return:  if there is more than one player who is alive
        """
        return len([player for player in self.players if player.alive]) > 1

    def play_game(self):
        """
        Plays through game without pause or ability to manually step
        :return:
        """
        while not self.__check_end():
            self.__distribute()
            for player in self.players:
                self.__allot(player)
                self.__attack(player)
                self.__fortify(player)














