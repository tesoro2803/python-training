1.Write a program that reads one value of each type from the user in the following order:

a = int(input())
b = float(input())
c = input()
d = int(input())
e = float(input())
print(a)
print(b)
print(c)
print(d)
print(e)
  
2.Write a program that reads a floating-point number and prints successively rounded values, reducing the number of decimal places by one each step.

import struct
a = float(input())
a=struct.unpack("f",struct.pack('f',a))[0]
print(f"{a:.5f}")
print(f"{a:.4f}")
print(f"{a:.3f}")
print(f"{a:.2f}")
print(f"{a:.1f}")
print(f"{a:.0f}")
     
3.Given two integers A and B, print their sum, difference,product, quotient and remainder each on a new line.

#import math 
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
if a<0 or b<0:
  mod=abs(a)%abs(b)
  print(-1*mod)
else:
  print(a%b)

4.Write the program to execute conversion of other datatype.

n = int(input())
print(chr(n))

5.You are given an integer counter. Perform the following operations in order:

a=int(input())
b=((a+5)*2)-3
print(b)

6.Write a program that reads an integer and prints whether the number is Odd or Even using Ternary operator.

n = int(input())
print("Odd" if n % 2 != 0 else "Even")

7.Write a program that reads an integer and print greatest among tree number using Ternary operator

a=int(input())
b=int(input())
c=int(input())
print(max(a,b,c))

8.Write a program that reads a single character representing a digit ('0' to '9') and prints its integer value.

char = input()
print(int(char))

9.Write a program that asks the user to enter their name (a single word).
Then, print a personalized greeting using that name in a sentence

a=input()
print("Hi %s, welcome to the programming class!"%a)

10.Write a program that reads the student's name and marks in five subjects. Then calculate and print:

name=input()
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
sum1=sub1+sub2+sub3+sub4+sub5
avg=sum1/5
print("Student Name:",name)
print("Total Marks:",sum1)
print("Average Marks: %.2f"%avg)

11.Write a program to calculate the area of each shape based on the given inputs.

a=int(input())
l=int(input())
b=int(input())
r=int(input())
B=int(input())
h=int(input())
square=a*a
rect=l*b
cir=float(3.14*(r**2))
tri=(1/2)*B*h
print("Area of Square=%d"%square)
print("Area of Rectangle=%d"%rect)
print("Area of Circle=%.2f"%cir)
print("Area of Triangle=%d"%tri)

12.Write a program that reads the required dimensions and calculates the perimeter of each shape using the given formulas:

side=int(input())
l=int(input())
w=int(input())
r=int(input())
s1=int(input())
s2=int(input())
base=int(input())
print(4*side)
print(2*(l+w))
print("%.2f"%(2*3.14*r))
print(s1+base+s2)


13.Write a program that correctly reads both the integer and the sentence, and then prints them on separate lines.

a=int(input())
b=input()
print(a)
print(b)


       
       
         
     
  
 