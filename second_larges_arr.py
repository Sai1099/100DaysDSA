arr = list(map(int,input().split()))
def second_lar_arr(arr):
    st = sorted(arr)
    f= st[::-1]
    h = f[1]
    k= f[len(arr)-2]
    return h ,k
print(second_lar_arr(arr))