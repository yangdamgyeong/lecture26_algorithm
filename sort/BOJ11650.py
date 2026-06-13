#BOJ 11650
from merge_sort import merge_sort

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

sorted_list = [0] * n
merge_sort(points, 0, n - 1, sorted_list)

for p in points:
    print(f"{p[0]} {p[1]}")