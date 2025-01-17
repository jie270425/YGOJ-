'''m,n = input().split()
def tentoq(ten,q):
    ret=''
    while ten>0:
        r=ten%q
        if r<10:
            ret=chr(48+r)+ret
        else:
            ret=chr(55+r)+ret
        ten//=q
    return ret
jinzhi = []
for i in range(1,9):
    m1,n1 = m,n
    a = tentoq(n1,i)
    '''
def change(n,b):
    x=""
    while n>0:
        c=n%b
        x=str(c)+x
        n=n//b
    return x
def pd(a,b):
    c,d=a[0],b[0]
    i,j=0,0
    if c!=d:
        return False
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            i+=1
        j+=1
    if i==len(a):
        return True
    return False
m,n=map(int,input().split())
flag=True
for i in range(2,9):
    m1,n1=change(m,i),change(n,i)
    list1=[0]*i
    list2=[0]*i
    for k in m1:
        list1[int(k)]+=1
    for k in n1:
        list2[int(k)]+=1
    if pd(m1,n1) and m1!=n1:
        print(i,end=" ")
        for j in range(i):
            list2[j]-=list1[j]
        for k in range(len(list2)):
            if list2[k]!=0:
                for l in range(list2[k]):
                    print(str(k),end="")
        print()
        flag=False
if flag:
    print("404 not found")