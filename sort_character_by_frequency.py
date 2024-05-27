
"""
x = len(c1)
print(x)
y = list(c1)
y.sort()
temp = int(x / 2)
print(temp)
new = y[temp:] + y[:temp]
print(new)


def mapping(c1):
    mp = {}
    # Count the frequency of each character
    for char in c1:
        mp[char] = mp.get(char, 0) + 1
    
    # Print the frequency dictionary
    print("Frequency dictionary:", mp)

    # Sort the dictionary by frequency in descending order
    sorted_mp = dict(sorted(mp.items(), key=lambda item: item[1], reverse=True))
    
    # Create a new list with characters repeated by their frequency
    sorted_list = []
    for key, count in sorted_mp.items():
        sorted_list.extend([key] * count)
    
    return sorted_list

# Take input and convert it to a list of characters
c1 = list(str(input("Enter a string: ")))
print("Original list:", c1)

# Get the sorted list by frequency and print it
sorted_by_frequency = mapping(c1)
print("Sorted by frequency:", sorted_by_frequency)

"""
text = "hello world i am hello world i i"
d = dict()
temp = list(set(text.split()))
temp.sort()
for i in temp:
    d[i] = text.count(i)
t1 = []
t2 = 0
l = list(d.keys())
count = len(d)
for i in range(len(l)):
    for j in range(i,len(l)):
        if d[l[i]] <= d[l[j]]:
            l[i],l[j] = l[j],l[i]
        if d[l[i]] == d[l[j]]:
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]

print(l)