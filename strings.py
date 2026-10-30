# 1.Length of a string

str1=input()
print(len(str1))

# 2.Join the strings

str1=input()
str2=input()
print(str1+" "+str2)

# 3.Compare the Strings

str1=input()
str2=input()
if str1==str2:
  print("true")
else:
  print("false")

# 4.First character of a string

str1=input()
print(str1[0])

# 5.Last character of a string

str1=input()
l=len(str1)
print(str1[l-1])

# 6.Join first & last characters of a string

str1=input()
l=len(str1)
print(str1[0]+str1[l-1])

# 7.Take a string from the input and check whether or not it contains both letters and numerals

str1=input()
if any(i.isdigit() for i in  str1) and any(j.isalpha() for j in str1):
  print("true")
else:
  print("false")

# 8. ake a string from the input and check all the letters in the string are of upper case

str1=input()
if str1.isupper():
  print("true")
else:
  print("false")

# 9.Take a string from the input and check all the letters in the string are of lower case

str1=input()
if str1.islower():
  print("true")
else:
  print("false")

# 10.ake two strings from the input and check the lengths of those strings equal or no

s1=input()
s2=input()
if len(s1)==len(s2):
  print("true")
else:
  print("false")

# 11.Take a string from the input and print it in reverse

s1=input()
print(s1[::-1])

# 12.Take a string from the input and split the strings with comma. Print the new strings one per line

s1=input()
for i in s1.split(","):
  print(i)

# 13.Take a string from the input and remove the vowels and print it

s1=input()
for i in s1:
  if i in "aeiouAEIOU0":
    s1=s1.replace(i,"")
print(s1)

# 14.Take a string from the input and change lowercase characters to uppercase and uppercase characters to lowercase

s1=input()
print(s1.swapcase())

# 15.Take a string from the input and print ascii character

s1=input()
print(ord(s1))

# 16.Take a string from the input and remove all occurrences of given char from that string

s1=input()
s2=input()
print(s1.replace(s2,""))

# 17.Search a word existence inside a given string

s1=input()
s2=input()
if s2 in s1:
  print("true")
else:
  print("false")

# 18.Count the total vowels and consonants in a given string and print them

s1=input()
r=r1=0
for i in s1:
  if i in "aeiouAEIOU":
    r+=1
  else:
    r1+=1
print(r)
print(r1)

# 19.Check the given 2 strings are anagrams.
# Hint: anagram means the strings contains same characters but order of characters is not important
# Note: Ignore considering the case or spaces.

s1=input().lower().replace(" ","")
s2=input().lower().replace(" ","")
if sorted(s1)==sorted(s2):
  print("true")
else:
  print("false")

# 20.Check whether or not the given string is a palindrome

s1=input()
if s1==s1[::-1]:
  print("true")
else:
  print("false")

