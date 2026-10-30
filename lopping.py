# 1.Print the first 100 natural numbers

for i in range(1,100+1):
  print(i,end="\n")

# 2.Take two integers a,b and print all the even numbers in between them, excluding the input integers.

a=int(input())
b=int(input())
a=min(a,b)+1
b=max(a,b)
for i in range(a,b):
  if i%2==0:
    print(i,end="\n")
  
# 3.Take two integers a,b and return the count of all the odd numbers in between them, inclusive of the input

a=int(input())
b=int(input())
a=min(a,b)
b=max(a,b)+1
count=0
for i in range(a,b):
  if i%2!=0:
    count+=1
print(count)
  
# 4.Print the sum of all even numbers from 1 to 100.

sum1=0
for i in range(1,100+1):
  if i%2==0:
    sum1=sum1+i
print(sum1)

# 5.Take an integer and print the multiplication table of the interger upto a factor of 10 in this form -> n x 1 = n

a=int(input())
for i in range(1,11):
  print(f"{a} x {i} = {i*a}")
# 6.Take an integer and return the factorial.
a=int(input())
fact=1
for i in range(1,a+1):
  fact=fact*i
print(fact)

# 7.Take an integer and print "YES" if the integer is prime and "NO" if it is not.

n = int(input())

if n < 2:
    print("NO")
else:
    for i in range(2, n):
        if n % i == 0:
            print("NO")
            break
    else:
        print("YES")

# 8.Take 10 integers as input and print their product.

a1=int(input())
a2=int(input())
a3=int(input())
a4=int(input())
a5=int(input())
a6=int(input())
a7=int(input())
a8=int(input())
a9=int(input())
a10=int(input())
while True:
  print(a1*a2*a3*a4*a5*a6*a7*a8*a9*a10)
  break

# 9.Print all numbers from 1 to 100 in their reverse order

for i in range(100,0,-1):
  print(i)

  # 10.Print the pattern given below, using loops.

for i in range(4):
  for i in range(5):
   print("*",end="")
  print()

# 11.Print the pattern given below, using loops

for i in range(5):
  for j in range(i+1):
    print("*",end="")
  print()

# 12.Print the pattern given below, using loops.

for i in range(1,6):
  for j in range(1,i+1):
    print(j,end="")
  print()

# 13.Print the pattern given below, using loops.

for i in range(1,6):
  for j in range(i):
   print(i,end="")
  print()

# 14.Print the pattern given below, using loops.

num = 1
for i in range(1,6):
  for j in range(i):
    print(num,end=" ")
    num+=1
  print()

#   15

num = 1
for i in range(1,6):
  for j in range(i):
    print(num,end=" ")
    num+=1
  print()