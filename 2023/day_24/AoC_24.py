'''
17:56:10 24/12/23
'''

def findTimes(posVol1,posVol2):
    try:
        timex = (posVol2[0][0]-posVol1[0][0])/(posVol1[1][0]-posVol2[1][0])
    except ZeroDivisionError:
        print("X is 0")
        timex = 999
    try:
        timey = (posVol2[0][1]-posVol1[0][1])/(posVol1[1][1]-posVol2[1][1])
    except ZeroDivisionError:
        print("Y is 0")
        timey = 999
    return timex,timey

def isParallell(posVol1,posVol2):
    #if (posVol1[1][0]/posVol2[1][0]) == (posVol1[1][1]/posVol2[1][1]):
            #return True
    if (posVol1[1][0]/posVol2[1][0]) == (posVol1[1][2]/posVol2[1][2]):
        return True
    if (posVol1[1][2]/posVol2[1][2]) == (posVol1[1][1]/posVol2[1][1]):
        return True
    else:
        return False

def intersectPoints(posVol1,posVol2):
    LHS = (posVol2[1][0]/posVol2[1][1])-(posVol1[1][0]/posVol1[1][1])
    RHS = (((posVol2[0][1]*posVol2[1][0])/posVol2[1][1])-((posVol1[0][1]*posVol1[1][0])/posVol1[1][1]))+posVol1[0][0]-posVol2[0][0]
    ypos = RHS/LHS
    xpos = ypos * (posVol1[1][0]/posVol1[1][1]) - (posVol1[0][1]*posVol1[1][0])/posVol1[1][1] + posVol1[0][0]
    timea= (ypos-posVol1[0][1])/posVol1[1][1]
    timeb = (ypos-posVol2[0][1])/posVol2[1][1]
    return xpos,ypos,timea,timeb
posVol = []
with open('input.txt','r') as file:
    for line in file.readlines():
        posVol1 = line[:-1].split('@')
        for i in range(2):
            posVol1[i] = posVol1[i].split(',')
            for j in range(3):
                posVol1[i][j] = int(posVol1[i][j])
        posVol.append(posVol1)

num_of_intersections = 0
minloc = 200000000000000
maxloc = 400000000000000
for i in range(len(posVol)-1):
    for j in range(i+1,len(posVol)):
        
        if isParallell(posVol[i],posVol[j]):
            print('Is Paralell')
            print('Hailstone A:',posVol[i])
            print('Hailstone B:',posVol[j])
        

print(num_of_intersections)
