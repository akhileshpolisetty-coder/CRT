s='akhilesh'
print(s.capitalize())
print(s.title())
def reverse_string(n):
    return n[::-1]     # using slicing 
print(reverse_string(s))  
reverse='' 
for i in range(-1,-1*len(s)-1,-1):   
    reverse=reverse+s[i]
print(reverse) # manuval way to reverse a string 

# ---- Anagram Logic ----
# Two strings are anagrams if they have the same characters with same frequency
# Example: "listen" & "silent", "race" & "care"

# Method 1: Using sorted()
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False

# Method 2: Manual way using character frequency (without built-in)
def is_anagram_manual(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    return True

print(is_anagram_manual("race", "care"))    # True
print(is_anagram_manual("python", "java"))  # False
