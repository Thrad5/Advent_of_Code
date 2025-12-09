
def inpHandle():
    file = './input.txt'
    f = open(file,'r')
    mode = 0
    stock = []
    fresh_ingredients = []
    for line in f:
        if line == "\n":
            mode = 1
        else:
            if mode:
                stock.append(int(line))
            else:
                line = line.split('-')
                line[0] = int(line[0])
                line[1] = int(line[1])
                fresh_ingredients.append([line[0],line[1]])
    return fresh_ingredients,stock

def pt1(fresh_ingredients, stock):
    number_fresh = 0
    for item in stock:
        for rang in fresh_ingredients:
            if rang[0] <= item <= rang[1]:
                number_fresh+=1
                break
    print(f"There are {number_fresh} items in stock")

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


def cleanIDs(fresh_ingredients,j):
    ids_to_remove = []
    for i in range(j+1,len(fresh_ingredients)):
        if fresh_ingredients[i][0] > fresh_ingredients[j][1]:
            break
        if fresh_ingredients[i][1]<=fresh_ingredients[j][1]:
            ids_to_remove.append(fresh_ingredients[i])
        elif fresh_ingredients[i][1] > fresh_ingredients[j][1]:
            fresh_ingredients[j][1] = fresh_ingredients[i][1]
            ids_to_remove.append(fresh_ingredients[i])
    for ids in ids_to_remove:
        fresh_ingredients.remove(ids)
    return fresh_ingredients, len(ids_to_remove)

def pt2(fresh_ingredients):
    i = 0
    while i <= len(fresh_ingredients):
        fresh_ingredients,num_removed = cleanIDs(fresh_ingredients,i)
        if num_removed == 0:
            i += 1
    number_of_ids = 0
    for line in fresh_ingredients:
        number_of_ids += line[1] - line[0] + 1
        print(line)
    print(f"There are {number_of_ids} ids available")

def main():
    fresh_ingredients,stock = inpHandle()
    print("Solving Part1")
    pt1(fresh_ingredients,stock)
    print("Solving Part 2")
    fresh_ingredients = mergeSort(fresh_ingredients)
    for line in fresh_ingredients:
        print(line)
    pt2(fresh_ingredients)

main()
