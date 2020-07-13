# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
    
        if p == None and q == None:
            return True
        
        if (p==None and q!=None) or (p!=None and q==None):
            return False
        
        if p.val != q.val:
            return False
        
        first = [p]
        second = [q]

        while first and second :
            

            currentf = first.pop()
            currents = second.pop()

            if currentf.val != currents.val:
                return False

            if currentf.left and (not currents.left):
                return False
            if (not currentf.left) and currents.left :
                return False


            if currentf.right and (not currents.right):
                return False
            if (not currentf.right) and currents.right :
                return False

            if currentf.left != None and currents.left != None:
                first.insert(0,currentf.left)
                second.insert(0,currents.left)
            if currentf.right != None and currents.right != None:
                first.insert(0,currentf.right)
                second.insert(0,currents.right)
            
        return True
