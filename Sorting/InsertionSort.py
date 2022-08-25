#INSERTION
#Time - O(n^2)
#Space - O(n), Auxilary - O(1)
arr = [4,5,2,1,6,9,0,8]
print(arr)
def insertion_sort(lst):
    i=1
    while(i<len(lst)):
        curele = lst[i]
        j = i-1
        while(j>=0 and curele<lst[j]):
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = curele
        i+=1
    print(lst)
insertion_sort(arr)
