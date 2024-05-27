"""
bro = list(input())
def check_max(bro):
    count=0
    temp=0
    res=[]
    for i in range(len(bro)):
       if(bro[i]=="(" or ")"):
            res.append(bro[:i])   
    return res  
    for i in bro:
        ##print(i)
        
        if(i == '('):
             count=count+1
             
        elif(i == ')'):
             temp=temp+1
            
    if(temp == count):
           return temp
    else:
         if(temp<count):
              return temp
         else:
              return count
print(check_max(bro))
"""

bro = list(input())

def check_max(bro):
    max_depth = 0
    current_depth = 0
    for char in bro:
        if char == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ')':
            current_depth -= 1
    return max_depth

print(check_max(bro))
