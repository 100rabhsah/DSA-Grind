#Check for Binary

# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        #code here
        for ch in s:
            if ch != '0' and ch != '1': 
                return False
        return True
            

#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input("Enter no of test cases: "))
    for i in range(t):
        str = input("Enter string: ").strip()
        if Solution().isBinary(str):
            print("true")
        else:
            print("false")
        

# } Driver Code Ends