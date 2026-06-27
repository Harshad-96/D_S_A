arr = [1,2,4,7,7,5]
first_large = arr[0]
sencond_large = -1

for i in range(0,len(arr)-1):
    if arr[i] > first_large:
        sencond_large = first_large
        first_large = arr[i]
if sencond_large < arr[len(arr)-1]:
    sencond_large = arr[len(arr)-1]
print(sencond_large)
            