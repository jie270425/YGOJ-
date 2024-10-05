a,b,c=map(int,input().split())
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('yes')
    else:
        print('no')
else:
    print('not a triangle')