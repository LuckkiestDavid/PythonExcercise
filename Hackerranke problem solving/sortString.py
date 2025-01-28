# Your task is to sort the string S in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Input Format

# A single line of input contains the string S.

# Constraints
# 0 < len(S) < 100
# Output Format

# Output the sorted string S.

# Sample Input

# Sorting1234
# Sample Output

# ginortS1324

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    s = input()
    # Sort with a custom key:
    # 1. Lowercase letters (ord(c) -> 1st priority)
    # 2. Uppercase letters
    # 3. Odd digits
    # 4. Even digits
    sorted_s = sorted(s, key=lambda c: (c.isdigit() - c.islower(), c.isdigit() and int(c) % 2 == 0, c))
    # print("".join(sorted_s))
    print(sorted_s)
        