# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        
        if root == None:
            return []
        
        res = []
        queue = [root]
        
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                
                current = queue.pop()
                temp.append(current.val)
                if current.left:
                    queue.insert(0,current.left)
                if current.right:
                    queue.insert(0,current.right)
                    
            res.append(temp)
        
        for i in range(len(res)):
            if i%2 != 0:
                res[i] = res[i][::-1]
                
        return res