'''
Created 21:34:00 10/12/23

author: @ram86
'''

import numpy as np

def new_layer(layer):
    layer1 = []
    for i in range(len(layer)):
        layer1_i = []
        for j in range(len(layer[i])-1):
            layer1_i.append(layer[i][j+1]-layer[i][j])
        layer1.append(layer1_i)
    return layer1

def printlayers(layer):
    for i in range(len(layer)):
        print(layer[i])

def all_equal(lst):
    return lst[:-1] == lst[1:]

def next_num_up(layer,currNum):
    nextNum = layer[0]-currNum
    return nextNum


initial = np.loadtxt("D:\\!Advent_of_Code\\2023\\day_9\\input.txt",dtype = 'int')
print(len(initial))
layer1 = new_layer(initial)
layer2 = new_layer(layer1)
layer3 = new_layer(layer2)
layer4 = new_layer(layer3)

layer5 = new_layer(layer4)
layer6 = new_layer(layer5)
layer7 = new_layer(layer6)
layer8 = new_layer(layer7)
layer9 = new_layer(layer8)
layer10 = new_layer(layer9)
layer11 = new_layer(layer10)
layer12 = new_layer(layer11)
layer13 = new_layer(layer12)
layer14 = new_layer(layer13)
layer15 = new_layer(layer14)
layer16 = new_layer(layer15)
layer17 = new_layer(layer16)
layer18 = new_layer(layer17)
layer19 = new_layer(layer18)

nextNum = 0
for i in range(len(initial)):
    temp = next_num_up(layer18[i],0)
    temp = next_num_up(layer17[i],temp)
    temp = next_num_up(layer16[i],temp)
    temp = next_num_up(layer15[i],temp)
    temp = next_num_up(layer14[i],temp)
    temp = next_num_up(layer13[i],temp)
    temp = next_num_up(layer12[i],temp)
    temp = next_num_up(layer11[i],temp)
    temp = next_num_up(layer10[i],temp)
    temp = next_num_up(layer9[i],temp)
    temp = next_num_up(layer8[i],temp)
    temp = next_num_up(layer7[i],temp)
    temp = next_num_up(layer6[i],temp)
    temp = next_num_up(layer5[i],temp)
    temp = next_num_up(layer4[i],temp)
    temp = next_num_up(layer3[i],temp)
    temp = next_num_up(layer2[i],temp)
    temp = next_num_up(layer1[i],temp)
    temp = next_num_up(initial[i],temp)
    print(temp)
    nextNum += temp

print(nextNum)

