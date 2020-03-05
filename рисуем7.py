import math as m
from tkinter import *

root = Tk()
root.title('<***>')
root.geometry ('1000x1000')
holst = Canvas (root, bg = '#22457E',width = 1000,height = 1000)

'''
holst.create_text(625,477,fill = "gray",font="timesnewroman 7",text="Меркурий")
holst.create_oval (400,400,600,600,fill = 'yellow',width = 5)
holst.create_oval (375,375,625,625,outline = 'black',width = 1)

holst.create_oval (612,487,638,513,fill = 'lightyellow',width = 1)
holst.create_text(625,477,fill = "gray",font="timesnewroman 7",text="Меркурий")
holst.create_oval (350,350,650,650,outline = 'black',width = 1)

holst.create_oval (337,487,363,513,fill = "#FF8000",width = 1)
holst.create_text(350,477,fill = "gray",font="timesnewroman 7",text="Венера")
holst.create_oval (325,325,675,675,outline = 'black',width = 1)

holst.create_oval (662,487,688,513,fill = "#6A6AFF",width = 1)
holst.create_text(674,525,fill = "gray",font="timesnewroman 7",text="Земля")
holst.create_oval (657,482,693,518,width = 1)
holst.create_oval (688,488,693,493,fill = "gray",width = 1)
holst.create_oval (300,300,700,700,outline = 'black',width = 1)

holst.create_oval (288,487,313,513,fill = "red",width = 1)
holst.create_text(300,525,fill = "gray",font="timesnewroman 7",text="Марс")
holst.create_oval (283,480,320,520,width = 1)
holst.create_oval (315,487,320,493,fill = "gray",width = 1)
holst.create_oval (283,487,288,493,fill = "gray",width = 1)
holst.create_oval (275,275,725,725,outline = 'black',width = 1)

holst.create_oval (708,483,742,517,fill = "#A60000",width = 1)
holst.create_text(725,477,fill = "gray",font="timesnewroman 7",text="Юпитер")
holst.create_oval (250,250,750,750,outline = 'black',width = 1)

holst.create_oval (237,487,263,513,fill = "#FFFF28",width = 1)
holst.create_text(250,530,fill = "gray",font="timesnewroman 7",text="Сатурн")
holst.create_oval (228,478,272,522,width = 3,outline = "#FFFF10")
holst.create_oval (232,482,268,518,width = 2,outline = "#FFFF10")
holst.create_oval (225,225,775,775,outline = 'black',width = 1)

holst.create_oval (762,487,788,513,fill = "#0080C0",width = 1)
holst.create_text(775,477,fill = "gray",font="timesnewroman 7",text="Уран")
holst.create_oval (200,200,800,800,outline = 'black',width = 1)

holst.create_oval (181,481,219,519,fill = "blue",width = 1)
holst.create_text(200,472,fill = "gray",font="timesnewroman 7",text="Нептун")
'''
'''

holst.create_polygon ([100,100],[150,150],[250,150],[300,100],fill = 'red',outline = 'black',width = 5)

holst.create_polygon ([350,150],[400,300],[550,300],[600,150],[475,50],fill = 'yellow',outline = 'black',width = 5)

holst.create_polygon ([650,150],[650,250],[700,250],[700,300],[800,300],[800,250],[850,250],[850,150],[800,150],[800,100],[700,100],[700,150],fill = 'green',outline = 'black',width = 5)

'''
'''
a = int (input('Dlina stor kvadrata'))
y = int (input('koordiata verh Y'))
x = int(input('Koordinata verhn X'))
xa = x + a
ya = y + a
holst.create_rectangle (x,y,xa,ya,fill = 'red')
holst.create_oval (x,y,xa,ya,fill = 'green')

xa2 = (xa + x) / 2
a = a / 2
xa3 = m.sqrt (a*a / 2)

ya2 = (ya + y) / 2
ya3 = m.sqrt(a * a / 2)
holst.create_rectangle (xa2-xa3,ya2-ya3,xa2+xa3,ya2+ya3,fill = 'blue')

'''
'''
holst.create_line (0,350,100,350,fill = 'blue')
holst.create_line (50,300,50,450,fill = 'blue')
holst.create_line (25,400,75,425,fill = 'blue')

holst.create_line (0,500,100,550,fill = 'red')
holst.create_line (0,550,100,500,fill = 'black')

'''
'''
holst.create_rectangle (0,67,300,134,fill = 'blue') 
holst.create_rectangle (0,134,300,200,fill = 'red')

holst.create_rectangle (350,0,450,200,fill = 'red') 
holst.create_rectangle (550,0,650,200,fill = 'indigo')

holst.create_rectangle (700,0,1000,67,fill = 'black')
holst.create_rectangle (700,67,1000,133,fill = 'red')
holst.create_rectangle (700,133,1000,200,fill = 'yellow')
'''
'''
'''
holst.create_rectangle (0,0,1000,1000,fill = 'blue')
holst.create_rectangle (0,0,500,500,fill = 'red')

holst.create_rectangle (500,500,1000,1000,fill = 'chocolate')
holst.create_rectangle (0,0,500,500,fill = 'indigo')
'''
holst.pack ()
holst.mainloop ()
