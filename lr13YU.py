firstW = str (input('Enter first word '))
secondW = str (input('Enter second word '))

firstW = list (firstW)
secondW = list (secondW)

lenght = len(secondW)
boof = 0
i = 0
j = 0

while (i < len(firstW)):
	while (j < len(secondW)):
		if (firstW[i] == secondW[j]):
			boof += 1
			firstW.pop (i)
			secondW.pop(j)
			i -= 1
			j -= 1
		j += 1
	j = 0
	i += 1
	if (boof == secondW):
		break
if (boof >= lenght):
	print ("Yes you can")
else:
	print ("No you can't")