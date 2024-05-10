arr = list(map(int,input().split()))
x=int(input())

def cal_is(arr,x,suma):
    sum=0
    board=1
    for paint in arr:
        if sum+paint<=suma:
            board +=1
            sum=paint
            if board>x:
                return False
        else:
            sum+=paint

    return True

def min_time_to_paint(arr,x):
    # The lower and upper bounds for the binary search
    lower_bound = max(arr)
    upper_bound = sum(arr)

    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if cal_is(arr,x,mid):
            upper_bound = mid
        else:
            lower_bound = mid + 1

    return lower_bound