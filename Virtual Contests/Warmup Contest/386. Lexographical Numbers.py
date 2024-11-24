#Problem Number: 386
#Problem Statement:
#Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
#You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
#Difficulty level: Medium

class Solution(object):
    def lexicalOrder(self, n):
        num = 1
        ans = []
        while len(ans) < n:
            ans.append(num)

            if num * 10 <= n: 
                num *= 10
            elif num % 10 != 9 and num + 1 <= n: 
                num += 1
            else:
                while (num / 10) % 10 == 9:
                    num /= 10
                num = (num / 10) + 1
                
        return ans
