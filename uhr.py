from time import sleep, time, localtime
from tkinter import Tk, Canvas
from math import cos, sin, radians


                                #sek = 12 # eine Sekunde sind 6 Grad
# for sek in range(60):
def stelle_zeiger(sek, min, hour):
    alpha = radians((-6 * sek)+90)
    xz = cos(alpha)
    yz = sin(alpha)
    xb = (350 * xz) + 400
    yb = (-350 * yz) + 400
    mycanvas.coords(sekundenzeiger, 400,400, xb, yb)
    

    alpha = radians((-360//60 * min) +90)
    xz = cos(alpha)
    yz = sin(alpha)
    xb = (300 * xz) + 400
    yb = (-300 * yz) + 400
    mycanvas.coords(mintuenenzeiger, 400,400, xb, yb)
    sek += 1
    if sek >= 60:
        min += 1
        sek = 0
        min %= 60

    alpha = radians((-360//12 * (hour+min/60)) +90)   
    xz = cos(alpha)
    yz = sin(alpha)
    xb = (200 * xz) + 400
    yb = (-200 * yz) + 400
    mycanvas.coords(stundenzeiger, 400,400, xb, yb)
    
    if min >= 59:
        hour += 1
        min = 0
        hour %= 60

    root.after(1000, lambda: stelle_zeiger(sek, min, hour))

root = Tk()
mycanvas = Canvas(root, bg="black", width=800, height=800)
mycanvas.pack()
uhr = mycanvas.create_oval(50,50,750,750, fill="white")
sekundenzeiger=mycanvas.create_line(400,400, 350, 400, fill="red", width=2) # 726 275
mintuenenzeiger=mycanvas.create_line(400,400, 350, 400, fill="blue", width=4) # 726 275
stundenzeiger=mycanvas.create_line(400,400, 350, 400, fill="black", width=7) # 726 275

punkt= mycanvas.create_oval(395,395,405,405, fill="red")

for i in range(60):
    alpha = radians(-6*i+90)
    xz = cos(alpha)
    yz = sin(alpha)
    xa = (350 * xz) + 400
    ya = (-350 * yz) + 400
    xi = (320 * xz) + 400
    yi = (-320 * yz) + 400
    mycanvas.create_line(xa, ya, xi, yi, fill="darkblue", width="2")

for i in range(12):
    alpha = radians(-360//12*i+90)
    xz = cos(alpha)
    yz = sin(alpha)
    xa = (350 * xz) + 400
    ya = (-350 * yz) + 400
    xi = (300 * xz) + 400
    yi = (-300 * yz) + 400
    mycanvas.create_line(xa, ya, xi, yi, fill="darkviolet", width="5")




#     phi = radians(-6 * sek + 90) # phi  = Winkel # radians formt Winkel in Bogen
#     xz =  cos(phi)
#     yz = sin(phi) 
#     xb = 350 * xz + 400
#     yb = -350 * yz + 400

#     mycanvas.coords(zeiger, 400,400, xb, yb) # 726 275
#     root.update()
#     sleep(1)

s = localtime(time())[5]
m = localtime(time())[4]
h = localtime(time())[3]

stelle_zeiger(s, m, h)
root.mainloop()



