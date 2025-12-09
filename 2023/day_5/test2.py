
# %%
import matplotlib.pyplot as plt
import numpy as np
#%%

seedstarts = [[858905075, 56936593], 
[947763189, 267019426] ,
[206349064, 252409474] ,
[660226451, 92561087] ,
[752930744, 24162055] ,
[75704321 , 63600948] ,
[3866217991,323477533] ,
[3356941271,54368890] ,
[1755537789,475537300] ,
[1327269841,427659734]]
# %%
seeds = []
for i in range(0,10):
    seeds.append([seedstarts[i][0],(seedstarts[i][0]+seedstarts[i][1])])
print(seeds)

#%%
plt.figure()
for i in range(0,10):
    plt.plot((seeds[i]),(seeds[i]))
plt.show()
# %%
tt = np.array([44,80,65,72])
dr = np.array([208,1581,1050,1102])
thmin = (tt - np.sqrt(tt*tt-4*dr))/2
thmax = (tt + np.sqrt(tt*tt-4*dr))/2
print(thmin)
print(thmax)
# %%
tt = np.array([7 , 15 ,  30])
dr = np.array([9,  40 , 200])
thmin = (tt - np.sqrt(tt*tt-4*dr))/2
thmax = (tt + np.sqrt(tt*tt-4*dr))/2
print(thmin)
print(thmax)
# %%
plt.figure()
for i in range(0,len(tt)):
    timeheld = np.arange(0,tt[i]+1,1)
    distance = (tt[i]-timeheld)*timeheld
    plt.plot(timeheld,distance)
    plt.axhline(dr[i])
plt.show()
# %%
maxh = (tt-tt/2)*(tt/2)
print(maxh)

# %%
validTimes = np.sqrt(tt**2-4*dr)
print(validTimes)
for i in range(0,len(validTimes)):
    if np.round(validTimes[i]) ==validTimes[i]:
        validTimes[i] = validTimes[i] -1
    else:
        validTimes[i] = round(validTimes[i])
print(validTimes)
# %%
moe = 1
for i in range(0,len(tt)):
    moe = moe*validTimes[i]
print(moe)
# %%
