a = input()
b = input()
c = input()
i = 0
flag = False
while i < len(a):
    if a[i:i+len(b)] == b:
        a = a[:i] + c + a[i + len(b):]
        flag = True
    i += 1
if not flag:
    print('0')
else: print(a)