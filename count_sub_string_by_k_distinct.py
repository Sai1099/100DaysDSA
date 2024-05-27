"""
ryy = list(input())
k=int(input())
count=0
for i in range(len(ryy)):
    z = ryy[i:i+k]
    count+=1
    print(z)
print(count)
"""

ryy = list(input())
k = int(input())
count = 0

def count_substrings_with_k_distinct(ryy, k):
    n = len(ryy)
    count = 0

    for i in range(n):
        distinct_chars = set()
        for j in range(i, n):
            distinct_chars.add(ryy[j])
            print(distinct_chars)
            if len(distinct_chars) == k:
                count += 1
            elif len(distinct_chars) > k:
                break
    return count

count = count_substrings_with_k_distinct(ryy, k)
print(count)
