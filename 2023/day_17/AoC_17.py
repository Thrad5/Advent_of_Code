'''
Created on: 22:27:20
author: @ram86

'''

import math
import copy

def findMin(weightsMap, visitedMap,xDims,yDims):
    minValue = math.inf
    xymin = None
    for x in range(xDims):
        for y in range(yDims):
            if visitedMap[y][x] == False and weightsMap[y][x] < minValue:
                minValue = weightsMap[y][x]
                xymin = [x,y]
    return xymin

def canGoDir(xy,locs,numInRow):
    locers = []
    



cityGridstr = []
with open('test.txt','r') as file:
    for line in file:
        cityGridstr.append(list(line)[:-1])


xDim = len(cityGridstr[0])
yDim = len(cityGridstr)
visit1l = []
weights1l = []
locFrom1l = []
for i in range(xDim):
    visit1l.append(False)
    weights1l.append(math.inf)
    locFrom1l.append([xDim,yDim])
hasVisited = []
weights = []
locFrom = []
for i in range(yDim):
    hasVisited.append(copy.deepcopy(visit1l))
    weights.append(copy.deepcopy(weights1l))
    locFrom.append(copy.deepcopy(locFrom1l))
cityGrid = copy.deepcopy(cityGridstr)
hasVisitedStr = copy.deepcopy(hasVisited)
weightsStr = copy.deepcopy(weights)
locFromStr = copy.deepcopy(locFrom)
for i in range(len(cityGrid)):
    for j in range(len(cityGrid[0])):
        cityGrid[j][i] = int(cityGrid[j][i])
        hasVisitedStr[j][i] = str(hasVisitedStr[j][i])
        weightsStr[j][i] = str(weightsStr[j][i])
        locFromStr[j][i] = str(locFromStr[j][i])
for i in range(yDim):
    print(','.join(cityGridstr[i]), ' ', ','.join(weightsStr[i]), ' ', ','.join(locFromStr[i]))
hasVisited[0][0] = True
weights[0][0] = 0
locFrom[0][0] = [-1,-1]
numberInARow = 2

runs = 0
while runs < 169:
    if runs % 100 == 0:
        print(f'Run number{runs}')
    runs += 1
    for x in range(xDim):
        for y in range(yDim):
            if hasVisited[y][x]:
                if x - 1 >= 0 and hasVisited[y][x-1] == False:
                    subtotal = weights[y][x] + cityGrid[y][x-1]
                    if subtotal < weights[y][x-1]:
                        weights[y][x-1] = subtotal
                        locFrom[y][x-1] = [x,y]
                if y - 1 >= 0 and hasVisited[y-1][x] == False:
                    subtotal = weights[y][x] + cityGrid[y-1][x]
                    if subtotal < weights[y-1][x]:
                        weights[y-1][x] = subtotal
                        locFrom[y-1][x] = [x,y]
                if x + 1 < xDim and hasVisited[y][x+1] == False:
                    subtotal = weights[y][x] + cityGrid[y][x+1]
                    if subtotal < weights[y][x+1]:
                        weights[y][x+1] = subtotal
                        locFrom[y][x+1] = [x,y]
                if y + 1 < yDim and hasVisited[y+1][x] == False:
                    subtotal = weights[y][x] + cityGrid[y+1][x]
                    if subtotal < weights[y+1][x]:
                        weights[y+1][x] = subtotal
                        locFrom[y+1][x] = [x,y]
    xymins = findMin(weights,hasVisited,xDim,yDim)
    if xymins != None:
        hasVisited[xymins[1]][xymins[0]] = True
    if hasVisited[12][12] == True:
        break
print("After 'Dijkstra's' algorithm")
hasVisitedStr = copy.deepcopy(hasVisited)
weightsStr = copy.deepcopy(weights)
locFromStr = copy.deepcopy(locFrom)
for i in range(len(cityGrid)):
    for j in range(len(cityGrid[0])):
        hasVisitedStr[j][i] = str(hasVisitedStr[j][i])
        if len(hasVisitedStr[j][i]) == 1:
            hasVisitedStr[j][i] = ' ' + hasVisitedStr[j][i]
        weightsStr[j][i] = str(weightsStr[j][i])
        if len(weightsStr[j][i]) == 1:
            weightsStr[j][i] = ' ' + weightsStr[j][i]
        locFromStr[j][i] = str(locFromStr[j][i])
        if len(locFromStr[j][i]) == 7:
            locFromStr[j][i] = ' ' + locFromStr[j][i]
        elif len(locFromStr[j][i]) == 6:
            locFromStr[j][i] = '  ' + locFromStr[j][i]
for i in range(yDim):
    print(','.join(cityGridstr[i]), ' ', ','.join(weightsStr[i]), ' ', ','.join(locFromStr[i]))
