arr = list(map(int,input().split()))

def linearSearch(a, num):
    n = len(a)  # size of array
    for i in range(n):
        if a[i] == num:
            return True
    return False


def longestSuccessiveElements(a):
    n = len(a)  # size of array
    longest = 1
    # pick an element and search for its consecutive numbers
    for i in range(n):
        x = a[i]
        cnt = 1
        # search for consecutive numbers using linear search
        while linearSearch(a, x + 1):
            x += 1
            cnt += 1

        longest = max(longest, cnt)
    return longest
a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)