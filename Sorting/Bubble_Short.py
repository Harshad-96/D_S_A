nums = [5,3,8,6,7,2]
n = len(nums)
for i in range (n-1,0,-1):
    for j in range(i):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            print(nums)
print(nums)            