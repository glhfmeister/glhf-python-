import random as r

#1
print ("Task 1")
word  = str(input('Enter anything '))
emptyUp = 0
emptyLow = 0
for i in word:
	if (i.isupper() == True):
		emptyUp += 1
	else:
		emptyLow += 1
print ("Upper case letters = \n",emptyUp  / len(word) * 100)
print ("Lower case letters = \n",emptyLow / len(word) * 100)


#2
print ()
print ("Task 2")
word = str(input('Enter anything ->'))
sumW = 0
proizW = 1
for i in word:
	sumW += int(i)
	if (i != "0"):
		proizW *= float(i)
print ('Sum numbers = ',sumW,'The product of the numbers = ',proizW)

#3
print ()
print ("Task 3")
word = str(input('Enter anything '))
i = 1
boof = 0
arr = [len(word)]
arr = list(word)

word.split()

print (arr)
while (i < len(arr)):

	print (i)
	if (arr[i] == ' ') and (boof == 1):
		print ("o may")
		arr.pop(i)
		i -= 1

	if (arr[i] == ' ') and (boof == 0):
		arr[i] = '*'
		boof = 1

	if (arr[i] != ' ') and (arr[i] != '*'):
		boof = 0
	i += 1
word = "".join(arr); arr
print (word)

#4
print ()
print ("Task 4")
lenghtpas = 0
while (lenghtpas < 3):
	lenghtpas = str(input('Enter lenght of password '))
	lenghtpas = int (lenghtpas)

arr = []

low = "qwertyuiopasdfghjklzxcvbnm"
num = "0123456789"
spec = "~!@#$%^&*()_-+=/*<>?|'"

high = low.upper()
low = list (low)
num = list (num)
spec = list (spec)

rlow = r.randint (0,len(low)-1)
arr.append(high[rlow])
rnum = r.randint (0,len(num)-1)
arr.append(num[rnum])
rspec = r.randint (0,len(spec)-1)
arr.append(spec[rspec])

for i in range (0,lenghtpas-3):
	ran = r.randint (0,2)
	if (ran == 0):
		rlow = r.randint (0,len(low)-1)
		arr.append(low[rlow])
	if (ran == 1):
		rnum = r.randint (0,len(num)-1)
		arr.append(num[rnum])
	if (ran == 2):
		rspec = r.randint (0,len(spec)-1)
		arr.append(spec[rspec])

r.shuffle(arr)
arr = "".join(arr); arr
print (arr)