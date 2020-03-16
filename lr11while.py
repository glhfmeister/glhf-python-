import random

pointy = -6
pointx = -4
points = 0
hit = 0

while  pointy <= 0:

        pointx = -4

        while pointx <= 4:

                storona1 = (3/2)*pointx-pointy-6
                storona2 = (-3/2)*pointx-pointy-6
                
                print ("x = ",pointx,"y = ",pointy)
                
                if storona1 <=0 and storona2 <=0:

                        hit += 1
                        print ('+')
                
                points += 1
                pointx += 0.1

        pointy += 0.1
        
print ('48')
print('24')
hit = hit/points*48
print (hit)

