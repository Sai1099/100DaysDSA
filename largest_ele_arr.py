arr = list(map(int,input().split()))

def largest_element_in_arr(arr):
    y= sorted(arr)
    u=y[::-1]
    return max(u)

print(largest_element_in_arr(arr))