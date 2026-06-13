#BOJ10814
#안정정렬(stable_sort) -> 값이 같은 요소들의 상대적인 순서 정렬
#회원 정렬 -> 나이가 많은순 단, 나이 == -> 먼저 가입한 순

from merge_sort import merge_sort

n = int(input())
members = []
for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

sorted =[0] * n
merge_sort(members, 0, n - 1, sorted)

for m in members:
    print(f'{m[0]} {m[1]}')