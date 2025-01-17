'''此版本由郭屹城同学提供'''

def isSymPeak(flag,steps):
    if flag==-1 and steps==0:
        return True
    else:
        return False
n=int(input())
a=list((map(int,input().split())))
 
flag=0;steps=0;count=0
for i in range(1,n):
    if a[i]>a[i-1]:
        if isSymPeak(flag,steps):
            count+=1
        if flag==0 or flag==-1:
            steps=1
        else:
            steps+=1
    elif a[i]==a[i-1]:
        if isSymPeak(flag,steps):
            count+=1
        steps=0;flag=0
    else:
        steps-=1
        flag=-1
if isSymPeak(flag,steps):
    count+=1
print(count)