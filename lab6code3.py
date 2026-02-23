
def shift_right(row):
    new_row = [x for x in row if x != 0]
    zeros = [0] * (len(row) - len(new_row))
    return zeros + new_row

def shift_left(row):
    new_row = [x for x in row if x != 0]
    zeros = [0] * (len(row) - len(new_row))
    return zeros + new_row

import random
row = 4
cols= 4

matrix = []

for i in range(row):
    row = []
    for j in range(cols):
        value = random.randint(0,8)
        row.append(value)
    matrix.append(row)
print("\nМатрица:")

for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()
    
for i in range(4):
    matrix[i] = shift_right(matrix[i])



print("До сдвига:")
for row in matrix:
    print(row)

