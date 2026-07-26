# def recursive(n):
    
#     if n == 5:
#         return
#     print("hello")
#     recursive(n+1)
# recursive(0) 
def print_nth(i,n):
    if i == n:
        return
    
    print_nth(i+1,n)
    print(i)
print_nth(0,15)
    