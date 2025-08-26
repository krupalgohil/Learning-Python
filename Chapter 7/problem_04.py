n=51
count = 0

for i in range(1,n):
    if n%i==0:
        count=count+1

if(count==1):
    print("number is prime")
else:
    print("number is not prime")