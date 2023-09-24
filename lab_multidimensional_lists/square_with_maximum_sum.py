data = input().split(", ")
rows = int(data[0])
col = int(data[1])

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

max_sum = float('-inf')
max_sum_sam_matrix = []

for row_index in range(rows - 1):
    for col_index in range(col - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]
        sum_element = current_element + next_element + element_below + element_diagonal
        if max_sum < sum_element:
            max_sum = sum_element
            max_sum_sam_matrix = [[current_element, next_element], [element_below, element_diagonal]]

print(*max_sum_sam_matrix[0])
print(*max_sum_sam_matrix[1])
print(max_sum)
