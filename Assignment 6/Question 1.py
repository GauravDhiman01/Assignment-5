x=int(input("Enter the number to check wheather it is perfect or not:"))
sum=0
for i in range(1,x+1):
    if x%i==0:
        print(i,"is a divisor of",x)
        sum+=i
if x/sum==0.5:
    print(x,"is a Prefect number.")
else:
    print(x,"is not a Prefect number.")