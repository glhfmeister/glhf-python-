import math as m
#1
n = int (input())

l = []

l = [[1 if (x-y == 0) or (n-1-x-y == 0) else 0 for x in range (n)]for y in range (n)]

for y in range(n):
    for x in range(n):
        print(l[y][x], end = " ")
    print(" ")

print ()

#2
l1 = []
ch1 = 0
ch2 = n-1

for y in range (n):
         
        l1.append ([])
        
        for x in range (n):
                
                if x == ch1 or x == ch2:

                    l1[y].append (1)

                else:

                    l1[y].append (0)
        ch1 += 1
        ch2 -= 1
        
for y in range(n):
    for x in range(n):
        print(l1[y][x], end = " ")
    print(" ")

