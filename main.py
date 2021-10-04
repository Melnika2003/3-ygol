import math
x = []
for z in range(1,51):
    x.append(z)
def shiftArrMax(x):
    max_val = max(x)
    index_max_value = x.index(max_val)

    x[index_max_value] = 0
    return [max_val, x]
[a, x] = shiftArrMax(x)
[b, x] = shiftArrMax(x)
[c, x] = shiftArrMax(x)
p = (a + b + c) / 2
print("p = ", p)
if p - a > 0 and p - b > 0 and p - c > 0:
    s = (p * (p - a) * (p - b) * (p - c))**0.5
    print("s = ", s)
else:
    print('try again')