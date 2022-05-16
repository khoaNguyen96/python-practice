dna_1 = "ABAZDC"
dna_2 = "BACBAD"


def longest_common_subsequence(string_1, string_2):
    print(f"Finding longest common subsequence of {string_1} and {string_2}")
    grid = [[0 for col in range(len(string_1)+1)] for row in range(len(string_2)+1)]
    for row in range(1, len(string_2)+1):
        print(f"Comparing: {string_2[row-1]}")
        for col in range(1, len(string_1)+1):
            print(f"Against: {string_1[col-1]}")
            if string_1[col-1] == string_2[row-1]:
                grid[row][col] = 1 + grid[row-1][col-1]
            else:
                grid[row][col] = max(grid[row][col-1], grid[row-1][col])
    for row_line in grid:
        print(row_line)

    result = []
    while row > 0 and col > 0:
        if string_1[col - 1] == string_2[row - 1]:
            result.append(string_1[col - 1])
            row -= 1
            col -= 1
        elif grid[row - 1][col] > grid[row][col - 1]:
            row -= 1
        else:
            col -= 1
    result.reverse()
    return "".join(result)

print(longest_common_subsequence(dna_1, dna_2))