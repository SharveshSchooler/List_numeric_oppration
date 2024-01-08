def odd(a,b):
    l=[]
    for v in range(a,b):
        if v%2!=0:
            l.append(v)
    return l
def prime(z):
    q=[]
    for i in (z):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            q.append(i)
    return q
def arm(h):
    k=[]
    for n in (h):
        j=n
        s=str(n)
        l=len(s)
        c=0
        while n>0:
            x=n%10
            g=x**l
            c=c+g
            n=n//10
            if j==c:
                k.append(j)
    return k

a=int(input("Starting range"))
b=int(input("Ending range"))
r=odd(a,b)
print(r)
z=r
p=prime(z)
print(p)
h=p
d=arm(h)
print(d)