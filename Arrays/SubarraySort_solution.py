def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        if isOutOfOrder(array, i):
            minOutOfOrder = min(array[i], minOutOfOrder)
            maxOutOfOrder = max(array[i], maxOutOfOrder)
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    upwardIndex = 0
    downwardIndex = len(array) - 1
    while array[upwardIndex] <= minOutOfOrder:
        upwardIndex += 1
    while array[downwardIndex] >= maxOutOfOrder:
        downwardIndex -= 1
    return [upwardIndex, downwardIndex]


def isOutOfOrder(array, i):
    if i == 0:
        return array[i] > array[i + 1]
    elif i == len(array) - 1:
        return array[i - 1] > array[i]
    else:
        return array[i] > array[i + 1] or array[i] < array[i - 1]


inputArray = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]


def main():
    print(subarraySort(inputArray))


if __name__ == "__main__":
    main()
