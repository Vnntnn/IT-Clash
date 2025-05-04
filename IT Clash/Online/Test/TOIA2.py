"""
20.08 - 21.10

toi a2-001, 002

หาจุดตัดระหว่างเส้น red กับ blue, หาขนาดเต้นที่ใหญ่ที่สุด

sol: find r, b intersect, find max in array or error if there's no camping

"""

def tangent():
    """Find intersect from 2 reflect lines"""

def camping():
    """002"""

    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    point_set = set(points)
    max_side = 0

    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]

            if abs(x1 - x2) == abs(y1 - y2) and x1 != x2 and y1 != y2:
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    max_side = max(max_side, abs(x1 - x2))

    print(max_side)

camping()
