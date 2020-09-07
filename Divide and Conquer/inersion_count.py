def mergeSort(A, left, right):
    inv_count = 0
    if left < right:
        mid = (left+right)//2
        inv_count += mergeSort(A, left, mid)
        inv_count += mergeSort(A, mid+1, right)
        inv_count += merge(A, left, mid, right)
    return inv_count

def merge(A, left, mid, right):
    i = left
    j = mid+1
    k = left
    B = [0]*(right+1)
    inv_count = 0

    while i<=mid and j<=right:
        if A[i]<=A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            inv_count=inv_count+(mid-i + 1)
        k += 1

    while i <= mid:
        B[k] = A[i]
        i += 1
        k +=1

    while j <= right:
        B[k] = A[j]
        j += 1
        k += 1

    for i in range(left, right+1):
        A[i] = B[i]
    return inv_count

#Driver Code
A = [1, 20, 6, 4, 5] 
n = len(A) 
result = mergeSort(A, 0, n-1) 
print(result) 