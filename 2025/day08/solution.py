
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

def mergeSortLength(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSortLength(leftHalf)
    sortedRight = mergeSortLength(rightHalf)

    return mergeLength(sortedLeft,sortedRight)

def mergeLength(left,right):
    result = []
    i = j= 0

    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def inCircuits (pair,circuits):
    for circuit in circuits:
        for connection in circuit:
            if pair[1] == connection[1]:
                circuit.append(pair)
                return circuits
            elif pair[2] == connection[1]:
                circuit.append(pair)
                return circuits
            elif pair[2] == connection[2]:
                circuit.append(pair)
                return circuits
            elif pair[1] == connection[2]:
                circuit.append(pair)
                return circuits
        
    circuits.append([pair])
    return circuits

def combineGroups(circuits):
    nodes_in_groups = []
    for circuit in circuits:
        group = set()
        for pair in circuit:
            group.add(pair[1])
            group.add(pair[2])
        nodes_in_groups.append(group)
    merged_groups = []
    to_remove = []
    for x in range(len(nodes_in_groups)-1):
        for y in range(x+1,len(nodes_in_groups)):
            if len(nodes_in_groups[x].intersection(nodes_in_groups[y])) > 0:
                new_group = nodes_in_groups[x].union(nodes_in_groups[y])
                to_remove.append(nodes_in_groups[x])
                to_remove.append(nodes_in_groups[y])
                merged_groups.append(new_group)
                break
        if to_remove != []:
            break
    #print(to_remove)
    if to_remove != []:
        for rem in to_remove:
            if rem in nodes_in_groups:
                nodes_in_groups.remove(rem)
    merged_groups = merged_groups + nodes_in_groups
    return merged_groups

def combineGroups2(groups):
    merged_groups = []
    to_remove = []
    for x in range(len(groups)-1):
        for y in range(x+1,len(groups)):
            if len(groups[x].intersection(groups[y])) > 0:
                new_group = groups[x].union(groups[y])
                to_remove.append(groups[x])
                to_remove.append(groups[y])
                merged_groups.append(new_group)
                break
        if to_remove != []:
            break
    for rem in to_remove:
        if rem in groups:
            groups.remove(rem)
    merged_groups = merged_groups + groups
    return merged_groups

def inpHandle():
    file = './input.txt'
    f = open(file,'r')
    boxes = []
    for line in f:
        line = line.split(',')
        boxes.append((int(line[0]),int(line[1]), int(line[2])))
    f.close()
    if file == './test.txt':
        tries = 10
    else:
        tries = 999
    return boxes,tries

def printCircuits(circuits):
    for circuit in circuits:
        print("\n")
        for pair in circuit:
            print(pair)

def printDistances(boxes):
    for dist in boxes:
        print(dist)

def pt1(boxes,tries):
    dis_sqr = []
    for x in range(len(boxes)-1):
        for y in range(x+1,len(boxes)):
            dis = (boxes[x][0]-boxes[y][0])**2 + (boxes[x][1]-boxes[y][1])**2 + (boxes[x][2]-boxes[y][2])**2
            dis_sqr.append((dis,boxes[x],boxes[y]))
    
    dis_sqr = mergeSort(dis_sqr)
    #printDistances(dis_sqr)
    circuits = []
    for i in range(tries):
        pair = dis_sqr.pop(0)
        circuits = inCircuits(pair,circuits)
    
    circuits = mergeSortLength(circuits)
    connected_boxes = combineGroups(circuits)
    connected_boxes = mergeSortLength(connected_boxes)
    print(f"{len(connected_boxes)}")
    any_change = 1
    while any_change:
        oldbox = connected_boxes
        connected_boxes = combineGroups2(connected_boxes)
        connected_boxes = mergeSortLength(connected_boxes)
        if len(oldbox) == len(connected_boxes):
            any_change = 0
    print(f"The three largest circuits have length {len(connected_boxes[-1])}, {len(connected_boxes[-2])}, and {len(connected_boxes[-3])}\nMultiplied together the result is {len(connected_boxes[-1])*len(connected_boxes[-2])*len(connected_boxes[-3])}")
    print(f"There are {len(connected_boxes)} connected circuits")


def addBox(pair,circuits):
    addd = 0
    for circuit in circuits:
        if pair[1] in circuit or pair[2] in circuit:
            circuit.add(pair[1])
            circuit.add(pair[2])
            addd = 1
    if not addd:
        circuits.append({pair[1],pair[2]})
    return circuits

def mergeCircuits(circuits):
    merged_groups = []
    to_remove = []
    for x in range(len(circuits)-1):
        for y in range(x+1,len(circuits)):
            if len(circuits[x].intersection(circuits[y])) > 0:
                new_group = circuits[x].union(circuits[y])
                to_remove.append(circuits[x])
                to_remove.append(circuits[y])
                merged_groups.append(new_group)
                break
        if to_remove != []:
            break
    for rem in to_remove:
        if rem in circuits:
            circuits.remove(rem)
    merged_groups = merged_groups + circuits
    return merged_groups


def pt2(boxes,tries):
    #get the distances between every two nodes and sort them
    sq_dis = []
    for x in range(len(boxes)-1):
        for y in range(x+1,len(boxes)):
            dis = (boxes[x][0]-boxes[y][0])**2 + (boxes[x][1]-boxes[y][1])**2 + (boxes[x][2]-boxes[y][2])**2
            sq_dis.append((dis,boxes[x],boxes[y]))
    sq_dis = mergeSort(sq_dis)

    boxes = set(boxes)
    circuits = [{sq_dis[0][1],sq_dis[0][2]}]
    sq_dis.pop(0)
    tries -= 2
    i = 0
    while len(boxes) != len(circuits[0]):
        to_add = sq_dis.pop(0)
        circuits = addBox(to_add,circuits)
        circuits = mergeCircuits(circuits)
        if i == tries:
            circuits = mergeSortLength(circuits)
            print(f"The three largest circuits have length {len(circuits[-1])}, {len(circuits[-2])}, and {len(circuits[-3])}\nMultiplied together the result is {len(circuits[-1])*len(circuits[-2])*len(circuits[-3])}")
        i += 1

    
    print(F"The final two boxes connected are {to_add[1]} and {to_add[2]}.\nTheir X values multiplied together is {to_add[1][0]*to_add[2][0]}")


    return 0
def main():
    boxes, tries = inpHandle()
    pt1(boxes,tries)
    print("Starting Part 2")
    pt2(boxes,tries)

main()