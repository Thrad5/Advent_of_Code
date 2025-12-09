'''
20:09:40 19/12/23
ram86
'''
import copy

def aComparison(comp,parta):
    partmod = 0
    if isinstance(comp,str):
        parta[4] = comp
        partmod = 0
    else:
        if comp[0] == 'x':
            if comp[2] <= parta[0][0] and comp[1] == '>':
                parta[4] = comp[3]
            elif parta[0][1] <= comp[2] and comp[1] == '>':
                pass
            elif comp[2] <= parta[0][0] and comp[1] == '<':
                pass
            elif parta[0][1] <= comp[2] and comp[1] == '<':
                parta[4] = comp[3]
            elif comp[1] == '>':
                partmod = copy.deepcopy(parta)
                partmod[0] = [partmod[0][0],comp[2]]
                parta[0] = [comp[2]+1,parta[0][1]]
                parta[4] = comp[3]
            elif comp[1] == '<':
                partmod = copy.deepcopy(parta)
                partmod[0] = [comp[2],partmod[0][1]]
                parta[0] = [parta[0][0],comp[2]-1]
                parta[4] = comp[3]
        elif comp[0] == 'm':
            if comp[2] <= parta[1][0] and comp[1] == '>':
                parta[4] = comp[3]
            elif parta[1][1] <= comp[2] and comp[1] == '>':
                pass
            elif comp[2] <= parta[1][0] and comp[1] == '<':
                pass
            elif parta[1][1] <= comp[2] and comp[1] == '<':
                parta[4] = comp[3]
            elif comp[1] == '>':
                partmod = copy.deepcopy(parta)
                partmod[1] = [partmod[1][0],comp[2]]
                parta[1] = [comp[2]+1,parta[1][1]]
                parta[4] = comp[3]
            elif comp[1] == '<':
                partmod = copy.deepcopy(parta)
                partmod[1] = [comp[2],partmod[1][1]]
                parta[1] = [parta[1][0],comp[2]-1]
                parta[4] = comp[3]
        elif comp[0] == 'a':
            if comp[2] <= parta[2][0] and comp[1] == '>':
                parta[4] = comp[3]
            elif parta[2][1] <= comp[2] and comp[1] == '>':
                pass
            elif comp[2] <= parta[2][0] and comp[1] == '<':
                pass
            elif parta[2][1] <= comp[2] and comp[1] == '<':
                parta[4] = comp[3]
            elif comp[1] == '>':
                partmod = copy.deepcopy(parta)
                partmod[2] = [partmod[2][0],comp[2]]
                parta[2] = [comp[2]+1,parta[2][1]]
                parta[4] = comp[3]
            elif comp[1] == '<':
                partmod = copy.deepcopy(parta)
                partmod[2] = [comp[2],partmod[2][1]]
                parta[2] = [parta[2][0],comp[2]-1]
                parta[4] = comp[3]
        elif comp[0] == 's':
            if comp[2] <= parta[3][0] and comp[1] == '>':
                parta[4] = comp[3]
            elif parta[3][1] <= comp[2] and comp[1] == '>':
                pass
            elif comp[2] <= parta[3][0] and comp[1] == '<':
                pass
            elif parta[3][1] <= comp[2] and comp[1] == '<':
                parta[4] = comp[3]
            elif comp[1] == '>':
                partmod = copy.deepcopy(parta)
                partmod[3] = [partmod[3][0],comp[2]]
                parta[3] = [comp[2]+1,parta[3][1]]
                parta[4] = comp[3]
            elif comp[1] == '<':
                partmod = copy.deepcopy(parta)
                partmod[3] = [comp[2],partmod[3][1]]
                parta[3] = [parta[3][0],comp[2]-1]
                parta[4] = comp[3]

    return parta, partmod
                    



workflows = {}
parts = []
stillInWF = True
with open('input.txt','r') as file:
    for line in file.readlines():
        if line == '\n':
            stillInWF = False
        elif stillInWF:
            workflow = line[:-2]
            workflow = workflow.split('{')
            workflow[1] = workflow[1].split(',')
            for i in range(len(workflow[1])):
                try:
                    workflow[1][i][1] == '>'
                except IndexError:
                    pass
                else:
                    if workflow[1][i][1] == '>' :
                        workflow[1][i] = workflow[1][i].split('>')
                        temp = workflow[1][i][1].split(':')
                        workflow[1][i] = workflow[1][i][0],'>',int(temp[0]),temp[1]
                    elif workflow[1][i][1] == '<' :
                        workflow[1][i] = workflow[1][i].split('<')
                        temp = workflow[1][i][1].split(':')
                        workflow[1][i] = workflow[1][i][0],'<',int(temp[0]),temp[1]
            workflows[workflow[0]] = workflow[1:]
        else:
            part = line[1:-2].split(',')
            for i in range(len(part)):
                part[i] = int(part[i][2:])
            part.append('in')
            parts.append(part)
'''
for workflow in workflows:
    print(workflow)
    for conditions in workflows[workflow]:
        for condition in conditions:
            print(condition)

'''
parts = [[[1,4000],[1,4000],[1,4000],[1,4000],'in']]
inte = 0
for part in parts:  
    while not(part[4] == 'R' or part[4] =='A'):
       startKey = copy.copy(part[4])
       conditions = workflows[part[4]][0]
       print(part)
       for condition in conditions:
           part, new = aComparison(condition,part)
           if new != 0:
                parts.append(new)
           if startKey != part[4]:
               break

total = 0
"""print('After')
for part in parts:
    print(part)
"""
'''
print('Rejected')
for part in parts:
    if part[4] == 'R':
        print(part)
print('Accepted')
for part in parts:
    if part[4] == 'A':
        print(part)
print(total)
'''
print(len(parts))
for part in parts:
    if part[4] == 'A':
        total = total + ( (part[0][1]-part[0][0]+1)*(part[1][1]-part[1][0]+1)*(part[2][1]-part[2][0]+1)*(part[3][1]-part[3][0]+1))
print(total)