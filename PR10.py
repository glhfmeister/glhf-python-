import random as r

# Функция которая ищёт ID элемента по элементу
def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        guess = list[mid]
        if guess == item: 
            return mid  
        elif guess > item: 
            hight = mid -1 
        else: 
            low = mid + 1
    return None

    
a = []

for i in range(15): 
    a.append(r.randint(0, 15))

a.sort()
print(a)


finder  = int(input("Enter elem>> "))
quanity = 0

'''for i in range(15):'''
try:
    b = binary_search(a, finder)
    if finder == a[b]: 
        print(b)
        for i in range (0,15):
            if (a[b] == a[i]):
                quanity += 1
        print (quanity)
except TypeError:
        print("I can't find this")
