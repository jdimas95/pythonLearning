class Node():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree():
    def __init__(self):
        self.root = None
        self.degree = 0

    def add_to_tree(self, data):
        if (self.root == None):
            self.root = Node(data)
        else:
            self.add_leaf(data, self.root)

    def add_leaf(self, val, current_node):
        if (val < current_node.value):
            if (current_node.left_child != None):
                self.add_leaf(val, current_node.left_child)
            else:
                current_node.left_child = Node(val)
        else:
            if (current_node.right_child != None):
                self.add_leaf(val, current_node.right_child)
            else:
                current_node.right_child = Node(val)

    def print(self, traversal_type):
        if (self.root != None):
            if (traversal_type.lower() == "inorder"):
                self.print_tree_inorder(self.root)
            elif (traversal_type.lower() == "preorder"):
                self.print_tree_preorder(self.root)
            elif (traversal_type.lower() == "postorder"):
                self.print_tree_postorder(self.root)
            else:
                print("Invalid traversal type!")
        else:
            print("No tree to print!")

    #inorder traversal
    def print_tree_inorder(self, node):
        if(node != None):
            self.print_tree_inorder(node.left_child)
            print(node.value)
            self.print_tree_inorder(node.right_child)

    #preorder traversal
    def print_tree_preorder(self, node):
        if(node != None):
            print(node.value)
            self.print_tree_preorder(node.left_child)
            self.print_tree_preorder(node.right_child)

    #postorder traversal
    def print_tree_postorder(self, node):
        if(node != None):
            self.print_tree_postorder(node.left_child)
            self.print_tree_postorder(node.right_child)
            print(node.value)

    def delete_tree(self):
        self.root == None
        print("\nTree deleted!")
        #Garbage collection takes care of the rest

tree = Tree()
tree.add_to_tree(4)
tree.add_to_tree(3)
tree.add_to_tree(6)
tree.add_to_tree(5)
tree.add_to_tree(2)
tree.add_to_tree(9)
print("In-order traversal")
tree.print("inorder")
print("\nPre-order traversal")
tree.print("preorder")
print("\nPost-order traversal")
tree.print("postorder")
print("\nInvalid case test")
tree.print("test")
tree.delete_tree()