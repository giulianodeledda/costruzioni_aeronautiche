from tkinter import *
#
import os
from math import *
from random import random

rw_width = 500
rw_height = 500
x_start = 10
y_start = 10
x_step = 120
y_step = 30

index = 0

## La variabile globale index stabilisce la riga sulla quale posizionare l'oggetto grafico
def getIndex(thestep = 1):
    global index
    index +=thestep
    return index

## Restituisce le coordinate x, y per posizionare l'oggetto grafico
def getPositionGrid(row, col):
    global rw_width, rw_height, x_start, y_start, x_step, y
    x_pos = x_start+x_step*(col-1)
    y_pos = y_start+y_step*(row-1)
    return str(x_pos), str(y_pos)

def getDensity(pressure, temperature):
    return pressure*100/(287*(temperature+273.15))

def doIt(self):
    thepressure = float(pressure_entry.get())
    thetemperature = float(temperature_entry.get())
    thedensity = getDensity(thepressure,thetemperature)
    density.set(round(thedensity,3))
    doIt2(self)


def getSpeed(ppressure, density):
    return sqrt(2*ppressure*9.80665/density)

def doIt2(self):
    theppressure = float(ppressure_entry.get())
    thedensity = float(density_entry.get())
    speed.set(round(getSpeed(theppressure,thedensity),3))
    speed2.set(round(3.6*getSpeed(theppressure, thedensity), 3))

copyrightlabel = "a cura del prof. Giuliano Deledda - DiMADid - Aeronautico - Nuoro"
def doIt3():
    global copyrightlabel
    copyrightlabel = str(random())

root = Tk()
root.title("Calcolo della velocità in galleria del vento")
root.geometry(str(rw_width)+"x"+str(rw_height))
root.resizable(0,0)
currentIndex = getIndex()

canvas = Canvas(width=460, height=210, bg='white')
canvas.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
cdir = os.getcwd()
##print(cdir+"/ccc")
png = PhotoImage(file="grafica.png")
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(5, 5, image=png, anchor=NW)

currentIndex = getIndex(7.5)
cond_label = Label(root, text="Condizioni ambiente")
cond_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])

currentIndex = getIndex()
pressure_label = Label(root, text="Pressione (mbar):")
pressure_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
pressure = StringVar()
pressure_entry = Entry(textvariable=pressure)
pressure_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
pressure.set("1013.25")
pressure_entry.bind("<Key-Return>", doIt)

currentIndex = getIndex()
temperature_label = Label(root, text="Temperatura (°C):")
temperature_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
temperature = StringVar()
temperature_entry = Entry(textvariable=temperature)
temperature_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
temperature.set("15.0")
temperature_entry.bind("<Key-Return>", doIt)

currentIndex = getIndex()
density_label = Label(root, text="Densità (kg/m^3):")
density_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
density = StringVar()
density_entry = Entry(textvariable=density, state="readonly")
density_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
density.set(str(round(getDensity(float(pressure_entry.get()),float(temperature_entry.get())),3)))

currentIndex = getIndex()
cond_label = Label(root, text="Calcolo della velocità del flusso")
cond_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])

currentIndex = getIndex()
ppressure_label = Label(root, text="Dp (mm H2O):")
ppressure_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
ppressure = StringVar()
ppressure_entry = Entry(textvariable=ppressure)
ppressure_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
ppressure.set("30")
ppressure_entry.bind("<Key-Return>", doIt2)

currentIndex = getIndex()
speed = StringVar()
speed_label = Label(root, text="v (m/s):")
speed_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
speed_entry = Entry(textvariable=speed,state="readonly")
speed_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
speed.set(str(round(getSpeed(float(ppressure_entry.get()),float(density_entry.get())),3)))

currentIndex = getIndex()
speed2 = StringVar()
speed2_label = Label(root, text="v (km/h):")
speed2_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
speed2_entry = Entry(textvariable=speed2,state="readonly")
speed2_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
speed2.set(str(round(float(speed_entry.get())*3.6,3)))


currentIndex = getIndex()
copyright_label = Label(root, text=copyrightlabel)
copyright_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
copyright_label.after(2000, doIt3)
root.mainloop()
