'''
created on 17:22:15 11/12/2023
author: @ram86
'''

import copy
import time
startTime = time.time()
starMap = []
with open("D:\\!Advent_of_Code\\2023\\day_11\\input.txt","r") as f:
    for line in f.readlines():
        if line[-1] == '\n':
            starMap.append(list(line[:-1]))
        else:
            starMap.append(list(line))

columnHasStar =[]
rowNoStar = []
for i in range(len(starMap)):
    rowAllSpace = True
    for j in range(len(starMap[0])):
        if starMap[i][j] == "#":
            rowAllSpace = False
            if (j in columnHasStar) == False:
                columnHasStar.append(j)
    if rowAllSpace:
        rowNoStar.append(i)

blankRow = []
columnNoStar = []
for i in range(len(starMap[0])):
    blankRow.append('.')
    if (i in columnHasStar) == False:
        columnNoStar.append(i)


for i in range(len(starMap)):
    print(''.join(starMap[i]))



for i in range(len(starMap)):
    print(''.join(starMap[i]))
print("Rows: ",rowNoStar)
print("Columns: ",columnNoStar)
starCoords = []
for i in range(len(starMap)):
    for j in range(len(starMap[0])):
        if starMap[i][j] == '#': # Row then Column
            starCoords.append([i,j])


newCoords = copy.deepcopy(starCoords)
distanceGrowth = 1000000-1
for i in range(len(starCoords)):
    for j in range(len(columnNoStar)):
        reverse = len(columnNoStar) -j-1
        if starCoords[i][1] > columnNoStar[reverse]:
            starCoords[i][1] = starCoords[i][1]+distanceGrowth
    for k in range(len(rowNoStar)):
        reverse = len(rowNoStar)-k-1
        if starCoords[i][0] > rowNoStar[reverse]:
            starCoords[i][0] = starCoords[i][0]+distanceGrowth


lengths = []

for i in range(len(starCoords)):
    for j in range(i+1,len(starCoords)):
        lengths.append(abs(starCoords[i][0]-starCoords[j][0])+abs(starCoords[i][1]-starCoords[j][1]))

total = 0
for j in lengths:
    total +=j
print(total)
print('Time taken to run: ',time.time()-startTime)




