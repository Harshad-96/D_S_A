arr = [13,46,24,52,20,9]
n = len(arr)
for i in range(n-1):
    min_ind = i
    for j in range(i+1,n):
        if arr[j] <arr[min_ind] :
            min_ind = j
    arr[i],arr[min_ind] = arr[min_ind] , arr[i]
    print(arr)
print(arr)            