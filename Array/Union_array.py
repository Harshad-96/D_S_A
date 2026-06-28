arr1 = [1,2,2,3,4,5]
arr2 = [1,2,4,5,6,6,7]

# s = set()
# n1 = len(arr1)
# n2 = len(arr2)

# i = 0
# j = 0

# for i in range(0,n1):
#     if i<=j:
#         s.add(arr1[i])
#     else:
#         s.add(arr2[j])
#         j += 1
# for j in range(0,n2):
    
#         s.add(arr2[j]) 
# union_arr = list(s)   
# print(union_arr)               

union_arr = []
i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        if not union_arr or union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1
    elif arr2[j] < arr1[i]:    
        if not union_arr or union_arr[-1] != arr2[j]:
            union_arr.append(arr2[j])
        j += 1
    else:
        if not union_arr or union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1
        j += 1
while i < len(arr1):
    if union_arr[-1] != arr1[i]:
        union_arr.append(arr1[i])
    i += 1
    
while j < len(arr2):
    if union_arr[-1] != arr2[j]:
        union_arr.append(arr2[j])
    j += 1
        
print(union_arr)