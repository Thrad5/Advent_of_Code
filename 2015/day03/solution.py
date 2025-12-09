
def main():
    file = './input.txt'
    f = open(file,'r')
    position = [0,0]
    visited = {(0,0)}
    pos_y_2_S = [0,0]
    pos_y_2_R = [0,0]
    visited_y_2 = {(0,0)}
    for line in f:
        for x in range(len(line)):
            if line[x] == '^':
                position[0] += 1
                if x %2 == 0:
                    pos_y_2_R[0] += 1
                else:
                    pos_y_2_S[0] +=1
            elif line[x] == 'v':
                position[0] -= 1
                if x %2 == 0:
                    pos_y_2_R[0] -= 1
                else:
                    pos_y_2_S[0] -=1
            elif line[x] == '>':
                position[1] += 1
                if x %2 == 0:
                    pos_y_2_R[1] += 1
                else:
                    pos_y_2_S[1] +=1
            else:
                position[1] -= 1
                if x %2 == 0:
                    pos_y_2_R[1] -= 1
                else:
                    pos_y_2_S[1] -=1
            visited.add(tuple(position))
            visited_y_2.add(tuple(pos_y_2_S))
            visited_y_2.add(tuple(pos_y_2_R))
    f.close()
    print(f"Santa delivers presents to {len(visited)} houses.")
    print(f"Next year Santa and Robot Santa deliver presents to {len(visited_y_2)} houses.")


main()