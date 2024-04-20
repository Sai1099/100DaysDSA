n = int(input())
def recur(n):
    if(n>0):
        print("Hello bro", end=" ")
        return recur(n-1)
print(recur(n))