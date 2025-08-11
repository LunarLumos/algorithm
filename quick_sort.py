def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

nums = input("Enter numbers separated by space: ").split()
nums = [int(n) for n in nums]

sorted_nums = quick_sort(nums)
print("Sorted:", sorted_nums)
