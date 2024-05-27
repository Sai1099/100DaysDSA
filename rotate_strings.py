c1 = list(str(input("Enter a string: ")))
c2 = list(str(input()))
print("Original list:", c1)

temp = 0
new = []

# Get all rotations of the list and append them to the new list
while temp < len(c1):
    # Rotate the list by one position
    rotated = c1[temp:] + c1[:temp]
    # Append the rotated list to the new list
    new.append(rotated)
    temp += 1

if c2 not in new:
    print('False')
else:
    print('True')





