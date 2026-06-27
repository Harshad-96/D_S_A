arr = [3,2,1,5,2]
big_ele = arr[0]
for i in range(0,len(arr)-1) :
    if arr[i] > big_ele:
        big_ele = arr[i]
print(big_ele)