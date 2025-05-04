def main():
    m, n = map(int, input().split(" x "))
    building_width = int(input())
    t_limit = int(input())
    avg = float(input())
    map_data = [input().split() for _ in range(m)]

    best_entry, best_exit, best_time, best_path, first_found, last_found, special_path_coords = find_best_path(m, n, map_data, building_width, avg, t_limit)
    output = create_output(best_entry, best_exit, first_found, last_found, best_path, best_time, t_limit, map_data, special_path_coords)

    for i in output:
        print(i)

def find_best_path(m, n, map_data, building_width, avg, t_limit):
    special_buildings = ['KP', 'TS', 'TC', 'TH', 'UR', 'LR', 'BH', 'CN']
    entry_points = ['10', '11', '12', '13', '14']
    exit_points = ['10', '11', '12', '13', '14']

    entry_coords, exit_coords, special_coords = [], [], {}

    for i in range(m):
        for j in range(n):
            cell = map_data[i][j]
            if cell in entry_points:
                if j == 0:
                    entry_coords.append((i, j, cell))
                elif j == n - 1 and cell in exit_points:
                    exit_coords.append((i, j, cell))

            elif cell in special_buildings:
                special_coords[cell] = (i, j)

    # Sort entry_coords by the entry value (smallest first) and exit_coords similarly
    entry_coords = sorted(entry_coords, key=lambda x: int(x[2]))  # Sort by entry number (ascending)
    exit_coords = sorted(exit_coords, key=lambda x: int(x[2]))  # Sort by exit number (ascending)

    best_time = float('inf')
    best_path = []
    best_entry = None
    best_exit = None
    first_found = ""
    last_found = ""
    best_special_path_coords = []

    memo = {}

    def dfs(x, y, visited_special, path, time_spent, special_path_coords):
        nonlocal best_time, best_path, best_entry, best_exit, first_found, last_found, best_special_path_coords

        cell = map_data[x][y]
        key_special = '-'.join(sorted(visited_special))
        memo_key = (x, y, key_special)

        if memo_key in memo and memo[memo_key] <= time_spent:
            return
        memo[memo_key] = time_spent

        if cell in special_buildings and cell not in visited_special:
            visited_special = visited_special + [cell]
            special_path_coords = special_path_coords + [(x, y)]
            if len(visited_special) == 1:
                first_found = cell  # Set the first found building
            elif len(visited_special) == 8:
                last_found = cell  # Set the last found building

        path = path + [(x, y)]

        if len(visited_special) == 8:
            if (x, y) in [(ex_x, ex_y) for ex_x, ex_y, _ in exit_coords]:
                candidates_exit = [(int(ex_val), ex_val) for ex_x, ex_y, ex_val in exit_coords if (x, y) == (ex_x, ex_y)]
                if candidates_exit:
                    candidates_exit.sort()  # Sort exits by value
                    ex_val = candidates_exit[0][1]
                    if time_spent < best_time or (time_spent == best_time and int(ex_val) < int(best_exit or 100)):
                        best_time = time_spent
                        best_path = path
                        best_exit = ex_val
                        best_entry = map_data[path[0][0]][path[0][1]]
                        best_special_path_coords = special_path_coords

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        candidates = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and map_data[nx][ny] != '0' and (nx, ny) not in path:
                next_cell = map_data[nx][ny]
                if next_cell in special_buildings:
                    t_walk = avg * building_width  # Walking time
                    t_bonus = avg * 7.7 if next_cell not in visited_special else 0  # Bonus time for first encounter
                else:
                    t_walk = float(next_cell)
                    t_bonus = 0

                new_time = time_spent + t_walk + t_bonus

                if new_time > best_time:
                    continue

                candidates.append((new_time, special_buildings.index(next_cell) if next_cell in special_buildings else 100, nx, ny, t_walk + t_bonus, next_cell))

        # Sort candidates by time and special building index (if applicable)
        candidates.sort(key=lambda x: (x[0], x[1]))  # Sort by time and special building index

        for _, _, nx, ny, t, next_cell in candidates:
            dfs(nx, ny, visited_special, path, time_spent + t, special_path_coords)

    found_complete_path = False

    for i, j, _ in entry_coords:
        if found_complete_path:
            break
        dfs(i, j, [], [], 0, [])

        if best_path and len(best_special_path_coords) == 8:
            found_complete_path = True

    return best_entry, best_exit, best_time, best_path, first_found, last_found, best_special_path_coords

def create_output(best_entry, best_exit, first_found, last_found, best_path, best_time, t_limit, map_data, special_path_coords):
    output = []
    output.append(f"Best entry: {best_entry}")
    output.append(f"Best exit: {best_exit}")
    output.append(f"First found: {first_found}")
    output.append(f"Last Found: {last_found}")
    output.append("All found: " + " -> ".join([f"({x},{y})" for x, y in special_path_coords]))
    node_path = [map_data[x][y] for x, y in best_path]
    output.append("Path: " + " -> ".join(node_path))

    if best_time <= t_limit:
        hours = int(best_time) // 60
        minutes = int(best_time) % 60
        output.append(f"Time estimated: {hours}:{minutes:02d}")
    else:
        output.append("You're fired.")
    return output

main()
