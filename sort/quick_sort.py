# 퀵 정렬
def quick_sort(A, left, right):
    if left < right:
        p = partition(A, left, right)
        quick_sort(A, left, p - 1 )
        quick_sort(A, p + 1, right)

def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right

    while low <= high:
        while A[low] < pivot:
            low += 1
        while A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

            low += 1
            high -= 1
        else:
            break
    
    A[left], A[high] = A[high], A[left]

    return high

input_data = input("숫자를 입력하세요: ").replace(',', ' ')
num_list = []
for x in input_data.split():
    number = int(x)
    num_list.append(number)

quick_sort(num_list, 0, len(num_list) - 1)
print(num_list)
