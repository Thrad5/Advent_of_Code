"""
created on 22:35:40 10/12/23
author: @ram86
"""
import random

def LTile(prev,curr):
    if curr[0]-prev[0] ==1:
        return curr, [curr[0],curr[1]+1]
    else:
        return curr, [curr[0]-1,curr[1]]

def FTile(prev,curr):
    if prev[0]-curr[0] == 1:
        return curr, [curr[0],curr[1]+1]
    else:
        return curr, [curr[0]+1,curr[1]]

def SevenTile(prev,curr):
    if prev[0]-curr[0] == 1:
        return curr, [curr[0],curr[1]-1]
    else:
        return curr, [curr[0]+1,curr[1]]
    
def JTile(prev,curr):
    if curr[0]-prev[0] ==1:
        return curr, [curr[0],curr[1]-1]
    else:
        return curr, [curr[0]-1,curr[1]]

def PipeTile(prev,curr):
    if curr[0]-prev[0] ==1:
        return curr, [curr[0]+1,curr[1]]
    else:
        return curr, [curr[0]-1,curr[1]]
def dashTile(prev,curr):
    if curr[1]-prev[1] ==1:
        return curr, [curr[0],curr[1]+1]
    else:
        return curr, [curr[0],curr[1]-1]
    
def whatTile(maze,prev,curr):
    if maze[curr[0]][curr[1]] == "J":
        prev,curr = JTile(prev,curr)
        return prev,curr
    elif maze[curr[0]][curr[1]] == "L":
        prev,curr = LTile(prev,curr)
        return prev,curr
    elif maze[curr[0]][curr[1]] == "7":
        prev,curr = SevenTile(prev,curr)
        return prev,curr
    elif maze[curr[0]][curr[1]] == "F":
        prev,curr = FTile(prev,curr)
        return prev,curr
    elif maze[curr[0]][curr[1]] == "|":
        prev,curr = PipeTile(prev,curr)
        return prev,curr
    elif maze[curr[0]][curr[1]] == "-":
        prev,curr = dashTile(prev,curr)
        return prev,curr

class Walker():
    def __init__(self,curr):
        self.current_position = curr
        self.facing = random.randint(0,3)



maze = []
with open("D:\\!Advent_of_Code\\2023\\day_10\\input.txt",'r') as file:
    for line in file.readlines():
        if line[-1] == '\n':
            maze.append(list(line[:-1]))
        else:
            maze.append(list(line))
visited = []
start = []
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start = [i,j]
            print(f"S at ({i},{j})")
        if start != []:
            break
    if start != []:
        break
'''
print(maze[0][0])
prev_loc_1 = start
prev_loc_2 = start
curr_loc_1 = [start[0],start[1]+1]
curr_loc_2 = [start[0]+1,start[1]]
print(f"{prev_loc_1} {curr_loc_1}, {prev_loc_2} {curr_loc_2}")
print(f"Tile at loc_1: {maze[curr_loc_1[0]][curr_loc_1[1]]}")
print(f"Tile at loc_2: {maze[curr_loc_2[0]][curr_loc_2[1]]}")
distance = 1
loop_locs = [start,curr_loc_1,curr_loc_2]
while((curr_loc_1[0] != curr_loc_2[0]) or (curr_loc_1[1]!=curr_loc_2[1])):
    prev_loc_1,curr_loc_1 = whatTile(maze,prev_loc_1,curr_loc_1)
    prev_loc_2,curr_loc_2 = whatTile(maze,prev_loc_2,curr_loc_2)
    loop_locs.append(curr_loc_1)
    loop_locs.append(curr_loc_2)
    print(f"{prev_loc_1} {curr_loc_1}, {prev_loc_2} {curr_loc_2}")
    print(f"Tile at loc_1: {maze[curr_loc_1[0]][curr_loc_1[1]]}")
    print(f"Tile at loc_2: {maze[curr_loc_2[0]][curr_loc_2[1]]}")
    print((curr_loc_1[0] != curr_loc_2[0]))
    print((curr_loc_1[1]!=curr_loc_2[1]))
    print((curr_loc_1[0] != curr_loc_2[0]) and (curr_loc_1[1]!=curr_loc_2[1]))
    distance +=1
print(distance)
outside_spread_start = [0,0]
maze[0][0] = "O"
print(maze[0][0])

'''

maze[112][18] = 'F'
for i in range(len(maze)):
    status = 'O'
    for j in range(len(maze[0])):
        if maze[i][j] == '.':
            maze[i][j] = status
        elif (maze[i][j] == "F") or (maze[i][j] == '7') or (maze[i][j] == "|"):
            if status == "O":
                status = "I"
            else:
                status = "O"
numI = 0
for i in range(len(maze)):
    print(''.join(maze[i]))
    for j in range(len(maze[0])):
        if maze[i][j] == "I":
            numI +=1
print(numI)