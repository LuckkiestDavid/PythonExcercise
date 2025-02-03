# Consider the following:

# A string, S, of length n  where S = C0,C1, ...Cn-1.
# An integer, k, where k is a factor of n.
# We can split S into n/k substrings where each subtring,ti, consists of a contiguous block of k characters in S. Then, use each ti to create string ui such that:

# The characters in ui are a subsequence of the characters in ti.
# Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once.
# In other words, if the character at some index j in ti occurs at a previous index < j in ti, then do not include the character in string ui.
# Given S and k, print n/k lines where each line i denotes string ui.

def merge_tools(string, k):
    for i in range(0, len(string), k):
        t = string[i : i + k]
        u = ""
        for char in t:
            if char not in u:
                u += char
                
        print(u)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_tools(string, k)