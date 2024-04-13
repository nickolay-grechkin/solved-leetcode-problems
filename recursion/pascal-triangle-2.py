hash = {}

def getTriangleNode(i, j):
    if j == 0 or i == j:
        return 1
    
    if str(i - 1) + str(j - 1) in hash:
        return hash.get(str(i - 1) + str(j - 1)) + getTriangleNode(i - 1, j)

    value = getTriangleNode(i - 1, j - 1) + getTriangleNode(i - 1, j)

    hash[str(i) + str(j)] = value

    return value


def getRow(rowIndex):
    nodes = []
    for i in range(0, rowIndex + 1):
        nodes.append(getTriangleNode(rowIndex, i))
    print(hash)

    return nodes

print(getRow(26))