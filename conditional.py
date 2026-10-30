# 1.Take an integer as input and return "POSITIVE" if the integer is positive, "NEGATIVE" if the integer is negative and "ZERO" if the integer is zero.

a=int(input())
if a>0:
  print("POSITIVE")
elif(a<0):
  print("NEGATIVE")
else:
  print("ZERO")

# 2.Kumar wants to know how the math functions are working in programming. Could you please help him write a program to understand the behavior of some mathematical functions like floor, ceil, round, sqrt, and power.

import math as m
a=float(input())
b=int(input())
c=int(input())
d=int(input())
print(m.floor(a))
print(m.ceil(a))
print(round(a))
print(int(m.sqrt(b)))
print(int(m.pow(c,d)))      

# 3.Write a program to read four integers and determine the minimum (smallest) number among them.

a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(min(a,b,c,d))

# 4.Write a program that takes a floating-point number as input and prints the value truncated (cut off) to two decimal places without rounding.

import math as m
a=float(input())
a=m.trunc(a*100)/100
print("%.2f"%a)

# 5.Write a program that reads three integers and finds the second largest number among them using if-else statements.
# If all three numbers are equal, print: No second max.

a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
  if b>c:
    print(b)
  else:
    print(c)
elif b>a and b>c:
  if a>c:
    print(a)
  else:
    print(c)
elif c>a and c>b:
  if a>b:
    print(a)
  else:
    print(b)
else:
  if a==b==c:
    print("No second max")
 
# 6.Take three integers A, B, C which denote the angles of a triangle

a=int(input())
b=int(input())
c=int(input())
if a+b+c==180 and a>0 and b>0 and c>0:
  if((a+b)>c and  (b+c)>a and (c+a)>b):
    print('VALID')
    if(a==b==c):
      print("EQUILATERAL")
    elif(a==b or b==c or a==c):
      print("ISOSCELES")
    else:
      print("SCALENE")
  else:
    print('NOT VALID')
else:
  print("NOT VALID")

# 7.Write a program that reads a single-digit number (0–9) as input and prints its word representation

a=int(input())

match a:
  case 0:
    print("zero")
  case 1:
    print("one")
  case 2:
    print("two")
  case 3:
    print("three")
  case 4:
    print("four")
  case 5:
    print("five")
  case 6:
    print("six")
  case 7:
    print("seven")
  case 8:
    print("eight")
  case 9:
    print("nine")
    
# 8.Write a program that reads a single character as input and prints whether it is a vowel or a consonant.

a=input()
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U':
  print("vowel")
else:
  print("consonant")
# 9.Write a program that reads a year as input and prints whether it is a leap year or not.
a=int(input())
if a>0:
  if a%4==0 and a%400==0 or a%100:
    print("yes")
  else:
    print("no")

# 10.Fun Grade Calculator

m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
total=m1+m2+m3+m4+m5
a=int(total/5)
if a>=90:
  print("Excellent!")
elif a>=80 and a<90:
  print("Great Job!")
elif a>=70 and a<80:
  print("Good Effort!")
elif a>=50 and a<70:
  print("Keep Trying!")
else:
  print("Better Luck Next Time!")

# 11.Write a program to determine the berth type based on the seat number.
# In a train coach, each seat number corresponds to a specific berth type. For a given seat number, your task is to determine which berth type it is. The seat allocation in most Indian Sleeper (SL) and 3AC coaches follows a repeated pattern of 8 seats

a=int(input())
b=a%8
if b==1:
  print("LB")
elif b==2:
  print("MB")
elif b==3:
  print("UB")
elif b==4:
  print("LB")
elif b==5:
  print("MB")
elif b==6:
  print("UB")
elif b==7:
  print("SL")
else:
  print("SU")
  
# 12.Write a program to calculate the electricity bill based on the number of units consumed.

import math as m
units = float(input())

if units <= 50:
    bill = units * 1
elif units <= 150:
    bill = 50 * 1 + (units - 50) * 2
elif units <= 250:
    bill = 50 * 1 + 100 * 2 + (units - 150) * 3
else:
    bill = 50 * 1 + 100 * 2 + 100 * 3 + (units - 250) * 4

if bill > 150:
    bill = bill + bill * 0.20

print(m.trunc(bill))

  print(a)

# 13.Write a program that takes a number as input and prints a famous Tamil cinema reference based on divisibility:
# If the number is divisible by 3 only, print "Thala"
# If the number is divisible by 5 only, print "Thalapathy"
# If the number is divisible by both 3 and 5, print "ThalaThalapathy"
# If the number is divisible by neither 3 nor 5, print the number itself

a=int(input())
if a%3==0 and a%5==0:
  print("ThalaThalapathy")
elif a%5==0:
  print("Thalapathy")
elif a%3==0:
  print("Thala")
else:
  print(a)

# 14.Write a program to calculate the train fare based on the passenger’s age and distance to travel. The fare rules are
# Children (age < 12): 50% of standard fare per km
# Adults (12 ≤ age ≤ 59): 100% of standard fare per km
# Seniors (age ≥ 60): 75% of standard fare per km
# Standard fare per km: Rs 5

age=int(input())
dis=int(input())
if age<12:
  far=dis*5
  far=far*0.5
elif age>=12 and age<=59:
  far=dis*5
else:
  far=dis*5
  far=far*0.75
print(int(far))

# 15.Write a program that reads marks in five subjects and calculates the average.
# If the average is a whole number, print it as an integer.
# If the average is not a whole number, print it with exactly two digits after the decimal point.

m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
total=m1+m2+m3+m4+m5
avg=total/5
if avg %1==0:
  print(int(avg))
else:
  print("%.2f"%avg)

# 16.Write a program that takes a single character as input and performs the following:
# If the character is a lowercase letter, convert it to uppercase.
# If the character is an uppercase letter, convert it to lowercase.
# If the character is not an alphabet, print a funny Tamil-style sentence like "abcd theriyatha?"

char=input()
char=char[0]
if ord(char)>=97 and ord(char)<=122:
  result=chr(ord(char)-32)
elif ord(char)>=65 and ord(char)<=90:
  result=chr(ord(char)+32)
else:
  result="abcd theriyatha?"

print(result)