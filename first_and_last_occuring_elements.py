#first occurence element
arr=list(map(float,input("Input Elemnts In List \t").split()))
target=int(input("Enter The Target Element \t"))
def binary_search(arr,target):
    l=0
    h=len(arr)-1
    m=0
    while(l<h):
        mid=(l+h)//2
        if p_first(arr,target,mid):
            h=mid
        else:
            l=mid+1
    return l
def p_first(arr,target,mid):
    if arr[mid]>=target:
        return True
    else:
        return False
a=binary_search(arr,target)
if a!=-1:
    print("target element ",target," is found at index ",a)
else:
    print("element not present in the list")
    
    
    
