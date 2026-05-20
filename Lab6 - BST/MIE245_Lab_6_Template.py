from typing import List, Union

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    """
    A class to implement insert, search, and level order traversal for a BST.

    Methods:
    --------
    insert(root: Union[TreeNode, None], val: int) -> TreeNode:
        Inserts a value into the BST and returns the root node.
    
    search(root: Union[TreeNode, None], val: int) -> bool:
        Searches for a value in the BST and returns True if found, False otherwise.
    
    level_order_traversal(root: Union[TreeNode, None]) -> List[int]:
        Traverses the BST in level order and returns the node values.
    """
    def insert(self, root: Union[TreeNode, None], val: int) -> TreeNode:
        # RECURSIVE SOLUTION
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        
        return root
        
        # ITERATIVE SOLUTION (FROM LECTURE)
        # current = root
        # parent = None
        # # Traverse to correct position of tree
        # # parent *will be* the correct parent of the new node
        # while current is not None:
        #     parent = current
        #     if current.val > val:
        #         current = current.left
        #     else:
        #         current = current.right
        # # Create/insert the new node
        # if parent is None:
        #     root = TreeNode(val)
        # elif val < parent.val:
        #     parent.left = TreeNode(val)
        # else:
        #     parent.right = TreeNode(val)
        # return root
    
    def search(self, root: Union[TreeNode, None], val: int) -> bool:
        # RECURSIVE SOLUTION
        if root is None:
            return False
        
        if val == root.val:
            return True
        elif val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)
        
        # ITERATIVE SOLUTION (FROM LECTURE)
        # node = root
        # while node is not None:
        #     if node.val == val:
        #         return True
        #     elif node.val > val:
        #         node = node.left
        #     else:
        #         node = node.right
        # return False
    
    def level_order_traversal(self, root: Union[TreeNode, None]) -> List[int]:
        if root is None:
            return []
        
        result = []
        q = [root]

        while q:
            node = q.pop(0)
            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return result
