# Problem 2


def sort_array(arr):
    for i in range(len(arr)):
        min_ele = i
        for j in range(i+1, len(arr)):
            if arr[min_ele] > arr[j]:
                min_ele = j
        arr[i], arr[min_ele] = arr[min_ele], arr[i]
    return arr


# Main
ar_1 = [2, 8, 10]
ar_2 = [3, 5, 7]
for element in ar_2:
    ar_1.append(element)
sorted_array = sort_array(ar_1)
print(sorted_array)


