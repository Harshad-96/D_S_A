nums = [3, 0, 1,4,5,6]
n = len(nums)
xor1 = 0
xor2 = 0

for i in range(1, n+1):
    xor1 ^= i
    print(xor1)

for num in nums:
    xor2 ^= num
    print(xor2)

print(xor1)  
print(xor2)  
print(xor1 ^ xor2)