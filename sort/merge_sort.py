#병합 정렬

def merge_sort(A, left, right, sorted):
    if left < right:
        mid = (left + right) // 2 #몫만
        merge_sort(A, left, mid, sorted)
        merge_sort(A, mid+1, right, sorted)
        merge(A, left, mid, right, sorted)

def merge(A, left, mid, right, sorted):
    i = left
    j =mid + 1
    k = left

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            k, i = k+1, i+1
        else:
            sorted[k] = A[j]
            k, j = k+1, j+1
    
    if i > mid:
        sorted[k: k+right - j + 1] = A[j: right + 1]
    else:
        sorted[k: k + mid - i + 1] = A[i: mid + 1]
    A[left:right + 1] = sorted[left: right+ 1]


