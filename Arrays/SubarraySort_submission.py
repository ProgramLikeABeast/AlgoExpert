def subarraySort(array):
    small, large, lower, higher = float("inf"), float("inf"), 0, 0
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            small = min(array[i + 1], small)
    if small == float("inf"):
        return [-1, -1]
    for j in reversed(range(len(array) - 1)):
        if array[j] > array[j + 1]:
            large = max(array[j], large)
    for m in range(len(array)):
        if small <= array[m] <= large:
            lower = m
            break
    for n in reversed(range(len(array))):
        if small <= array[n] <= large:
            higher = n
            break
    return [lower, higher]


inputArray = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]


def main():
    print(subarraySort(inputArray))


if __name__ == "__main__":
    main()
