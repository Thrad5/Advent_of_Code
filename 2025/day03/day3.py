
def enter():
    file = "./input.txt"
    f = open(file,'r')
    inp = []
    for line in f:
        l = []
        for i in line[:-1]:
            l.append(int(i))
        inp.append(l)
    f.close()
    return inp

def pt1(banks):
    max_joltage = 0
    for bank in banks:
        first_digit = 0
        first_digit_loc = 0
        for i in range(len(bank)-1):
            if bank[i] > first_digit:
                first_digit = bank[i]
                first_digit_loc = i
                if first_digit == 9:
                    break
        second_digit = 0
        for i in range(first_digit_loc+1,len(bank)):
            if bank[i] > second_digit:
                second_digit = bank[i]
                if second_digit == 0:
                    break
        joltage = int(str(first_digit)+str(second_digit))
        max_joltage += joltage
        #print(f"The joltage of this bank is {joltage}")
    print(f"The max joltage is {max_joltage}")

def maxValue(bank, starting,end):
    digit = 0
    digit_place = 0
    for i in range(starting,len(bank)-end):
        if bank[i] > digit:
            digit = bank[i]
            digit_place = i
            if digit == 9:
                break
    return digit_place

def pt2(banks):
    max_joltage = 0
    for bank in banks:
        number_of_digits = 12
        joltage = ''
        digit_marker = 0
        while number_of_digits > 0:
            number_of_digits -=1
            digit_marker = maxValue(bank, digit_marker, number_of_digits)
            joltage += str(bank[digit_marker])
            digit_marker +=1
        #print(f"The highest joltage of this bank is {joltage}")
        max_joltage += int(joltage)
    print(f"The max joltage is {max_joltage}")

def main():
    banks = enter()
    print("Solving part 1")
    pt1(banks)
    print("solving part 2")
    pt2(banks)

main()