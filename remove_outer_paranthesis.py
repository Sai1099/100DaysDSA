s = input()
def remobe_outer(s):
    open_par  = 0
    close_par = 0
    result = ""
    start = 0
    for i,c in enumerate(s):
        if(c=="("):
            open_par+=1
        elif(c==")"):
            close_par+=1
        if(open_par==close_par):
            result+=s[start + 1:i]
            start=i+1
    return result
print(remobe_outer(s))