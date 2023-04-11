import matplotlib.pyplot as plt
import math

Cg = 4472.14
Cs = 346

def func(f):
    Ba = 2*math.pi*f/Cs
    Bg = 2*math.pi*f/Cg

    re = (13184*math.sin(Ba)*math.sin(Bg) + math.cos(Ba) + math.cos(Bg)) / ((13184*13184*math.sin(Bg)*math.sin(Bg)) + math.cos(Bg)*math.cos(Bg))
    im = (math.sin(Ba)*math.cos(Bg) - 13184*math.cos(Ba)*math.sin(Bg)) / ((13184*13184*math.sin(Bg)*math.sin(Bg)) + math.cos(Bg)*math.cos(Bg))

    t = complex(re, im)
    return abs(t)

list = []
index = []

for i in range(20, 20001):
    list.append(func(i))
    index.append(i)

print(list)
print(index)

plt.loglog(index, list)
plt.ylabel('some numbers')
plt.show()