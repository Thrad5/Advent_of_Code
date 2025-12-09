'''
Created on 12:55:30 15/12/23
author:@ram96
'''

def find_hash (stringf):
    totalf = 0
    for characterf in stringf:
        totalf += ord(characterf)
        totalf *= 17
        totalf %= 256
    return totalf

def find_location(stringl,boxesl,boxNuml):
    possibleValues = [[stringl,1],[stringl,2],[stringl,3],[stringl,4],[stringl,5],[stringl,6],[stringl,7],[stringl,8],[stringl,9],]
    for i in possibleValues:
        try: 
            index = boxesl[boxNuml].index(i)
        except ValueError:
            continue
        else:
            return index




def remove_lense(stringr,boxesr):
    boxNumr = find_hash(stringr[:-1])
    x =  find_location(stringr[:-1],boxesr,boxNumr)
    if x != None:
        if len(boxesr[boxNumr]) == 1:
            boxesr[boxNumr] = [0]
            return boxesr
        else:
            j = find_location(stringr[:-1],boxesr,boxNumr)
            del boxesr[boxNumr][j]
            return boxesr
    else:
        return boxesr

def add_lens(stringa,boxesa):
    boxNuma = find_hash(stringa[:-2])
    x =  find_location(stringa[:-2],boxesa,boxNuma)
    if boxesa[boxNuma] == [0]:
        boxesa[boxNuma] = [[stringa[:-2],int(stringa[-1])]]
        return boxesa
    if x != None:
        j = find_location(stringa[:-2],boxesa,boxNuma)
        boxesa[boxNuma][j] = [stringa[:-2],int(stringa[-1])]
        return boxesa
    else:
        boxesa[boxNuma].append([stringa[:-2],int(stringa[-1])])
        return boxesa


def box_sum(boxs):
    subTotal = 0
    for i in range(len(boxs)):
        subTotal += boxs[i][1] *(i+1)
    return subTotal

with open('input.txt','r') as file:
    line = file.readline()[:-1].split(',')

total = 0
boxes = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
for string in line:
    if string[-1] == '-':
        boxes = remove_lense(string,boxes)
    elif string[-2] == '=':
        boxes = add_lens(string,boxes)
for i in range(len(boxes)):
    box = boxes[i]
    if box != [0]:
        total += box_sum(box)*(1+i)

print(total)

