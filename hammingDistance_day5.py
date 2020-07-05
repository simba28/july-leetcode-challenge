class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        a = list(bin(x)[2:])
        b = list(bin(y)[2:])
        
        la = len(a)
        lb = len(b)
        
        if la > lb:
            b = (['0'] * (la-lb)) + b
        else:
            a = (['0'] * (lb-la)) + a
            
        count = 0
        
        
        for i in range(len(a)):
            if a[i]!=b[i]:
                count += 1
                
        return count

# test = Solution()
# print(test.hammingDistance(4,1))