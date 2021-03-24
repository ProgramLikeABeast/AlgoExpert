# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left:
                self.left.contains(value)
            else:
                return False
        else:
            if self.right:
                self.right.contains(value)
            else:
                return False
        pass

    def remove(self, value):
        if not self.contains(value):
            return
