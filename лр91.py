n = int (input('Введите "n" '))              #переменная в которую вводит пользователь любое число
n1 = 0                                       #переменная для того чтобы когда в while пишется несколько чисел это количество вычиталось можно сказать с конца

chislo = 1                                   #число для добавления в массив
sledchislo = 1                               #нужно для числа 

mainArray = []

for i in range (n):

    if chislo > 1:
            
        while chislo > 1:

            mainArray.append (chislo)

            chislo -= 1

    for index1 in range (n-n1):

        mainArray.append (chislo)
        chislo += 1

    n1 += 1

    for index2 in range (n):
    
        print (mainArray[0],end = ' ')
        mainArray.pop(0) 

    print ()
    chislo = sledchislo
    chislo += 1
    sledchislo += 1
