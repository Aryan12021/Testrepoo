#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     24-10-2022
# Copyright:   (c) HP 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------



nums = [11,3,4,44,67]
print(nums)
print(nums[4])
print(nums[2:])

nums.append(87)
print(nums)

print(nums)
print(nums)
nums.insert(1,99)
print(nums)

nums.pop(5)
print(nums)


nums.extend([1,5,67,89,54,22])
print(nums)

print(min(nums))
print(max(nums))
nums = [12,34,78,95,89]
nums.append(764745646)
print(nums)
sum(nums)


tup = (23,6,91,34)

print(tup[1])

s = {22,36,58,41}
print(s)

s.add(2)
print(s)

data = {1:'sanju',2:'sinjo',3:'sanjo'}
print(data[2])
print(data.get(3))

keys = ["sinju","sanjo","sanju"]
values =["java","python","js"]
data = dict(zip(keys,values))
print(data)

data['sinji'] = 'CS'
print(data)
del data['sanju']
print(data)

num = 5
print(id(num))

a = 45
b = a
print(id(a))
print(id(b))
print(id(45))

a = 55
print(id(a))
print(id(b))

print(type(a))
print(type(num))

num = 25
print(type(num))

num = 6+9j
print(type(num))

num = 2.8
print(type(num))

a = 4.7
b = int(a)
print(type(b))
print(b)

k = float(b)
print(b)

c = complex(b,a)
print(c)

x = 8
y = 2
print(x>y)

print(int(True))
print(int(False))

lst = [65,8,48,97,12]
print(type(lst))

s = {5,6515,45458,84,83}
print(type(s))

t = (65,32,97,54)
print(type(t))

st = "king"
print(type(st))

range(0,20)
print(list(range(20)))

range(2,20,2)
print(list(range(2,20,2)))

x = 5
y = 9

print(x/y)

x = x+2
print(x)

x += 2
print(x)

x *= 2
print(x)

a = 6
b = 8

print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)

print(a < 7 and b < 9)

print(a < 5 and b < 9)

print(a < 8 or b<7)

print(a<4 or b<7)

z = True
print(not z)

print(bin(25))
