t = input()
##count_frequency
s = list(map(int,input().split()))
print(s)
n= len(s)
print(n)
def funt(s,n):
    visited = [False] * n
    t=[]
    for i in range(n):
        
        if(visited[i]==True):
         continue
        count=1
        for j in range(i+1,n):
            if(s[i]==s[j]):
               visited[j]=True
               count+=1
        t.append(count)
        print(s[i],count)
    print(t)

print(funt(s,n))


##Hashing -------REVISION
def hashmap(s,n):
   mp={}
   for i in range(n):
      if s[i] in mp:
         mp[s[i]] +=1
      else:
         mp[s[i]]=1

   for x in mp:
      print(mp[x],x)

##print(hashmap(s,n))