'''
23:53:20 19/12/23
ram86
'''
import copy



directions = []
with open('input.txt','r') as file:
    for line in file.readlines():
        modlin = line.split(' ')
        twoNeeded = [int(modlin[-1][2:-3],16),modlin[-1][-3]]
        directions.append(twoNeeded)


verticies = [[0,0]]

mineMap = [['.']]
numDir = 0
for direction in directions:
    numDir+=1
    if direction[1] == '3':
        verticies.append([verticies[-1][0]-direction[0],verticies[-1][1]])
                
    elif direction[1] == '1':
        verticies.append([verticies[-1][0]+direction[0],verticies[-1][1]])
    elif direction[1] =='2':
        verticies.append([verticies[-1][0],verticies[-1][1]-direction[0]])
    else:
        verticies.append([verticies[-1][0],verticies[-1][1]+direction[0]])

doubleTotal = 0
perimiter = 0
for i in range(len(verticies)-1):
    doubleTotal += (verticies[i][0]*verticies[i+1][1]) - (verticies[i+1][0]*verticies[i][1])
    perimiter += abs((verticies[i][0]-verticies[i+1][0])+(verticies[i][1]-verticies[i+1][1]))
print(abs(doubleTotal/2))
doubleTotal = abs(doubleTotal)
total = int(doubleTotal/2)
print(952408144115-total)
diff = 952408144115 - total
print(perimiter)
halfperim = int(perimiter/2)
print(total + halfperim+1)