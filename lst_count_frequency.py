j = list(map(int, input().split()))
count = float('inf')  # Set count to positive infinity initially
index = 0
temp = 0
for i in range(0, len(j)):
    temp = j.count(j[i])
    
    if temp < count:  # Check if the current count is less than the previous minimum count
        count = temp
        index = i

print("The least repeating number is " + str(j[index]))
print("The number of times it repeats is " + str(count))
