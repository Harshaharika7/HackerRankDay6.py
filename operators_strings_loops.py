# Read number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    s = input()
    even_chars = s[::2]  # Characters at even indices
    odd_chars = s[1::2]  # Characters at odd indices
    print(even_chars, odd_chars)
