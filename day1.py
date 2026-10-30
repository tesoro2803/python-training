# 1
print("Hello World")

# 2
name="Deepan Sri"
print("Name:",name)



# 3
name=input("Enter your name:")
city=input("Enter your city:")
age=int(input("Enter the age:"))
print("Name:", name, "City:", city, "Age:", age)

# 4
a,b=map(int,input("Enter the two numbers:").split())
print(a,b,sep="-")


# 5
a=10
b=20
print(a,b,sep=" ")
a,b=b,a
print(a,b,sep=" ")

part 2

# 1
integr=int(input("Enter the integer:"))
float_num=float(input("Enter the float number:"))
bollean1=bool(input("Enter the boolean value:"))
string1=str(input("Enter the string:"))
print("Integer:",integr)
print("Float:",float_num)
print("Boolean:",bollean1)
print("String:",string1)

# 2
age=int(input("Enter the age:")
print(type(age))

# 3
num1,num2=map(int,input("Enter the two numbers:").split())
print("sum:",num1+num2)

# 4
num1=int(input("Enter the num1:"))
print(float(num1))   

# 5
num1=input("Enter the number:")
print(int(num1)+5)

# part c

#1
num1,num2=map(int,input("Enter the two numbers:").split())
print("sum:",num1+num2)
print("diffrence:",num1-num2)
print("product:",num1*num2)
print("qoutient:",num1/num2)

# 2
num1,num2=map(int,input("Enter the two numbers:").split())
print("Floor division:",num1//num2)

# 3
num1,num2=map(int,input("Enter the two numbers:").split())
print("Modulus:",num1%num2)

# 4
num1=int(input("Enter the number:"))
print("last digit:",num1%10)

# 5
num1=int(input("Enter the number:"))
fristdigit=num1//10
lastdigit=num1%10
sumdigit=fristdigit+lastdigit
print(sumdigit)

# 6
num1=int(input("Enter the number:"))
print("Square:",num1**2,"Cube:",num1**3,sep=" ")

# 7
lenth=float(input("Enter the lenth:"))
breadth=float(input("Enter the breadth:"))
print("Area:",lenth*breadth,"Perimeter:",2*(lenth+breadth),sep="\n")
