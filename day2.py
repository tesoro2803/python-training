import math as m
# #1
product1=float(input("Enter the price:"))
product2=float(input("Enter the price:"))
print("********************************")
print("Total Price:",product1+product2)
print("********************************")
print("Higher price:",max(product1,product2))
print("Lower price:",min(product1,product2))

#2
m1,m2,m3,m4,m5=map(int,input("Enter the marks:").split())
total=int (m1+m2+m3+m4+m5)
print("Toatl marks:",total)
percentage=total/5
print(f"percenatage:{percentage:.2f}")

#3

length=float(input("Enter the lenght:"))
width=float(input("Enter the width:"))
area=length*width
peremeter=2*(length+width)
print(f"Area of Floor:{area:.2f}\nPermeter of the floor:{peremeter:.2f}")


#4


distance=float(input("Enter the distance:"))
print(f"Distance:{m.trunc(distance)}km")  


5
 
a=int(input())
b=int(input())
print("Box required for this product:",m.ceil(a/b))


# 6

area=float(input("Enter the are of square:"))
print("Lenght of the square:",m.sqrt(area))

# 7
a=int(input())
b=int(input())
print("matching bit are:",a & b)

# #8
a=int(input())
print((a//2)*2==a)

#9

a=int(input())
b=int(input())
print(divmod(a,b))

#10
x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())
print(m.sqrt((x2-x1)**2+(y2-y1)**2))



