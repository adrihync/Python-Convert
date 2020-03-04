def bubble_sort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True
    return A

print('hello word')
L = [2, 4, 5, 7, 1, 0, -12]
print(bubble_sort(L))