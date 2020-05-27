import random as r
import math as m
size = int (input('Enter size array -> '))
arr=[]
b = 2
c = 0
i = 0
d = 2
e = 0

while (i < size):
  while (c < d):
    if (e < size):
      i += 1
      c += 1
      e += 1
      arr.append(b)
      print (b)
    else:
      c = d
      i = size
  d += 1
  b += 4
  c = 0
print (arr)

number = int(input('Enter any number, but I would like it to be in the list -> '))
boof = 0
low = 0
high = size-1
while low <= high:
    mid = (low + high) // 2
    if number < arr[mid]:
        high = mid - 1
    elif number > arr[mid]:
        low = mid + 1
    else:
        boof = arr[mid]
        break
quanity = 0
if (boof != 0):
    for i in range (size):
        if (boof == arr[i]):
            quanity += 1
        if (boof == arr[i] and boof != arr[i-1]):
            print ('First appearance this number -> ',i)
    print ('Quanity this number -> ',quanity)
else:
    print ('There is no such number')
