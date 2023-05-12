import csv
from queue import PriorityQueue


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


def build_graph(path):
    graph = {}
    try:
        with open(path, "r",encoding="utf8") as file:
            reader = csv.reader(file)
            next(reader) #skip header
            for row in reader:
                first_city, second_city, distance = row
                if first_city not in graph: #add city to graph
                    graph[first_city] = {}
                if second_city not in graph:
                    graph[second_city] = {}
                add_road(graph, first_city, second_city, int(distance)) #add distance btw cities
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found.")
    file.close()
    return graph

def add_road(graph, first_city, second_city, distance):
    graph[first_city][second_city] = distance
    graph[second_city][first_city] = distance
        

def uniform_cost_search(graph, start, end):
    distances = {city: float('inf') for city in graph}
    previous_city = {city: None for city in graph}
    distances[start] = 0

    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        current_distance, current_city = priority_queue.get()

        if current_city == end:
            path = []
            while current_city:
                path.insert(0, current_city)
                current_city = previous_city[current_city]
            return path, distances[end]

        for neighbor, distance in graph[current_city].items():
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_city[neighbor] = current_city
                priority_queue.put((new_distance, neighbor))
    
   
    raise CityNotFoundError()


def main():
    path = "C:\CSE\AI\Project-1\data\cities.csv"
    start = input("Enter the start city: ")
    end = input("Enter the target city: ")

    try:
        map = build_graph(path)
        shortest_path, distance = uniform_cost_search(map, start, end)
        print(f"{' -> '.join(shortest_path)}")
        print(f"distance: {distance}")
    except FileNotFoundError as e:
        print(str(e))
    except CityNotFoundError as e:
        print(str(e))


if __name__ == "__main__":
    main()
