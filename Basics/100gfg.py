#Sum of sum-series of first N Natural numbers

class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        return (n*(n+1))//2



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))  # Number of test cases
    for _ in range(t):
        n = int(input("Enter value of n: "))  # Taking 'n' as input
        obj = Solution()
        res = obj.seriesSum(n)
        print("Sum of series:", res)

# } Driver Code Ends