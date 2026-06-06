from collections import deque

N = int(input())
queue = deque()

# 1부터 N까지 카드 채우기
for i in range(1, N + 1):
    queue.append(i)

# 카드가 1개 남을 때까지 반복
while len(queue) > 1:
    # 1. 맨 위 카드를 그냥 꺼내서 바로 출력 (버리기)
    print(queue.popleft(), end=' ')
    
    # 2. 그다음 카드를 꺼내서 다시 뒤에 넣기 (옮기기)
    person = queue.popleft()
    queue.append(person)

# 마지막으로 남은 카드 한 장 출력
print(queue.popleft())