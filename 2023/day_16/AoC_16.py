'''
Created on 23:57:20
author: @ram86
'''

# Orientations
# 0 - North
# 1 - East
# 2 - South
# 3 - West

# Position [x,y] 
# x is east west
# y is north south
import copy

class FrontOfBeam():
    def __init__(self,current_pos,facing,xMax,yMax):
        self.curr = current_pos
        self.facing = facing
        self.moving = True
        self.xMax = xMax
        self.yMax = yMax
    
    def __str__(self):
        return f"Beam object at {self.curr}, facing {self.facing}, is moving {self.moving}"

    def continueStraight(self):
        if self.moving:
            if not(self.willHitWall()):
                if self.facing == 0:
                    self.curr[1] -= 1
                elif self.facing == 1:
                    self.curr[0] += 1
                elif self.facing == 2:
                    self.curr[1] += 1
                else:
                    self.curr[0] -= 1
            else:
                self.moving = False

    def willHitWall(self):
        if self.facing == 0:
            if self.curr[1] <= 0:
                return True
        elif self.facing == 1:
            if self.curr[0] >= xMax:
                return True
        elif self.facing == 2:
            if self.curr[1] >= yMax:
                return True
        else:
             if self.curr[0] <= 0:
                 return True
        return False
    

def barSplitter(fob: FrontOfBeam):
    new = 0
    if fob.facing % 2 == 1 and fob.moving:
        fob.facing = 0
        new = FrontOfBeam(copy.copy(fob.curr),2,fob.xMax,fob.yMax)
    return fob,new

def dashSplitter(fob: FrontOfBeam):
    new = 0
    if fob.facing % 2 == 0 and fob.moving:
        fob.facing = 1
        new = FrontOfBeam(copy.copy(fob.curr),3,fob.xMax,fob.yMax)
    return fob,new

def bSlashRef(fob: FrontOfBeam):
    if fob.moving:
        if fob.facing == 0:
            fob.facing = 3
        elif fob.facing == 1:
            fob.facing = 2
        elif fob.facing == 2:
            fob.facing = 1
        else:
            fob.facing = 0
    return fob

def fSlashRef(fob: FrontOfBeam):
    if fob.moving:
        if fob.facing == 0:
            fob.facing = 1
        elif fob.facing == 1:
            fob.facing = 0
        elif fob.facing == 2:
            fob.facing = 3
        else:
            fob.facing = 2
    return fob

def stillMoving(manyBeams:list[FrontOfBeam]):
    for beam in manyBeams:
        if beam.moving:
            return True
    return False

def walkingStep(manyBeamsW,contraptionM,hashM):
    for i in range(len(manyBeamsW)):
        hashM[manyBeamsW[i].curr[1]][manyBeamsW[i].curr[0]] = '#'
        if contraptionM[manyBeamsW[i].curr[1]][manyBeamsW[i].curr[0]] == '.':
            pass
        elif contraptionM[manyBeamsW[i].curr[1]][manyBeamsW[i].curr[0]] == '|':
            manyBeamsW[i],new = barSplitter(manyBeamsW[i])
            if new != 0:
                new.continueStraight()
                manyBeamsW.append(new)
        elif contraptionM[manyBeamsW[i].curr[1]][manyBeamsW[i].curr[0]] == '-':
            manyBeamsW[i],new = dashSplitter(manyBeamsW[i])
            if new != 0:
                new.continueStraight()
                manyBeamsW.append(new)
        elif contraptionM[manyBeamsW[i].curr[1]][manyBeamsW[i].curr[0]] == '/':
            manyBeamsW[i] = fSlashRef(manyBeamsW[i])
        elif contraptionM[manyBeamsW[i].curr[1]][manyBeamsW[i].curr[0]] == 'a':
            manyBeamsW[i] = bSlashRef(manyBeamsW[i])
        else:
            print(f"Unexpected character{contraptionM[manyBeamsW[i].curr[1]][manyBeamsW[i].curr[0]]}")
        manyBeamsW[i].continueStraight()
    return manyBeamsW,hashM

def numOfHashes(hashMap):
    total = 0
    for line in hashMap:
        for char in line:
            if char == '#':
                total +=1
    return total

def printList(ha,con,loc,total):
    print(f'Step {total}')
    for i in range(len(ha)):
        print(''.join(ha[i]), ' ', ''.join(con[i]), ' ', ''.join(loc[i]))

def findNumEnergised(x,y,facing,contraption,xMax,yMax):
    starting_beam = FrontOfBeam([x,y],facing,xMax,yMax)
    beams = [starting_beam]
    hashChart = copy.deepcopy(contraption)
    prevHash = -2
    currHash = -1
    total = 0
    patience = 10
    numTimesPatient = 0
    while True:
        if prevHash == currHash and patience == numTimesPatient:
            break
        elif prevHash == currHash:
            numTimesPatient += 1
        else:
            numTimesPatient = 0
        prevHash = currHash
        beams,hashChart = walkingStep(beams,contraption,hashChart)
        beamLoc = copy.deepcopy(contraption)
        for beam in beams:
            if beam.moving:
                beamLoc[beam.curr[1]][beam.curr[0]] = 'o'
        currHash = numOfHashes(hashChart)
        #printList(hashChart,contraption,beamLoc,total)
        total +=1

    beams,hashChart = walkingStep(beams,contraption,hashChart)
    return numOfHashes(hashChart)


contraption = []
with open('input.txt','r') as file:
    for line in file:
        contraption.append(list(line)[:-1])

xMax = len(contraption[0])-1
yMax = len(contraption)-1
maxHash = 0
for i in range(len(contraption[0])):
    testHash = findNumEnergised(i,0,2,contraption,xMax,yMax)
    if testHash > maxHash:
        maxHash = testHash
        print(f"New Max: {maxHash} from start [{i},0]")
    testHash = findNumEnergised(i,yMax,0,contraption,xMax,yMax)
    if testHash > maxHash:
        maxHash = testHash
        print(f"New Max: {maxHash} from start [{i},{yMax}]")
for i in range(len(contraption[0])):
    testHash = findNumEnergised(0,i,1,contraption,xMax,yMax)
    if testHash > maxHash:
        maxHash = testHash
        print(f"New Max: {maxHash} from start [0,{i}]")
    testHash = findNumEnergised(xMax,i,3,contraption,xMax,yMax)
    if testHash > maxHash:
        maxHash = testHash
        print(f"New Max: {maxHash} from start [{xMax},{i}]")

print(maxHash)

'''
print('map')
for line in contraption:
    print(''.join(line))
print('Step 0')
for line in hashChart:
    print(''.join(line))
beams,hashChart = walkingStep(beams,contraption,hashChart)
print('Step 1')
for line in hashChart:
    print(''.join(line))
beams,hashChart = walkingStep(beams,contraption,hashChart)
print('Step 2')
for line in hashChart:
    print(''.join(line))
beams,hashChart = walkingStep(beams,contraption,hashChart)
print('Step 3')
for line in hashChart:
    print(''.join(line))
beams,hashChart = walkingStep(beams,contraption,hashChart)
print('Step 6')
for line in hashChart:
    print(''.join(line))
beams,hashChart = walkingStep(beams,contraption,hashChart)
print('Step 5')
for line in hashChart:
    print(''.join(line))
beams,hashChart = walkingStep(beams,contraption,hashChart)
print('Step 7')
for line in hashChart:
    print(''.join(line))
beams,hashChart = walkingStep(beams,contraption,hashChart)
print('Step 8')
for line in hashChart:
    print(''.join(line))
'''

