f=open("abc.txt","r")
k=f.read()
l=k.split()
for i in l:
    if len(g)<len(i):
        g=i
print(g)
