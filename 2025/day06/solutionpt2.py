
def inpHandle():
    file = './input.txt'
    f = open(file,'r')
    maths = []
    for line in f:
        line = line[:-1]
        maths.append(line)
    f.close()

    num_rows = len(maths)
    for i in range(len(maths[0])):
        col = []
        for j in range(num_rows):
            col.append(maths[j][i])
        if len(col) != col.count(' '):
            for j in range(num_rows-1):
                if maths[j][i] == ' ':
                    if i +1 == len(maths[0]):
                        maths[j] = maths[j][:i] + "a"
                    else:
                        maths[j] = maths[j][:i] + "a" + maths[j][i+1:]
    
    for j in range(len(maths)):
        maths[j] = maths[j].split()
    
    equations = [] 
    for b in range(len(maths[0])):
        index = len(maths[0][b])
        equation = []
        for j in range(index):
            number = ""
            for i in range(len(maths)-1):
                number += maths[i][b][j]
            equation.append(number)
        equation.append(maths[-1][b])
        equations.append(equation)

    for equation in equations:
        for i in range(len(equation)-1):
            equation[i] = int(equation[i].replace('a'," "))
    return equations


def pt2(maths):
    total = 0
    for i in range(len(maths)):
        print(maths[i])
        if maths[i][-1] == '+':
            subtotal = 0
            for j in range(len(maths[i])-1):
                subtotal += maths[i][j]
        else:
            subtotal = 1
            for j in range(len(maths[i])-1):
                subtotal *= maths[i][j]
        #print(f"The total is {subtotal}")
        total += subtotal
    print(f"The grand total is {total}")

def main():
    print('Starting')
    maths = inpHandle()
    pt2(maths)
    #for line in maths:
        #print(line)

main()