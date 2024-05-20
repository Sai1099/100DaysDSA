sta = list(map(str,input().split()))
y=sta[::-1]
for item in range(0,len(sta)):
    print(y[item])


"""
def reverse_words_in_string(s: str) -> str:
    # Step 1: Split the string into words
    words = s.split()
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
    # Step 3: Join the reversed list of words into a single string
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Example usage
input_string = "Hello world this is an example"
output_string = reverse_words_in_string(input_string)
print(output_string)  # Output: "example an is this world Hello"
"""