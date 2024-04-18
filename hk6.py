num=int(input())

n1 =1
n2=1
sum = 0
for i in range(0,num):
   ## print(sum,end=" ")
    n1=n2
    n2=sum
    sum=n1+n2
print("the i value is " + str(sum))


