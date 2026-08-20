class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n = len(asteroids)
        stack = []
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                while stack and abs(num) > stack[-1] and stack[-1] > 0:
                    stack.pop()
                if stack and abs(num) == stack[-1]:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                        stack.append(num)
        return stack
        