import random

def generate_map(m, n):
    if m < 5 or m > 20 or n < 5 or n > 20:
        raise ValueError("Map dimensions must be between 5 and 20")

    # รายชื่อตึก
    buildings = ['KP', 'TS', 'TC', 'TH', 'UR', 'LR', 'BH', 'CN']
    random.shuffle(buildings)

    # แบ่งทางเข้า: 12, 14 (ซ้ายมือ) / 10, 11, 13 (ขวามือ)
    left_entrances = [12, 14]
    right_entrances = [10, 11, 13]
    entrance_rows = random.sample(range(m), 5)
    entrance_map = {
        entrance_rows[i]: (left_entrances.pop() if i < 2 else right_entrances.pop(), 0 if i < 2 else -1)
        for i in range(5)
    }

    grid = [['' for _ in range(n)] for _ in range(m)]

    # เตรียมช่องว่างในเมือง
    city_cells = [(i, j) for i in range(m) for j in range(n)
                  if j != 0 and j != n - 1]  # หลีกเลี่ยง col 0 กับ -1
    random.shuffle(city_cells)

    # ใส่ตึกลงในแผนที่
    for b in buildings:
        i, j = city_cells.pop()
        grid[i][j] = b

    # ใส่เลขในเมือง (ยกเว้น 0 และ 10–14)
    for i in range(m):
        for j in range(n):
            if j == 0 or j == n - 1:
                grid[i][j] = 0  # default border
            elif grid[i][j] == '':
                while True:
                    val = random.randint(1, 1000)
                    if val not in range(10, 15):
                        grid[i][j] = val
                        break

    # ใส่ทางเข้า (10–14) ลงใน col 0 หรือ -1 ตามเงื่อนไข
    for row, (val, side) in entrance_map.items():
        grid[row][side] = val

    # ป้องกันไม่ให้เลข 10–14 โผล่ในเมือง
    for i in range(m):
        for j in range(n):
            if j != 0 and j != n - 1:
                if isinstance(grid[i][j], int) and grid[i][j] in range(10, 15):
                    while True:
                        val = random.randint(1, 1000)
                        if val not in range(10, 15):
                            grid[i][j] = val
                            break

    return grid

def print_map_with_metadata(m, n, grid):
    print(f"{m} x {n}")

    # ความกว้างตึก (สูงสุดต้องมากกว่าขนาดเมือง)
    building_width = random.randint(max(m, n) + 1, 2000)
    print(building_width)

    # เวลากำหนดตายตัว (t)
    t = random.randint(60, 5000)
    print(t)

    # เวลาเฉลี่ยระหว่างตึก
    avg = round(random.uniform(30, 100), 2)
    print(avg)

    for row in grid:
        print(' '.join(str(x).ljust(3) for x in row))

# ตัวอย่างการใช้
m, n = random.randint(5, 5), random.randint(5, 5)
g = generate_map(m, n)
print_map_with_metadata(m, n, g)
