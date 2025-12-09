
def main():
    file = './input.txt'
    f = open(file,'r')
    floor = 0
    basement_entry = 0
    first_entry = 0
    for line in f:
        #print(line)
        for x in range(len(line)):
            if line[x] == '(':
                floor += 1
            else:
                floor -=1
            if floor < 0 and not first_entry:
                basement_entry = x+1
                first_entry = 1
    f.close()
    print(f"The instructions take Santa to floor {floor}")
    print(f"Santa first enters the basement on instruction {basement_entry}")

main()