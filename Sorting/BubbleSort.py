#BUBBLE SORT
#Time:   Worst - O(n^2)
#        Best - O(n) - sorted array
#Space - O(n), Auxilary - O(1)

arr = [4,5,2,1,6,9,0,8]
print(arr)

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return lst

def bubble_sort(lst):
    i=0
    while(i<len(lst)):
        flag = 0
        j=0
        while(j<len(lst)-1-i): #gets sorted from last
            if(lst[j]>lst[j+1]):
                lst = swap(lst,j,j+1)
                flag = 1
            j+=1
        if(flag == 0):
            break
        i+=1
    print(lst)
bubble_sort(arr)
