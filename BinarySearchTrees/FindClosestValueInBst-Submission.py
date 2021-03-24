# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    tempNode = tree
    tempValue = float("inf")
    while True:
        if abs(tempNode.value - target) < abs(tempValue - target):
            tempValue = tempNode.value
        if tempNode.value == target:
            return tempValue
        elif tempNode.value < target:
            if not tempNode.right:
                return tempValue
            else:
                tempNode = tempNode.right
        else:

            if not tempNode.left:
                return tempValue
            else:
                tempNode = tempNode.left
