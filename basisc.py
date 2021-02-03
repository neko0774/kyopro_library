def binary_search(sorted_array, index):#二分探索
    bottom, top = 0, len(sorted_array)+1
    while top > bottom+1:
        mid = (bottom+top)//2
        if sorted_array[mid] == index:
            return mid
        elif sorted_array[mid] > index:
            top = mid
        else:
            bottom = mid

