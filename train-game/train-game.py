import csv
import random

STARTING_TRAIN_COUNT = 45
TOTAL_COLOR_CARDS = {
    'green': 12,
    'pink': 12,
    'blue': 12,
    'white': 12,
    'yellow': 12,
    'orange': 12,
    'black': 12,
    'red': 12,
    'multicolor': 14
}

CITIES = ['Atlanta', 'Boston', 'Calgary', 'Charleston', 'Chicago', 'Dallas', 
              'Denver', 'Duluth', 'El Paso', 'Helena', 'Houston', 'Kansas City', 
              'Las Vegas', 'Little Rock', 'Los Angeles', 'Miami', 'Montreal', 'Nashville', 
              'New Orleans', 'New York', 'Oklahoma City', 'Omaha', 'Phoenix', 'Pittsburgh', 
              'Portland', 'Raleigh', 'Saint Louis', 'Salt Lake City', 'San Francisco', 'Santa Fe', 
              'Sault St Marie', 'Seattle', 'Toronto', 'Vancouver', 'Washington', 'Winnipeg']

COLORS = ['na', 'green', 'pink', 'blue', 'white', 'yellow', 'orange', 'black', 'red']
TRAIN_COLORS = ['blue', 'green', 'red', 'yellow', 'black']

ROUTE_SIZE_POINTS = {
    1: 1,
    2: 2,
    3: 4,
    4: 7,
    5: 10,
    6: 15
}

class Path:
    def __init__(self, path_id, start_city, end_city, distance, color, path_owner=None):
        self.path_id = path_id
        self.start_city = start_city
        self.end_city = end_city
        self.distance = distance
        self.color = color
        self.path_owner = path_owner

class Route:
    def __init__(self, point_a, point_b, distance, achieved_by=None):
        self.point_a = point_a
        self.point_b = point_b
        self.distance = distance
        self.achieved_by = achieved_by

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.train_count = STARTING_TRAIN_COUNT
        self.color_cards = {color: 0 for color in COLORS}
        self.routes = []
        self.score = 0

class Card:
    def __init__(self, color):
        self.color = color

class Deck:
    def __init__(self):
        self.cards = []
        for color, count in TOTAL_COLOR_CARDS.items():
            self.cards.extend([Card(color) for _ in range(count)])
    def shuffle(self):
        random.shuffle(self.cards)


def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(Path(*row))
    return data

def setup():
    connections_path = 'train-game/connections.csv'
    routes_path = 'train-game/routes.csv'

    connections_data = []
    routes_data = []

    with open(connections_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            connections_data.append(Path(*row))

    with open(routes_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            routes_data.append(Route(*row))

    return connections_data, routes_data

def can_claim_path(player, path):
    if path.path_owner is not None:
        return False
    if player.train_count < int(path.distance):
        return False
    if player.color_cards[path.color] < int(path.distance):
        return False
    return True

def main(player_count, player_names, color_order): 
    players = [Player(name, color) for name, color in zip(player_names, color_order)]
    paths, routes = setup()
    dist_matrix = [[0 for _ in range(len(CITIES))] for _ in range(len(CITIES))]

    for path in paths:
        start_index = CITIES.index(path.start_city)
        end_index = CITIES.index(path.end_city)
        dist_matrix[start_index][end_index] = int(path.distance)
        dist_matrix[end_index][start_index] = int(path.distance)

    deck = Deck()
    deck.shuffle()
    draw_set = deck.cards[:5]

if __name__ == "__main__":
    main(2, ['Alice', 'Bob'], ['blue', 'red'])