def nonConstructibleChange(coins):
    coins.sort()
    resultSet = set()
    resultSet.add(0)
    for i in coins:
        tempSet = set()
        for j in resultSet:
            tempSet.add(j + i)
        resultSet |= tempSet
    probe = 0
    while True:
        if probe not in resultSet:
            return probe
        probe += 1


coins = [5, 7, 1, 1, 2, 3, 22]


def main():
    print(nonConstructibleChange(coins))


if __name__ == "__main__":
    main()
