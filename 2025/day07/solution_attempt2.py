
def inpHandle():
    file = './input.txt'
    f = open(file,'r')
    start = 0
    splitters = []
    y = 0
    for line in f:
        max_x = len(line)
        for x in range(len(line)):
            if line[x] == "S":
                start = x
            elif line[x] == '^':
                splitters.append((y,x))
        y += 1
    f.close()
    return start, splitters,y,max_x

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft,sortedRight)

def merge(left,right):
    result = []
    i = j= 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def combineBeams(beams:list):
    beams = mergeSort(beams)
    temp_beams = []
    for i in range(len(beams)):
        if temp_beams == []:
            temp_beams.append(beams[0])
        else:
            x_in = 0
            for temp in temp_beams:
                if temp[0] == beams[i][0]:
                    x_in = 1
            if not x_in:
                temp_beams.append(beams[i])
    for temp_beam in temp_beams:
        beams.remove(temp_beam)
    for beam in beams:
        for temp in temp_beams:
            if temp[0] == beam[0]:
                temp[1] = temp[1] + beam[1]
    beams = temp_beams
    return beams


def solveRun2(start,splitters,y):
    beams = [[start,1]]
    row = 0
    num_splits = 0
    while row <= y-1:
        beams_temp = []
        did_break = 0
        for splitter in splitters:
            repeat_split = 0
            if splitter[0] > row:
                #Deal with beams
                beams = beams_temp + beams
                beams = combineBeams(beams)
                row +=1
                did_break = 1
                break
            elif splitter[0] == row:
                to_remove = []
                for beam in beams:
                    if splitter[1] == beam[0]:
                        if not repeat_split:
                            repeat_split = 1
                            num_splits += 1
                        beams_temp.append([beam[0]-1,beam[1]])
                        beams_temp.append([beam[0]+1,beam[1]])
                        to_remove.append(beam)
                for rem in to_remove:
                    beams.remove(rem)
        if not did_break:
            #Deal with beams
            beams = beams_temp + beams
            beams = combineBeams(beams)
            row += 1
    print(f"There are {num_splits} splits in the manifold")
    total = 0
    for beam in beams:
        total += beam[1]
    print(f"The total number of paths is {total}")



def main():
    start,splitters,y,max_x = inpHandle()
    splitters = mergeSort(splitters)
    solveRun2(start,splitters,y)
    
main()
