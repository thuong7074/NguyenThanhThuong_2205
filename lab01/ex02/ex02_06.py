
input_str = input("Nhập X, Y: ")

dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
column = dimensions[1]

multilist = [[0 for j in range(column)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(column):
        multilist[row][col] = row * col

print(multilist)