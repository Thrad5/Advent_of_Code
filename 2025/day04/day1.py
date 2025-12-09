

def fle():
    file = 'input.txt'
    f = open(file,'r')
    papers = []
    for line in f:
        line = list(line[:-1])
        line.append('.')
        line.insert(0,'.')
        papers.append(line)
    f.close()
    init = []
    for i in range(len(papers[0])):
        init.append('.')
    papers.append(init)
    papers.insert(0,init)
    return papers

def numAround(papers,locx,locy):
    num = 0
    if papers[locy-1][locx-1] == '@':
        num+=1
    if papers[locy][locx-1] == '@':
        num+=1
    if papers[locy+1][locx-1] == '@':
        num+=1
    if papers[locy-1][locx] == '@':
        num+=1
    if papers[locy+1][locx] == '@':
        num+=1
    if papers[locy-1][locx+1] == '@':
        num+=1
    if papers[locy][locx+1] == '@':
        num+=1
    if papers[locy+1][locx+1] == '@':
        num+=1
    return num

def print_around(papers,locx,locy):
    print(papers[locy-1][locx-1]+papers[locy-1][locx]+papers[locy-1][locx+1])
    print(papers[locy][locx-1]+papers[locy][locx]+papers[locy][locx+1])
    print(papers[locy+1][locx-1]+papers[locy+1][locx]+papers[locy+1][locx+1])

def pt1(papers):
    accessable_rolls = 0
    removable_rolls = []
    for i in range(1,len(papers)-1):
        for j in range(1,len(papers[0])-1):
            if numAround(papers,j,i)<4 and papers[i][j]=='@':
                accessable_rolls += 1
                removable_rolls.append([i,j])
    #print(f"There are {accessable_rolls} accessible rolls in this pass.")
    return accessable_rolls,removable_rolls

def clearRolls(papers,removable_rolls):
    for roll in removable_rolls:
        papers[roll[0]][roll[1]] = '.'
    return papers

def pt2(papers):
    total_removed = 0
    accessable = 1
    while accessable != 0:
        accessable = 0
        accessable,to_remove = pt1(papers)
        papers = clearRolls(papers,to_remove)
        total_removed += accessable
    print(f"The total number of rolls that can be removed is {total_removed}")

def main():
    papers = fle()
    print("Solving part 1")
    pt1(papers)
    print("Solving part 2")
    pt2(papers)

main()