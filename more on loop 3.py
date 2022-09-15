#n=int(input("enter your number:"))
count=0
for i in range(1,101):
    count+=1
    for i in range(i,101):
     if (n%i==0):
        print(i)
    
