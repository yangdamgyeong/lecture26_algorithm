from collections import deque
queue = deque()

N = int(input())
for _ in range(N):
    op_list = input().split()

    if op_list[0] == 'push':
        data = int(op_list[1])
        queue.append(data)
    elif op_list[0] == 'pop':
        if queue: 
            data = queue.popleft()
            print(data)
        # print
    elif op_list[0] == 'size':
        print(len(queue))
    elif op_list[0] == 'empty':
        if not queue:
            print(True)
        else:
            print(False)
    elif op_list[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
        #print(queue.[0] if queue else -1)
    elif op_list[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
        #print(queue.[0] if queue else -1)
 
