class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def preorder(self,root,tree_order=None):
        if tree_order is None:
            tree_order = []
        if root:
            tree_order.append(root.val)
            self.preorder(root.left, tree_order)
            self.preorder(root.right, tree_order)
        return tree_order

    def inorder(self,root,tree_order=None):
        if tree_order is None:
            tree_order = []
        if root:
            self.inorder(root.left, tree_order)
            tree_order.append(root.val)
            self.inorder(root.right, tree_order)
        return tree_order


    def postorder(self,root,tree_order=None):
        if tree_order is None:
            tree_order = []
        if root:
            self.postorder(root.left, tree_order)
            self.postorder(root.right, tree_order)
            tree_order.append(root.val)
        return tree_order

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

    def search(self,val,current_node): 
        if current_node is None:
            return "Not found"
        if val == current_node.val:
            return "Found"
        if val < current_node.val:
            return self.search(val,current_node.left)
        else: 
            return self.search(val,current_node.right)

if __name__=="__main__":
    BST = BinaryTree()
    BST.insert_node(TreeNode(10))
    BST.insert_node(TreeNode(5))
    BST.insert_node(TreeNode(15))
    BST.insert_node(TreeNode(3))
    print(BST.inorder(BST.root))
    print(BST.preorder(BST.root))
    print(BST.postorder(BST.root))
    print(BST.search(15,BST.root))
    print(BST.search(78,BST.root))



