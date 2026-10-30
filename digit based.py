# 1.Write a program to count the number of digits in a given integer.

a=int(input())
count=0
if a==0:
  count=1
while a!=0:
  count=count+1
  a=a//10
print(count)

# 2.Write a program to find the sum of all even digits in a given number.

a=int(input())
count=0
if a==0:
  count=1
while a!=0:
  count=count+1
  a=a//10
print(count)

# 3.Write a program to find the product of all digits of a given integer.

n=int(input())
sum1=1
while n!=0:
  r=n%10
  sum1=sum1*r 
  n=n//10
print(sum1)

# 4.Write a program to reverse a given integer.

n=int(input())
h=0
while n!=0:
  r=n%10
  h=h*10+r
  n=n//10
print(h)
  
# 5.Write a program to check whether a given number is a palindrome or not

n=int(input())
j=n
h=0
while n!=0:
  r=n%10
  h=h*10+r
  n=n//10
if j==h:
  print("Palindrome")
else:
  print("Not Palindrome")

# 6.Write a program to find the first digit of a given number.

n=int(input())
while n>=10:
  n=n//10
print(n)

# 7.Write a program to count how many zeros (0s) are present in a given number.

n=int(input())
sum1=0
if n==0:
  sum1=1
else:
  sum1=0
while n!=0:
  t=n%10
  if t==0:
    sum1=sum1+1
  n=n//10
print(sum1)

# 8.Write a program to check whether a given number is an Armstrong number or not

a=int(input())
n=comp=a
add=0
count=0
while n!=0:
  count+=1
  n=n//10
while a!=0:
  digit=a%10
  add=add+(digit**count)
  a=a//10
if comp==add:
  print("Armstrong")
else:
  print("Not Armstrong")

# 9.Write a program to check whether a number is a Strong number.

a=int(input())
comp=a
add=0
while a!=0:
  digit=a%10
  fact=1
  for i in range(1,digit+1):
    fact=fact*i
  add=add+fact
  a=a//10
if add==comp:
  print("Strong")
else:
  print("Not Strong")

# 10.Write a program to check whether a given number is a Perfect number or not.

a=int(input())
add=0
for i in range(1,a):
  if a%i==0:
    add=add+i
if a==add:
  print("Perfect")
else:
  print("Not Perfect")