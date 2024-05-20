s=list(map(str,input().split()))
def longest_common(s):
    print(s)
    for i in range(0,len(s)):
        print(s[i])
        for j in range(i,len(s[i])):
            for k in range(j+1,len(s[i+1])):
                if(s[i][j]==s[i][k]):
                    return s[i][k]
                else:
                    return s[i][j]
                    continue
    
def commmon_prefix(s):
    start_prefix=s[0]
    new_prefix  =""
    for i in s:
        current_prefix = s[i]
        for j in range(min(len(current_prefix),len(start_prefix))):
            if(start_prefix[j] == current_prefix[j]):
                new_prefix +=start_prefix[j]
               
            else:
                break
        start_prefix=new_prefix
        if not  start_prefix:
            break
    return start_prefix



print(longest_common(s))