# LC415.py
# Solution to the LeetCode problem 415
# https://leetcode.com/problems/add-strings/
class Solution:
    def toInt(self, num):
        answer = 0
        for d in num:
            answer = answer * 10 + (ord(d)-48) 
        return answer
        
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = self.toInt(num1)
        n2 = self.toInt(num2)
        print(n1,n2)
        answer = n1+n2
        return str(answer)


  
mySolution = Solution()
'''
result = mySolution.addStrings('123', '456')
print(result) # We expect 123+456=579
# Do a test that will fail
result = mySolution.addStrings('aaa', 'bbb')
print(result)

result = mySolution.addStrings('-123', '456')
print(result) # We expect result = 333

result = mySolution.addStrings('123.5', '456.1')
print(result) # We expect result = 579.6

result = mySolution.addStrings('123a', '456b')
print(result) # Don't know what to expect

result = mySolution.addStrings('123!', '456@')
print(result)
'''
# Let's build a list of test cases and expected results
num1 = ['123', '999', '1000']
num2 = ['456', '111', '2000']
expectedResults = ['579', '1110', '3000']
# Write a loop to try all the test case
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResults[i]:
        print("test passed")
    else:
        print("test FAILED. Change profession")
        print('expected result', expectedResults[i], 'actual result', result)
