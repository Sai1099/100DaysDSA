rt = str(input())
fds=[]
"""
for i in range(len(rt)-1,-1,-1):
   
   print(rt[i],end=" ")
"""
y = rt.split()
print(y)
##for rev
def reverseWords(self, s: str) -> str:
        ty = s.split()
        ty.reverse()
        return ' '.join(ty)
    