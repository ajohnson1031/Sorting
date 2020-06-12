# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    a, b = len( arrA ), len( arrB )
    merged_arr = []
    # TO-DO
    i = j = 0
    
    while i < a and j < b:
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1 
        
    while i < a:
        merged_arr.append(arrA[i])
        i += 1
    
    while j < b:
        merged_arr.append(arrB[j])
        j += 1
        
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    
    return merge(merge_sort(left), merge_sort(right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


arr = [3, 1, 2, 6, 5, 4]
print(merge_sort(arr))
