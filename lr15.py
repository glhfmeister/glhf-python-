dictWorkers={
    "таб ном"      :[],
    "фамилия"      :[],
    "пол"          :[],
    "зарплата"     :[],
    "дата рождения":[]
    }
number=[6,100,15,456,123,789,159,124,576,10]
secondName=["Гушшамов","Никиткин","Круг","Егошин","Мальчиков","Джостар","Мальчиков","Подзаборкин","Смоукин","Изукин"]
hender=["мафиозник","средний","круглый","паркет","томатный","самый-мужской","самоопыляющийся","бревно","беглый","нормальный"]
price=[120,10000,15000,200000,6,16700000,20000,12000,6000,215000]
born=[2,6,90,23,56,12,342,43,23,67]
secondName.sort()
print ("таб ном =",number)
print ("фамилия =",secondName)
print ("пол =",hender)
print ("зарплата =",price)
print ("дата рождения =",born)
halfborn=0
for i in range (10):
    halfborn += born[i]
    if (secondName[i-1] == secondName[i] and i != 9 and born[i-1] < born[i]):
        boof = hender[i]
        hender[i]=hender[i-1]
        hender[i-1]=boof

        boof = price[i]
        price[i]=price[i-1]
        price[i-1]=boof

        boof = born[i]
        born[i]=born[i-1]
        born[i-1]=boof

        boof = number[i]
        number[i]=number[i-1]
        number[i-1]=boof
dictWorkers.get("таб ном").append(number)
dictWorkers.get("фамилия").append(secondName)
dictWorkers.get("пол").append(hender)
dictWorkers.get("зарплата").append(price)
dictWorkers.get("дата рождения").append(born)
for i in dictWorkers.keys():
    print (i,"=",dictWorkers[i])
