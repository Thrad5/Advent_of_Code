'''
Created on 11:14:18 14/12/23
author: ram86
'''
import copy
def print_plane(planet):
    for lin in planet:
        string = ''
        for i in lin:
            string += i
        print(string)

def count_O_in (line):
    total = 0
    for i in line:
        if i == 'O':
            total+=1
    return total

def fall_north(planet):
    none_moved = True
    while none_moved:
        none_moved = False
        for i in range(1,len(planet)):
            for j in range(len(planet[0])):
                if planet[i][j] == 'O' and planet[i-1][j] == '.':
                    planet[i-1][j] = 'O'
                    planet[i][j] = '.'
                    none_moved = True
    return planet

def fall_south(planet):
    none_moved = True
    while none_moved:
        none_moved = False
        for i in range(0,len(planet)-1):
            for j in range(len(planet[0])):
                if planet[i][j] == 'O' and planet[i+1][j] == '.':
                    planet[i+1][j] = 'O'
                    planet[i][j] = '.'
                    none_moved = True
    return planet

def fall_south(planet):
    none_moved = True
    while none_moved:
        none_moved = False
        for i in range(0,len(planet)-1):
            for j in range(len(planet[0])):
                if planet[i][j] == 'O' and planet[i+1][j] == '.':
                    planet[i+1][j] = 'O'
                    planet[i][j] = '.'
                    none_moved = True
    return planet

def fall_east(planet):
    none_moved = True
    while none_moved:
        none_moved = False
        for i in range(0,len(planet)-1):
            for j in range(len(planet[0])):
                if planet[j][i] == 'O' and planet[j][i+1] == '.':
                    planet[j][i+1] = 'O'
                    planet[j][i] = '.'
                    none_moved = True
    return planet

def fall_west(planet):
    none_moved = True
    while none_moved:
        none_moved = False
        for i in range(1,len(planet)):
            for j in range(len(planet[0])):
                if planet[j][i] == 'O' and planet[j][i-1] == '.':
                    planet[j][i-1] = 'O'
                    planet[j][i] = '.'
                    none_moved = True
    return planet

def spin_cycle (planet):
    planeb = fall_north(planet)
    planeb = fall_west(planeb)
    planeb = fall_south(planeb)
    planeb = fall_east(planeb)
    return planeb

plane = []
with open('./input.txt','r') as file:
    for line in file.readlines():
        plane.append(list(line[:-1]))

plane1 = spin_cycle(plane)

cycles = [copy.deepcopy(plane1)]
plane2 = spin_cycle(plane1)
cycleNum = [1]
i = 2
while  i<1000000:
    if i %10000 ==0:
        print(i)
    if plane2 in cycles:
        break
    cycles.append(copy.deepcopy(plane2))
    cycleNum.append(i)
    plane2 = spin_cycle(plane2)
    i +=1

j =cycles.index(plane2)
finalIndex = 1000000%((i-1)-cycleNum[j])+j-1

print('Cycle start:',j)
print('Cycle end:',i-1)
print(finalIndex)
totals = []
for k in range(j,i-1):
    total = 0
    for i in range(len(cycles[j])):
        total += count_O_in(cycles[k][i]) * (len(cycles[k])-i)
    print(f'Cycle {k+1}. Weight {total}')
    totals.append([total,k+1])


for i in range(len(totals)):
    if totals[i][0] >103858:
        print(totals[i][1])