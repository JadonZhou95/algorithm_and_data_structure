class Node(object):

    def __init__(self, data):
        self.value = data
        self.leftchild = None
        self.rightchild = None

     
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild:
                self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
        else:
            if self.rightchild:
                self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)

    
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False


    def preorder(self):
        print(self.value)
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()


    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        print(self.value)
        if self.rightchild:
            self.rightchild.inorder()


    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(self.value)



class Tree(object):
    def __init__(self):
        self.root = None
    

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("Preorder")
        if self.root:
            self.root.preorder()

    def inorder(self):
        print("Inorder")
        if self.root:
            self.root.inorder()

    def postorder(self):
        print("Postorder")
        if self.root:
            self.root.postorder()



tree = Tree()
tree.insert(10)
tree.insert(9)
tree.insert(20)
tree.insert(8)
tree.insert(3)
tree.insert(2)

print(tree.find(20))
print(tree.find(2))
tree.preorder()
tree.inorder()
tree.postorder()
    