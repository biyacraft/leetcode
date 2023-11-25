

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dict = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                dict.append("FizzBuzz")
            elif i%3==0:
                dict.append("Fizz")
            elif i%5==0:
                dict.append("Buzz")
            else:
                dict.append(str(i))
        return dict
