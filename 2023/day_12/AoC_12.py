"""
created on 14:52:27 12/12/23

author: @ram86
"""
def sum_of_char (row, car):
    n = 0
    for i in row:
        if i == car:
            n += 1
    return n



def num_of_answer (row, key):
    keySum = 0
    for i in key:
        keySum += i
    if is_it_valid(row,key) :
        return 1
    
    return 0

def is_it_valid (test,key):
    numHash = 0
    numBlocks = []
    for i in range(len(test)):
        if test[i]=='#':
            numHash +=1
        elif test[i] == '.' and numHash != 0:
            numBlocks.append(numHash)
            numHash = 0
    if numHash != 0:
        numBlocks.append(numHash)
    if numBlocks == key:
        return True
    else:
        return False


inp = []
path = './test.txt'
with open(path) as f:
    for line in f.readlines():
        inp.append(line[:-1].split(' '))

for i in range(len(inp)):
    inp[i][1] = inp[i][1].split(',')
    for j in range(len(inp[i][1])):
        inp[i][1][j] = int(inp[i][1][j])

for i in range(len(inp)):
    is_it_valid(inp[i][0],inp[i][1])

for line in inp:
    print(line[0])
qmark = []
working = []
broken = []
all_info = []
for j in range(len(inp)):
    line = inp[j]
    row = []
    numOf= 0
    currChar = line[0][0]
    row.append(currChar)
    for i in range(len(line[0])):
        if line[0][i] == currChar:
            numOf += 1
        else:
            row.append(numOf)
            currChar = line[0][i]
            row.append(currChar)
            numOf = 1
    
    row.append(numOf)
        
    all_info.append(row)

for line in all_info:
    print(line)

