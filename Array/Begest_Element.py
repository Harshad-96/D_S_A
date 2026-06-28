arr = [3,2,1,5,10]
big_ele = arr[0]
for i in range(0,len(arr)) :
    if arr[i] > big_ele:
        big_ele = arr[i]
print(big_ele)