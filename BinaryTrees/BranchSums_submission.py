class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def BranchSums(root):
    sumArray = []
    calculateSum(root, sumArray, 0)
    return sumArray


def calculateSum(node, sumArray, tempSum):
    if not node.left and not node.right:
        sumArray.append(tempSum+node.value)
    if node.left:
        calculateSum(node.left, sumArray, tempSum + node.value)
    if node.right:
        calculateSum(node.right, sumArray, tempSum + node.value)
