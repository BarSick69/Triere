def check(num,m):
    sum=0
    if(num==0 and m==0):
        return True
    while(num!=0):
        sum+=num%10
        num//=10
    if(sum==m):
        return True
    else:
        return False

n=int(input("Dati n: "))
m=int(input("Dati m: "))
k=0
for i in range(0,n+1):
    if(check(i,m)):
        k+=1
print(k)
