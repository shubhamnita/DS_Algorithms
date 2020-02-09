def get_number_of_islands(binaryMatrix):
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])
    # you can use Set if you like
    # or change the content of binaryMatrix as it is visited
    visited = [[0 for col in range(cols)] for r in range(rows)]
    number_of_island = 0
    for row in range(rows):
        for col in range(cols):
            number_of_island += get_island(binaryMatrix, row, col, visited)
    return number_of_island


# get a continuous island
def get_island(binaryMatrix, row, col, visited):
    if not is_valid(binaryMatrix, row, col)
        or visited[row][col] == 1 or binaryMatrix[row][col] == 0:
        return 0

    # mark as visited
    visited[row][col] = 1
    get_island(binaryMatrix, row, col + 1, visited)
    get_island(binaryMatrix, row, col - 1, visited)
    get_island(binaryMatrix, row + 1, col, visited)
    get_island(binaryMatrix, row - 1, col, visited)
    return 1


def is_valid(binaryMatrix, row, col):
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])
    return row >= 0 and row < rows and col >= 0 and col < cols
Extra