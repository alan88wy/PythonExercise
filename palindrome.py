def is_palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s

if is_palindrome("racecar"):  # Output: True
    print("Yes")
else:
    print("No")
    
if is_palindrome("radar"):  # Output: True
    print("Yes")
else:
    print("No")