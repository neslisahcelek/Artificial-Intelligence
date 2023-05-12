def main():
    file_path = input("Enter the path of the road map file: ")
    start = input("Enter the start city: ")
    end = input("Enter the target city: ")

    try:
        road_map = build_graph(file_path)
        shortest_path, distance = uniform_cost_search(road_map, start, end)
        print(f"The shortest path from {start} to {end} is: {' -> '.join(shortest_path)}")
        print(f"The distance is: {distance} units.")
    except FileNotFoundError as e:
        print(str(e))
    except CityNotFoundError as e:
        print(str(e))

# Implement main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    main()
