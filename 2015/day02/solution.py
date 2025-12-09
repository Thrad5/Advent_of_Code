
def main():
    file = './input.txt'
    f = open(file,'r')
    box_dims = []
    for line in f:
        line = line.split('x')
        box_dims.append([int(line[0]),int(line[1]),int(line[2])])
    f.close()
    total_sqft = 0
    total_ribbon = 0
    for box in box_dims:
        areas = [box[0]*box[1],box[0]*box[2],box[1]*box[2]]
        total_sqft += 2*areas[0] + 2*areas[1] + 2*areas[2] + min(areas)
        perimiters = [(box[0]+box[1])*2,(box[0]+box[2])*2,(box[1]+box[2])*2]
        total_ribbon += box[1] * box[0] * box[2] + min(perimiters)

    print(f"The total square feet of wrapping paper to order is {total_sqft}")
    print(f"The total feet of ribbon needed is {total_ribbon}")


main()