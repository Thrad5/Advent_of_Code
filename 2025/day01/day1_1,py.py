
def rotation (instruction, dial):
    to_add = abs(instruction[1]//100)
    dial_init = dial
    #print(f"This many greater than 100: {to_add}")
    instruction[1] = instruction[1] % 100
    if instruction[0] == "L":
        dial -= instruction[1]
        if dial <0 and dial_init!=0:
            to_add += 1
    else:
        dial += instruction[1]
        if dial > 100 and dial_init!=0:
            to_add += 1
    #print(f"{dial}, {to_add}")
    dial = dial % 100
    return dial,to_add

def getinst():
    file = "./input.txt"
    f = open(file,'r')
    instructions = []
    for line in f:
        #print(line)
        move = line[0]
        times = int(line[1:])
        instructions.append([move,times])
    return instructions
        


def main():
    instructions = getinst()
    #print(instructions)
    location = 50
    num_0s = 0
    print(f"The dial is at {location}")
    for i in range(len(instructions)):
        location,to_add = rotation(instructions[i],location)
        #print(f"The dial is now at {location}")
        num_0s += to_add
        if location == 0:
            num_0s +=1
    print(f"The dial hit 0 {num_0s} time(s)")

main()
