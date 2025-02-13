matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2)
print(matrix2[2])
print(matrix2[2][0])



i = 5
while True:
    if i%0o11 == 0: #first comment below
        break
    print(i)
    i += 1

# This line checks if the value of `i` is divisible by `0o11`
# (octal representation of the decimal number `9`).
# The `%` operator is the modulus operator, which returns the remainder of the division.
# If `i` is divisible by `9`, the condition will be `True`.

### Summary of the Loop Execution:
# - The loop starts with `i` initialized to `5`.
# - It checks if `i` is divisible by `9` (since `0o11` in octal is `9` in decimal).
# - If `i` is not divisible by `9`, it prints the value of `i` and increments `i` by `1`.
# - The loop continues until `i` becomes `9`, at which point the condition `i % 0o11 == 0` becomes `True`, and the loop breaks.

### Output:
# The output of the code will be:
# 5
# 6
# 7
# 8

testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

print(testdict.keys())