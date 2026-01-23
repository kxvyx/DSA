class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def preorder(self):
        def dfs(node):
            if not node:
                return
            tree.append(node.val)
            dfs(node.left)
            dfs(node.right)
        tree = []
        dfs(self.root)
        return tree


    def inorder(self):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)
        tree = []
        dfs(self.root)
        return tree

    def postorder(self):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            tree.append(node.val)
        tree = []
        dfs(self.root)
        return tree

    def recursive_insert(self,new_node,current_node):
        if new_node.val < current_node.val:
            if not current_node.left:
                current_node.left = new_node
            else:
                self.recursive_insert(new_node,current_node.left)
        elif new_node.val > current_node.val:
            if not current_node.right:
                current_node.right = new_node
            else:
                self.recursive_insert(new_node,current_node.right)

    def insert_node(self,new_node):
        if not self.root:
            self.root = new_node
        else:
            self.recursive_insert(new_node,self.root)
        
    def delete_node():
        pass

    def search(self,val): 
        pass

if __name__=="__main__":
    BST = BinaryTree()
    BST.insert_node(TreeNode(10))
    BST.insert_node(TreeNode(5))
    BST.insert_node(TreeNode(15))
    BST.insert_node(TreeNode(3))
    print(BST.inorder())
    print(BST.preorder())
    print(BST.postorder())


