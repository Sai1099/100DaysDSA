s=input()
def odd_num(s):
   for i in range(len(s)-1,-1,-1):
      if(int(s[i]) % 2 ):
         return s[:i+1]
   return ""

print(odd_num(s))