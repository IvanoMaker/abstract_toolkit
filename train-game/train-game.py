import csv

class Route:
    def __init__(self, route_id, start_city, end_city, distance, color):
        self.route_id = route_id
        self.start_city = start_city
        self.end_city = end_city
        self.distance = distance
        self.color = color

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(Route(*row))
    return data

if __name__ == "__main__":
    file_path = 'train-game/routes.csv'
    routes = read_csv(file_path)

    cities = set()
    colors = set()

    for route in routes:
        print(route.__dict__)
        cities.add(route.start_city)
        cities.add(route.end_city)
        colors.add(route.color)

    print("Cities:", cities)
    print("Colors:", colors)