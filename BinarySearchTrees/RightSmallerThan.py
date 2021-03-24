class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(node, value, records):
    renew(node, value, records)
    temp = node
    while True:
        if value < temp.value:
            if temp.left:
                temp = temp.left
            else:
                temp.left = Node(value)
        else:
            if temp.right:
                temp = temp.left
            else:
                temp.right = Node(value)


def renew(node, value, records):
    if node.value > value > records[node.value]:
        records[node.value] = value


def rightSmallerThan(array):
    if not array:
        return []
    else:
        result = []
        records = {}
        for i in range(len(array)):
            records[array[i]] = 0
        tree = Node(array[0])
        for j in range(len(array) - 1):
            insert(tree, array[j + 1], records)
        for k in records:
            result.append(k)
        return result


def main():
    rightSmallerThan([1, 2, 3, 4, 5])


if __name__ == "__main__":
    main()
