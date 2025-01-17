def d(a):
    i=0
    c=""
    list1=[]
    while i<(len(a)):
        if a[i]=="+" or a[i]=="-" :
            if len(c)!=0:
                list1.append(c)
                c=""
                if a[i]=="-":
                    c="-"
            else:
                c=c+a[i]
        else:
            c=c+a[i]
        i+=1
    list1.append(c)
    for i in range(len(list1)):
        if "X" in list1[i]:
            if "^" in list1[i]:
                for m in range(len(list1[i])):
                    if list1[i][m]=="X":
                        n1=m
                    if list1[i][m]=="^":
                        n2=m
                if list1[i][0]!="X":
                    s1=int(list1[i][:n1])
                else:
                    s1=1
                s3=int(list1[i][-1])-1
                s2=s1*(s3+1)
                if s3==1:
                    list1[i]=str(s2)+"X"
                else:
                    list1[i]=str(s2)+"X^"+str(s3)
            else:
                list1[i]=list1[i][:-1]
        else:
            list1[i]="0"
    mn=""
    for i in list1:
        if i==list1[0]:
            if i!="0":
                mn=i
        else:
            if i!="0":
                if len(mn)==0:
                    mn=i
                else:
                    mn=mn+"+"+i
    if len(mn)==0:
        mn="0"
    return mn
a = "-3X^-2+5X^3-10+X^4"
print(d(a))