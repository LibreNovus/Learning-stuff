matrix=[]
x = ''
sum = 0

for x in range(5):
    list=[]
    x=str(input()).replace(' ','')
    for y in x:
        list.append(y)
    matrix.append(list)

row=len(matrix)
columns=len(matrix[0])
for i in range(row):
    for j in range(columns):
        if matrix[i][j] == '1':
            i = int(i)
            j = int(j)
            print(i, j)
            while i != 2:
                if i > 2:
                    i -= 1
                    sum += 1
                elif i < 2:
                    i += 1
                    sum += 1
            while j != 2:
                if j > 2:
                    j -= 1
                    sum += 1
                elif j < 2:
                    j += 1
                    sum += 1
            print(sum)
#[1][4] = 3
#[2][1] = 1
