intergers = [2, 3, 4, 5, 7, 8, 9, 12, 14, 17, 23, 25, 27, 28, 33, 37]
target = 6
#target is the element that i am looking for, need to determent if it is in the list or not.

#binary search uses login time
# if you have a list of a billion entries, login of a billion is 30.
#it will take 30 operations to determin weather or not an element is on the list.


#iterative binary search
def binary_search_iterative(intergers, target):
    low = 0
    #lists the index of the first element
    high = len(intergers) - 1
    #the index of the last element in the list - 1

    while low <= high:
        mid = (low + high) // 2
        #middle element(num) of the intergers
        if target == intergers[mid]:
            return True
        elif target < intergers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

print(binary_search_iterative(intergers,target))