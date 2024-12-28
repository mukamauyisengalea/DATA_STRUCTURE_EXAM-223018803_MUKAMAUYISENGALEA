def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest][1] < arr[left][1]:
        largest = left
    if right < n and arr[largest][1] < arr[right][1]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Example usage
reservations = [("User1", 2), ("User2", 1), ("User3", 3)]
heap_sort(reservations)
print("Sorted by priority:")
for user, priority in reservations:
    print(f"{user} with priority {priority}")