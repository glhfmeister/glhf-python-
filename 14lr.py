import random as r
flowers = ["ромашки","роза","лилии","алоэ","тюльпан","ванда","василёк","гладиолус","дельфиниум","драцена"]

before = r.randint (1,5)
mnoj = [{},{},{},{},{}]
check=False

for i in range(len(mnoj)):
    mnoj[i] =({r.choice(flowers)for j in range(3) })
    if (len(mnoj[i])!=3):
        
        while (check!=True):
            buf_2=(r.choice(flowers))
            for g in mnoj[i]:
                if g!=buf_2:
                        
                        check=True
        mnoj[i].add(buf_2)

print (mnoj)
al = 0
al = mnoj[0]
for i in range (1,5):
    al = al & mnoj[i]
print (al)
var = mnoj[0]
for i in mnoj:
    var|=i
b = set (flowers)

var=b-var
print("элементы которые не входят ",var)
al = mnoj[2] & mnoj[4]
print (al)
boof = mnoj[2] - al
print (boof)