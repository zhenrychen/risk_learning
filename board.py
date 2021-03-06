import networkx as nx
import yaml
from player import Player


class Board:
    """
    Class that represents a board. Contains all available territories.
    """
    def __init__(self, board=None):
        self.graph = nx.Graph()  # Graph that holds territories and edges between them
        self.territories = {}  # Maps territory name to Territory

        if board is not None:
            self.parse_boardfile(board)

    def parse_boardfile(self, boardfile):
        """
        Loads in a territory YAML and saves it to local vars.
        :param boardfile: path to YAML file
        """
        with open(boardfile) as f:
            board = yaml.load(f)
            for continent_name, continent_dict in board['continents'].items():
                for country_name, country_dict in continent_dict.items():
                    self.territories[country_name] = Territory(country_name, continent_name, country_dict['neighbors'])

            for territory in self.territories.values():
                for neighbor in territory.neighbors:
                    self.graph.add_edge(territory, self.territories[neighbor])

    def draw(self):
        """
        Draws current graph
        """
        inv_dict = {v: k for k, v in self.territories.items()}
        layout = nx.kamada_kawai_layout(self.graph)
        nx.draw(self.graph, pos=layout, labels=inv_dict, with_labels=True)


class Territory:
    """
    Class representing a single territory.
    """
    def __init__(self, name, continent, neighbors=None):
        self.name = name
        self.neighbors = neighbors  # type: [Territory]
        self.continent = continent  # type: str
        self.num_armies = 0         # number of armies contained
        self.owner = None           # type: Player

    def add_armies(self, num_armies):
        """
        Adds armies to territories. Adding conditions should be checked here
        :param int num_armies: Armies to add

        :return int Num armies not added
        """
        self.num_armies = num_armies
        return 0

    def remove_armies(self, num_armies):
        """
        Removes armies from territories. Removal conditions should be checked here.
        :param Territory territory:
        :param int num_armies:

        :return int Num armies not removed
        """
        num_under_zero = self.num_armies - num_armies
        if num_under_zero > 0:
            self.num_armies -= num_armies
            return 0
        else:
            self.num_armies = 0
            return num_under_zero

