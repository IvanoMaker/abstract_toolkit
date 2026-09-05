import csv

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

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(Path(*row))
    return data

if __name__ == "__main__":
    connections_path = 'train-game/connections.csv'
    routes_path = 'train-game/routes.csv'
    paths = read_csv(connections_path)
    routes = read_csv(routes_path)

    cities = ['Atlanta', 'Boston', 'Calgary', 'Charleston', 'Chicago', 'Dallas', 
              'Denver', 'Duluth', 'El Paso', 'Helena', 'Houston', 'Kansas City', 
              'Las Vegas', 'Little Rock', 'Los Angeles', 'Miami', 'Montreal', 'Nashville', 
              'New Orleans', 'New York', 'Oklahoma City', 'Omaha', 'Phoenix', 'Pittsburgh', 
              'Portland', 'Raleigh', 'Saint Louis', 'Salt Lake City', 'San Francisco', 'Santa Fe', 
              'Sault St Marie', 'Seattle', 'Toronto', 'Vancouver', 'Washington', 'Winnipeg']

    colors = ['na', 'green', 'pink', 'blue', 'white', 'yellow', 'orange', 'black', 'red']

    dist_matrix = [[0 for _ in range(len(cities))] for _ in range(len(cities))]

    for path in paths:
        start_index = cities.index(path.start_city)
        end_index = cities.index(path.end_city)
        dist_matrix[start_index][end_index] = int(path.distance)
        dist_matrix[end_index][start_index] = int(path.distance)
            
    print("Distance Matrix:")
    for row in dist_matrix:
        print(row)