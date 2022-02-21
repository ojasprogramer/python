# This program tells that is the str palindrom or not.

def isPalindrome(s):
	return s == s[::-1]

s=input("Enter a word-")
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
