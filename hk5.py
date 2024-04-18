list = input()
h=list
i =0
count = 0
count1=0
##don't forget the length in the while loop or for loop in that way only will configure 
while(i<len(h)):
    if(int(h[i]) % 2 == 0):
        count+=int(h[i])
    else:
        count1+=int(h[i])
    i+=1
print("sum of even numbers are" + str(count))