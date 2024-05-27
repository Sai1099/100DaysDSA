z=list(input())


def count_roman(z):
  
  count = 0
  mp={}
  for char in z:
       if char in mp:
          mp[char]+=1
          
       else:
          mp[char]  = 1
          
  return mp

print(count_roman(z))
mp = count_roman(z)

def merge(mp):
   sum=0
   v=mp.keys()
   temp=0
   rockz =[]
   for i,j in zip(mp,v):
    z = mp.get(i)
    stiu = {'I':1,
        'V':5,
        'X':10,
         'L':50,
          'C':100,
        'D': 500,
         'M':1000}
    p=stiu.get(j)
    
    bt=int(p)*z
    rockz.append(bt)
   return rockz
rockz = merge(mp)
def add(rockz):
   count = 0
   for i in rockz:
      count+=i
   return count
print(add(rockz))
   
    
      
     
      
      


#c='I'
#
#print(len(mp))