class Solution:
    def reverse(self, arr: list, n: int) -> None:
        self.rev(arr,0)
    def rev(self,arr,left):
        length = len(arr)
        if left >= length//2:
            return
        arr[left],arr[length-1-left] = arr[length-1-left],arr[left]
        self.rev(arr,left+1)
        