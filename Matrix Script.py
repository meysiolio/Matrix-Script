#!/bin/python3
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string = ""
for j in range(m):
    for i in range(n):
        string += matrix[i][j]
        
print(re.sub(r'(?<=\w)([^\w]+)(?=\w)',' ', string))
