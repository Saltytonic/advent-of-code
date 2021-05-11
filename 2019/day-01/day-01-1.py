import math
f = open("input.txt", "r")
o = 0
for line in f:
    o = o + (math.floor(int(line)/3)-2)

print(o)
