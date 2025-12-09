
def getfile():
    file = "./input.txt"
    f = open(file,'r')
    enter = []
    for line in f:
        enter = line.split(',')
    for i in range(len(enter)):
        enter[i] = enter[i].split('-')
    for i in range(len(enter)):
        enter[i][0] = int(enter[i][0])
        enter[i][1] = int(enter[i][1])
    return enter

def pt1(ids):
    running_sum = 0
    for id in ids:
        #no_invalids = 0
        for i in range(id[0],id[1]+1):
            if len(str(i)) % 2 ==0:
                splitpoint = int(len(str(i))/2)
                if str(i)[:splitpoint] == str(i)[splitpoint:]:
                    #no_invalids = 1
                    #print(f"The ID {i} is invalid.")
                    running_sum += i
        #if not no_invalids:
            #print(f"{id[0]}-{id[1]} has no invalid IDs")

    print(f"The sum of invalid IDs is {running_sum}")
    return 0

def chunk (string,n):
    res = []
    for i in range(0,len(string),n):
        res.append(string[i:i+n])
    return res

def pt2(ids):
    running_sum = 0
    for id in ids:
        #no_invalids = 0
        for i in range(id[0],id[1]+1):
            for j in range(1,len(str(i))):
                if len(str(i))%j ==0:
                    parts = chunk(str(i),j)
                    if parts.count(parts[0]) == len(parts):
                        running_sum += i
                        #print(f"{i} is an invalid ID")
                        break
        #if not no_invalids:
            #print(f"{id[0]}-{id[1]} has no invalid IDs")

    print(f"The sum of invalid IDs is {running_sum}")
    return 0

def main():
    ids = getfile()
    #for id in ids:
    #    print(f"The ids start at {id[0]} and end at {id[1]}")
    #print(type(ids[0][0]))
    print("Part 1 soln")
    pt1(ids)
    print("Part 2 soln")
    pt2(ids)
    return 0
main()