
'''
16:48:20 13/12/23
'''

def does_it_reflect(mapp,reflectRow):
    # reflectRow is the row above the line of reflection (if it is 4 the reflection line 
    # is between rows 4 and 5)
    topLine = reflectRow
    bottomLine = reflectRow +1
    total_num_diff = 0
    while not(topLine == -1 or bottomLine == len(mapp)):
        total_num_diff += num_of_diffs(mapp[topLine],mapp[bottomLine])
        topLine -= 1
        bottomLine += 1
    topLine = reflectRow
    bottomLine = reflectRow +1
    if total_num_diff == 0:
        return False, total_num_diff
    while not((topLine == -1 or bottomLine == len(mapp))):
        
        if mapp[topLine] != mapp[bottomLine] and total_num_diff != 1:
            return False,total_num_diff
        topLine -= 1
        bottomLine += 1
    return True,total_num_diff

def num_of_diffs(line1, line2):
    diffs = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            diffs +=1
    return diffs

def line_of_reflect_row (mapp):
    for i in range(len(mapp)-1):
        j, k = does_it_reflect(mapp,i)
        if j:
            return (i+1)*100
        
    return 0

def line_of_reflect_clmn (mapp):
    mappt = list(map(list, zip(*mapp)))
    for i in range(len(mappt)-1):
        j,k = does_it_reflect(mappt,i)
        if j:
            return i+1
    
    return 0

path = './input.txt'
singMap = []
fullMap = []
with open(path,'r') as file:
    for line in file:
        if line != '\n':
            singMap.append(line[:-1])
        else:
            fullMap.append(singMap)
            singMap = []
    fullMap.append(singMap)


i = 0
for j in range(len(fullMap)):
    k = line_of_reflect_clmn(fullMap[j])
    if k == 0:
        k = line_of_reflect_row(fullMap[j])
    i += k
print('Column First')
print(i)

i = 0
for j in range(len(fullMap)):
    k = line_of_reflect_row(fullMap[j])
    if k == 0:
        k = line_of_reflect_clmn(fullMap[j])
    i += k
print('Row First')
print(i)

print('Do Both')
i = 0
for j in range(len(fullMap)):
    i += line_of_reflect_clmn(fullMap[j])
    i += line_of_reflect_row(fullMap[j])
print(i)