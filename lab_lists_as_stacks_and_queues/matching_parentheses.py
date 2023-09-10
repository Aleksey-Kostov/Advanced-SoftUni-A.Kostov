algebraic_expression = input()
stack_parentheses = []

for char in range(len(algebraic_expression)):
    if algebraic_expression[char] == "(":
        stack_parentheses.append(char)
    elif algebraic_expression[char] == ")":
        start_index = stack_parentheses.pop()
        end_index = char + 1
        print(algebraic_expression[start_index:end_index])

