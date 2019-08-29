n=int(input("enter no of inputs"))
arr=input().split()
res=list(map(int,input().split()))
print(max([res.count(i) for i in res]))






















