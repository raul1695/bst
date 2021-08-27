"""
Simple implementation of an the Binary Search Tree in python.

includes : height function, balancing function, and traversal function.

In this implementation I do not make a distinction between the "node" class and the "tree" class, as found in the implementation
of the BST in other languages. (My AVL implementation does make this distinction)

The purpose of implementing the height function as iterative is in order to better grasp the relation between recurisve
functions and their iterative implementations. 

The recursive version of the height function is also shown below (although not used with the isBalanced method).

If using the recursive height function, the isBalanced method would have to be implemented as follows:

    def isBalanced(self):
        if(self.val == None):
            return True
        return ( height(self) != -1 )

"""





"""
------------------------------------------------------------ Class Def -----------------------------------------
"""

import collections
 
class TreeNode:
    def __init__(self, key = None):
        self.val = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)
        
    def insert(self,key):
        if(self.val == None):
            self.val = key
            return
        else:
            if(self.val > key):
                if( self.left == None):
                    self.left = TreeNode(key)
                    return
                else:
                    n = self.left
                    n.insert(key)
                    return
            elif(key == self.val):
                return
            
            else:
                if(self.right == None):
                    self.right = TreeNode(key)
                    return
                else:
                    r = self.right
                    r.insert(key)
                    
    def find(self, key):
        if(self.val == key):
            return True
        elif(self.val > key):
            if(self.left != None):
                n = self.left
                return n.find(key)
            else:
                return False
        else:
            if(self.right != None):
                n = self.right
                return n.find(key)
            else:
                return False
        return False
    
    
    def isBalanced(self):
        l = self.left
        r = self.right
        
        left_height = height_itr(l)
        right_height = height_itr(r)

        if abs(left_height - right_height) > 1:
            return left_height - right_height
        else:
            return 0
   
    def delete(self,key):
        if self.val is None:
            return
        if key < self.val:
            if self.left:
                self.left = self.left.delete(key)
            else:
                print("Key not found in tree")
        elif key > self.val:
            if self.right:
                self.right = self.right.delete(key)
            else:
                print("Key not found in tree")
        elif(key == self.val):

            #Takes care of Case 1 : No Child, and Case 2 : 1 child
            if self.left == None:
                temp = self.right
                self = None
                return temp
            if self.right == None:
                temp = self.left
                self = None
                return temp

            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key)

        return self
    
    def find_min(self):
        if self.val:
            if self.left:
                return self.left.find_min()
        return self.val

    def find_max(self):
        if self.val:
            if self.right:
                return self.right.find_max()
        return self.val

        

"""
------------------------------------------------------------ Class Def -----------------------------------------
"""


"""
------------------------------------------------------------ FUNCTIONS -----------------------------------------
"""
        



def height_itr(root):
    count = 0
    queue = collections.deque()

    if root == None:
        return count
    
    queue.append(root)

    while queue:
        q_size = len(queue)
        while q_size > 0:
            current_node = queue.popleft()
            q_size -= 1

            if(current_node.left != None):
                queue.append(current_node.left)
            if(current_node.right != None):
                queue.append(current_node.right)
        count += 1
    return count


def height_recursive(root):
    if(root == None):
        return 0
        
    l = height(root.left)
    r = height(root.right)

    if(l == -1 or r == -1 or abs(l - r) > 1):
        return -1
    return max(l,r) + 1




"""
------------------------------------------------------------ FUNCTIONS -----------------------------------------
"""




"""Driver program below"""
    

a = [9,2,16,17,18,3,99,56,1]
root = TreeNode()
for i in a:
    root.insert(i)

print(root.isBalanced())
print(root.find_min())
root.delete(1)
print(root.find_min())
