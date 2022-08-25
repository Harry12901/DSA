#SELECION SORT
#Time - O(n^2)
#Space - O(n), Auxilary - O(1)
arr = [4,5,2,1,6,9,0,8]
print(arr)
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return lst
