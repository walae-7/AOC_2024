import time

def get_coords(x, y):
    return x * 1024 + y

class Cell:
    def __init__(self, value, x, y):
        self.v = value  # ASCII value
        self.x = x
        self.y = y

def get_area(sol, spot, not_done, field, dirs):
    not_done.remove(spot)
    sol['area'] += 1
    
    for id, dir in enumerate(dirs, 1):
        neigh_coord = get_coords(spot.x + dir['x'], spot.y + dir['y'])
        neigh = field.get(neigh_coord, Cell(-1, 0, 0))
        
        if neigh.v == spot.v:
            if neigh in not_done:
                get_area(sol, neigh, not_done, field, dirs)
        else:
            sol['perim'] += 1
            k = f"{id} "
            if dir['x'] == 0:
                k += str(spot.y)
                v = spot.x
            else:
                k += str(spot.x)
                v = spot.y
                
            sol['perims'].setdefault(k, []).append(v)

def main():
    start_time = time.time()
    
    # Read input
    field = {}
    not_done = set()
    y = 1
    
    try:
        with open("data.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    for x, char in enumerate(line, 1):
                        cell = Cell(ord(char), x, y)
                        field[get_coords(x, y)] = cell
                        not_done.add(cell)
                y += 1
    except FileNotFoundError:
        print("File not found")
        return

    dirs = [
        {'x': 1, 'y': 0},
        {'x': -1, 'y': 0},
        {'x': 0, 'y': 1},
        {'x': 0, 'y': -1}
    ]

    p1 = 0
    p2 = 0

    while not_done:
        t = next(iter(not_done))
        sol = {'area': 0, 'perim': 0, 'perims': {}}
        get_area(sol, t, not_done, field, dirs)
        
        p1 += sol['area'] * sol['perim']
        
        p = sol['perim']
        for perims in sol['perims'].values():
            perims.sort()
            for i in range(len(perims) - 1):
                if perims[i] == perims[i + 1] - 1:
                    p -= 1
        
        p2 += sol['area'] * p

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    print(f"Time elapsed: {(time.time() - start_time) * 1000:.2f} ms")

if __name__ == "__main__":
    main()