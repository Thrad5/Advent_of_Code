
class Beam:
    def __init__(self,x,value=1):
        self.x = x
        self.value = value
    def __eq__(self, other):
        if isinstance(other,Beam):
            return self.x == other.x
        else:
            return self.x == other

def inpHandle():
    file = './test.txt'
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


def mergeSortBeam(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSortBeam(leftHalf)
    sortedRight = mergeSortBeam(rightHalf)

    return mergeBeam(sortedLeft,sortedRight)

def mergeBeam(left,right):
    result = []
    i = j= 0

    while i < len(left) and j < len(right):
        if left[i].x < right[j].x:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def condenseBeam(beams):
    beams = mergeSortBeam(beams)
    for beam in beams:
                    print(f"Tachyon beam at {beam.x} with value {beam.value}.")
    condensed_beams = beams
    return condensed_beams


def solveRun2(start,splitters,y):
    beams = [[start,1]]
    row = 0
    num_splits = 0
    while row <= y-1:
        beams_temp = []
        print(f"Row number {row}")
        did_break = 0
        for splitter in splitters:
            repeat_split = 0
            if splitter[0] > row:
                #Deal with beams
                beams = beams_temp + beams
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
            beams = beams_temp + beams
            #Deal with beams
            row += 1
    print(f"There are {num_splits} splits in the manifold")
    print(f"The number of splitters is {len(splitters)}")
    total = 0
    for beam in beams:
        total += beam[1]
    print(f"The total number of paths is {total}")



def main():
    start,splitters,y,max_x = inpHandle()
    t_beams = [Beam(start,1)]
    row = 0
    num_splits = 0
    splitters = mergeSort(splitters)
    #print(splitters)
    
    while row <= y-1:
        t_beams_temp = []
        print(f'Row number {row}')
        #for beam in t_beams:
            #print(f"Tachyon beam at {beam.x} with value {beam.value}.")
        did_break = 0
        for splitter in splitters:
            repeat_split = 0
            if splitter[0] > row: #There are no more splitters on the same level so need to
                #prepare for the next row
                t_beams = t_beams_temp + t_beams
                t_beams = condenseBeam(t_beams)
                row += 1
                did_break = 1
                break
            elif splitter[0] == row:
                if splitter[1] in t_beams:
                    for t_beam in t_beams:
                        if t_beam == splitter[1]:
                            if not repeat_split:
                                repeat_split = 1
                                num_splits += 1
                            t_beams_temp.append(Beam(splitter[1]-1,t_beam.value))
                            t_beams_temp.append(Beam(splitter[1]+1,t_beam.value))
                            t_beams.remove(t_beam)
        if not did_break:
            t_beams = t_beams_temp + t_beams
            t_beams = condenseBeam(t_beams)
            row += 1
    
    t_beams = t_beams_temp + t_beams
    t_beams = condenseBeam(t_beams)

    print(f"There are {num_splits} splits in the manifold")
    print(f"The number of splitters is {len(splitters)}")
    total = 0
    for t_beam in t_beams:
        total += t_beam.value
    print(f"There are {total} paths in this manifold")
    print("\nThis is the second attempt\n")
    solveRun2(start,splitters,y)
    
main()


b1 = Beam(5,9)
b2 = Beam(5,10)
b3 = Beam(5)
b3.value = b1.value+b2.value

print(b3.value)