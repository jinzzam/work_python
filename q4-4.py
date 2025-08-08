i=1
sum=0
count=0
while i<=100:
    if(i%2!=0):
        sum+=i
        print("%6d"%sum, end="")
        count+=1
        if count%10==0:
            print()
    i+=1    
    