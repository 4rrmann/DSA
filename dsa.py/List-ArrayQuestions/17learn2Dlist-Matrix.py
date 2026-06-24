nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(nums)
columns = len(nums[0])

print(f"Rows:{rows} & Columns:{columns}\n")


print("2D Matrix:")
for i in range(0, rows):
    for j in range(0, columns):
        print(nums[i][j], end=" ")
    print()

#UPPER TRIANGLE:
print("\nUPPER TRIANGLE Matrix:")
for i in range(0, rows):
    for j in range(0, columns):
        if j>=i:
            print(nums[i][j], end=" ")
    print()

#LOWER TRIANGLE:
print("\nLOWER TRIANGLE Matrix:")
for i in range(0, rows):
    for j in range(0, columns):
        if i>=j:
            print(nums[i][j], end=" ")
    print()

#DIAGONAL:
print("\nDIAGONAL Matrix:")
for i in range(0, rows):
    for j in range(0, columns):
        if i==j:
            print(nums[i][j], end=" ")
    print()

#OPPOSITE DIAGONAL:
print("\nOPPOSITE DIAGONAL Matrix:")
for i in range(rows):
    for j in range(columns):
        if i + j == columns - 1:
            print(nums[i][j], end=" ")
    print()

#TRANSPOSE MATRIX:
print("\nTRANSPOSE Matrix:")
transpose = [[0]*rows for _ in range(columns)]
for i in range(rows):
    for j in range(columns):
        transpose[j][i] = nums[i][j]
    print()

print(transpose)