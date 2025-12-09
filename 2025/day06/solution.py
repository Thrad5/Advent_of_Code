
def inpHandle():
    file = './input.txt'
    f = open(file,'r')
    maths = []
    for line in f:
        line = line.split()
        #print(line)
        if not ((line[0] == '*' and not line[0] == '+') or (not line[0] == '*' and line[0] == '+')):
            for i in range(len(line)):
                #print(line[i])
                line[i] = int(line[i])
        maths.append(line)
    f.close()
    return maths

def pt1(maths):
    total = 0
    num_of_nums = len(maths)-1
    for i in range(len(maths[0])):
        if maths[-1][i] == '+':
            subtotal = 0
            for j in range(0,num_of_nums):
                subtotal += maths[j][i]
        else:
            subtotal = 1
            for j in range(0,num_of_nums):
                subtotal *= maths[j][i]
        #print(f"The total is {subtotal}")
        total += subtotal
    print(f"The grand total is {total}")

def main():
    print('Starting')
    maths = inpHandle()
    pt1(maths)

main()