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
def selection_sort(lst):
    i = 0
    while(i<len(lst)-1):
        mini = i
        j = i+1
        while(j<len(lst)):
            if(lst[j]<lst[mini]):
                mini = j
            j+=1
        lst = swap(lst,mini,i)
        i+=1
    print(lst)
selection_sort(arr)
