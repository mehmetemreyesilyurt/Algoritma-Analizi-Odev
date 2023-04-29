b,c,d,e,f,g,h,i,j,k,l,m,n=0,0,0,0,0,0,0,0,0,0,0,0,0
def func(first,last):
    if(first==0):
        return last
    elif(last<first):
        return last
    else:
        return first

def distance(x):
    print("{}m".format(x)) 

totaldistance=0
route=[]
route.append("A")
#[A-I] arası mesafe bulunur.
#A
b=func(b,400)
route.append("B")
#B
c=func(c,b+600)
g=func(g,b+550)
#C
d=func(d,c+350)
j=func(j,c+450)
l=func(l,c+200)
#G
h=func(h,g+50)
i=func(i,g+370)
#H
i=func(i,h+350)
#J
i=func(i,j+410)
if(g==950):
    route.append("G")

print("A-I arası en kısa mesafe:")
route.append("I")
distance(i)
totaldistance+=i
#[I-J] arası en kısa mesafe 410 metredir.
route.append("J")
totaldistance+=410
#[J-L] arası mesafe bulunur.
b,c,d,e,f,g,h,i,j,k,l,m,n=0,0,0,0,0,0,0,0,0,0,0,0,0
#D
e=func(e,d+200)
#J
c=func(c,450)
n=func(n,380)
#C
d=func(d,c+350)
l=func(l,c+200)
#N
k=func(k,n+180)
#K
e=func(e,k+210)
#L
m=func(m,l+500)
#M
e=func(e,m+120)
#E
m=func(m,e+120)
if(c==450):
    route.append("C")
if(l==650):
    route.append("L")
print("J-L arası en kısa mesafe:")
distance(l)
totaldistance+=l
#En son [L-F] arası mesafe bulunur.
b,c,d,e,f,g,h,i,j,k,l,m,n=0,0,0,0,0,0,0,0,0,0,0,0,0
#L
m=func(m,500)
route.append("M")
#M
e=func(e,m+120)
route.append("E")
#E
f=func(f,e+150)
route.append("F")
print("L-F arası en kısa mesafe:")
distance(f)
totaldistance+=f
print("Toplam mesafe = {}m".format(totaldistance))
print("Rota: ",end='')
f=False
for i in route:
    if(f==False):
        print("{}".format(i),end='')
        f=True
    else:
        print("-{}".format(i),end='') 