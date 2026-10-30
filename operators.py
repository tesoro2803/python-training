a= float(input("Enter the value 1:"))
choice=str(input("Enter the mathamatical operator (+,-,/,*,//,%,**):"))
b=float(input("Enter the value 2:"))

match choice:
    case "+":
        print("Result:",a+b)
    case "-":
        print("Result:",a-b)
    case "*":
        print("Result:",a*b)
    case "/":
        print("Result:",a/b)
    case "%":
        print("Result:",a%b)
    case "//":
        print("Result:",a//b)
    case "**":
        print("Result:",a**b)
    case  _:
        print("invaild opertaor")


# 1.Input and Output Practice
# Write a program that reads one value of each type from the user in the following order:
a=int(input())
b=float(input())
c=input()[0]
d=int(input())
e=float(input())
print(a)
print(b)
print(c)
print(d)
print(e)

# 2.Write a program that reads a floating-point number and prints successively rounded values, reducing the number of decimal places by one each step.

import struct
a=float(input())
a=struct.unpack('f',struct.pack('f',a))[0]
print(f"{a:.5f}")
print(f"{a:.4f}")
print(f"{a:.3f}")
print(f"{a:.2f}")
print(f"{a:.1f}")
print(f"{a:.0f}")

# 3.Given two integers A and B, print their sum, difference,product, quotient and remainder each on a new line.

a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
if a<0 or b<0:
  c=abs(a)%abs(b)
  print(-1*c)
else:
  print(a%b)

# 4.Write the program to execute conversion of other datatype.

a=int(input())
print(chr(a))

# 5.You are given an integer counter. Perform the following operations in order:

a=int(input())
print(((a+5)*2)-3)

# 6.Write a program that reads an integer and prints whether the number is Odd or Even using Ternary operator.

a=int(input())
sri= "Even" if a%2==0 else "Odd"
print(sri)
# 7.Write a program that reads an integer and print greatest among tree number using Ternary operator.

a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
  print(a)
elif b>c and b>a:
  print(b)
else:
  print(c)


# 8.Write a program that reads a single character representing a digit ('0' to '9') and prints its integer value.

a=input()
a=a[0]
print(a)

# 9.Write a program that asks the user to enter their name (a single word).
# Then, print a personalized greeting using that name in a sentence.

name=input()
print(f"Hi {name}, welcome to the programming class!")

# 10. John wants to learn how to calculate the total and average marks of a student in programming.
# Write a program that reads the student's name and marks in five subjects. Then calculate and print:

name=input()
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
total=m1+m2+m3+m4+m5
avg=float(total/5)
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {avg:.2f}")


# 11.Veena wants to learn how to calculate the area of different shapes (Square, Rectangle, Circle, Triangle) and implement it in programming.
# Write a program to calculate the area of each shape based on the given inputs

a=int(input())
l=int(input())
b=int(input())
r=int(input())
B=int(input())
h=int(input())
square=a*a
rect=l*b
circle=float((3.14)*r**2)
tirangle=((1/2)*B*h)
print("Area of %dSquare="%square)
print("Area of Rectangle=%d"%rect)
print("Area of Circle=%.2f"%circle)
print("Area of Triangle=%d"%tirangle)

# 12.Veena wants to learn how to calculate the perimeter of different shapes — Square, Rectangle, Circle, and Triangle — to implement them in programming.

a=int(input())
l=int(input())
w=int(input())
r=int(input())
s1=int(input())
s2=int(input())
base=int(input())
print(4*a)
print(2*(l+w))
print("%.2f"%(2*3.14*r))
print(s1+s2+base)

# 13.Priya is writing a program that needs to take two kinds of input from the user — first an integer, and then a sentence on the next line.
# However, after entering the integer, when she tries to type the sentence, the program immediately skips the input line and prints an empty output.
# Write a program that correctly reads both the integer and the sentence, and then prints them on separate lines.

a=int(input())
str1=input()
print(a)
print(str1)