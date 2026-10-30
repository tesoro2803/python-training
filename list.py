# 1.Print Array Elements:

a=int(input())
array=list(map(int,input().split()))
for i in array:
  print(i,end=" ")

#  2.Sum of Array Elements:

a=int(input())
array=list(map(int,input().split()))
print(sum(array))

# 3.Sum of Odd and Even Elements in an Array:

a=int(input())
array=list(map(int,input().split()))
odd=[y for y in array if y%2!=0]
even=[x for x in array if x%2==0]
print(sum(even),sum(odd))

#  4.Sum of Elements at Odd and Even Indices in an Array:

a=int(input())
array=list(map(int,input().split()))
odd=[y for y in array if array.index(y)%2!=0]
even=[x for x in array if array.index(x)%2==0]
print(sum(even),sum(odd))

#  5.Find Maximum Element in an Array:

a=int(input())
array=list(map(int,input().split()))
print(max(array))

#  6.Find Minimum Element in an Array:

a=int(input())
array=list(map(int,input().split()))
print(min(array))

#  7.Find Maximum Odd and Even Elements in an Array:

a=int(input())
array=list(map(int,input().split()))
odd=[y for y in array if y%2!=0]
even=[x for x in array if x%2==0]
if len(even)>0:
    print(max(even))
else:
    print("None")
if len(odd)>0:
    print(max(odd))
else:
    print("None")

#  8.Difference Between Sum of Odd and Even Elements in an Array:

a=int(input())
array=list(map(int,input().split()))
odd=[y for y in array if y%2!=0]
even=[x for x in array if x%2==0]
print(sum(odd)-sum(even))

#  9.Check if a Key Number Exists in an Array:

a=int(input())
array=list(map(int,input().split()))
find=int(input())
if find in array:
  print("Yes")
else:
  print("No")

#  10.Find Index of a Key Number in an Array:

a=int(input())
array=list(map(int,input().split()))
find=int(input())
if find in array:
  print(array.index(find))
else:
  print(-1)

 