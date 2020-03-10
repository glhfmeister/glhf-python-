import random

square = 24

emptypoints = random.randint (100,1000)

pointx = random.randint (-4,4)
pointy = random.randint (-6,0)

hit = 0

for i in range (emptypoints):

        storona1 = (3/2)*pointx-pointy-6
        storona2 = (-3/2)*pointx-pointy-6
        
        if storona1 <=0 and storona2 <=0:

                hit += 1
                print ("x = ",pointx,"y = ",pointy)
        
print ('48')
print(square)
hit = hit/emptypoints*square
print (hit)
