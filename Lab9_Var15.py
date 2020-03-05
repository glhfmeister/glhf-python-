n = int(input("n: ")) #Кол-во элементов
elements = []

for i in range(n):
	a = int(input("a: ")) #Сами элементы
	elements.append(a)

print(elements, "\n")

#Генератор списков
l = [[elements[j + i - n] for j in range(n)] for i in range(n)]

for i in range(n):
	for j in range(n):
		print(l[i][j], end = " ")
	print()

print()
#Двумерные списки
l = []
for i in range(n):
	l.append([])

	for j in range(n):
		l[i].append(elements[j + i - n])

		print(l[i][j], end = " ")
	print()