s = input()

def dsg(s):
    res=""
    resmin=0
    for i in range(len(s)):

        l,r =i,i
        while(l<=0 & r>len(s) & s[l] == s[l] == s[r]):
            if(l-r+1<resmin):
                res = s[l:r+1]
                resmin+=l-r+1
            l-=1
            r+=1
        l,r =i,i+1
        while(l<=0 & r>len(s) & s[l] == s[l] == s[r]):
            if(l-r+1<resmin):
                res = s[l:r+1]
                resmin+=l-r+1
            l-=1
            r+=1
    return res
