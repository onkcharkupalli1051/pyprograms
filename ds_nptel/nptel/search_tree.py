class Tree:
    def __init__(self, initval = None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return

    def isempty(self):
        return(self.value == None)

    #inorder traversal : lists values in sorted order : left value right
    def inorder(self):
        if self.isempty():
            return []
        else:
            return (self.left.inorder() + [self.value] + self.right.inorder())

    def __str__(self):
        return (str(self.inorder()))

    def find(self,v):
        if self.isempty():
            return False
        if self.value == v:
            return True
        if v < self.value:
            return self.left.find(v)
        else:
            return self.right.find(v)

    def minval(self):
        if self.left == None:
            return self.value
        else:
            return self.left.minval()

    def maxval(self):
        if self.right == None:
            return self.value
        else:
            return self.right.maxval()

    def insert(self,v): #find v, if not found the place where
                        # we stop searching is the location
                        # of v
        if self.isempty():
            self.value = v
            self.right = Tree()
            self.left = Tree()

        if self.value == v:
            return

        if v < self.value:
            self.left.insert(v)
            return

        if v > self.value:
            self.right.insert(v)
            return

    def delete(self,v):
        if self.isempty():
            return
        if self.value == v:
            if self.isleaf():
                self.makeempty()


