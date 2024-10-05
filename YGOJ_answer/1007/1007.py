import math
a=float(input())
if a<=10:
    b=2.5
else:
    b=2.5+math.ceil(a-10)*1.5
print(b)