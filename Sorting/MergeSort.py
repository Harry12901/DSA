#MERGE
#Time - O(n*logn)
#Auxilary - O(n)
#Recurrence Relation - T(n)=2T(n/2)+o(n)
arr = [4,5,2,1,6,9,0,8]
print(arr)
def merge_sort(lst):
    if (len(lst)>1):
        mid = len(lst)//2
        L = lst[:mid]
        R = lst[mid:]
        merge_sort(L)
        merge_sort(R)
        
        i=j=k=0
        while(i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                lst[k] = L[i]
                i+=1
            else:
                lst[k] = R[j]
                j+=1
            k+=1
        while(i<len(L)):
            lst[k] = L[i]
            i+=1
            k+=1
        while(j<len(R)):
            lst[k] = R[j]
            j+=1
            k+=1
merge_sort(arr)
print(arr)
