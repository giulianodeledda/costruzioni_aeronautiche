from tkinter import *
#
from AeroApp001Lib import *


rw_width = 500
rw_height = 800
x_start = 10
y_start = 10
x_step = 50
y_step = 30

index = 0


def getIndex():
    global index
    index +=1
    return index


def getPositionGrid(row, col):
    global rw_width, rw_height, x_start, y_start, x_step, y
    x_pos = x_start+x_step*(col-1)
    y_pos = y_start+y_step*(row-1)
    return str(x_pos), str(y_pos)


def doIt(self):
    df = getAeroData(float(cd0_entry.get()),float(k_entry.get()),float(clmin_entry.get()),float(clmax_entry.get()),int(pcl_entry.get()))
    showResults.delete("1.0",END)
    showResults.insert(END, str(df))
    print("done..."+version())
    pass

def doPlot01(self):
    df = getAeroData(float(cd0_entry.get()), float(k_entry.get()), float(clmin_entry.get()), float(clmax_entry.get()), int(pcl_entry.get()))
    values = df.to_numpy()
    plotIt(values[:,0],values[:,1])
    print("done..."+version())
    pass
def doPlot02(self):
    df = getAeroData(float(cd0_entry.get()), float(k_entry.get()), float(clmin_entry.get()), float(clmax_entry.get()), int(pcl_entry.get()))
    values = df.to_numpy()
    plotIt(values[:,0],values[:,2])
    print("done..."+version())
    pass

root = Tk()
root.title("Dipartimento di Meccanica e Aeronautica - Polare Aerodinamica")
root.geometry(str(rw_width)+"x"+str(rw_height))
root.resizable(0,0)

currentIndex = getIndex()
cd0_label = Label(root,text="CD0")
cd0_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
cd0 = StringVar()
cd0_entry = Entry(textvariable=cd0)
cd0_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
cd0.set("0.025")
cd0_entry.bind("<Key-Return>", doIt)

currentIndex = getIndex()
k_label = Label(root,text="k")
k_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
k = StringVar()
k_entry = Entry(textvariable=k)
k_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
k.set("0.05")
k_entry.bind("<Key-Return>", doIt)

currentIndex = getIndex()
clmin_label = Label(root,text="clmin")
clmin_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
clmin = StringVar()
clmin_entry = Entry(textvariable=clmin)
clmin_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
clmin.set("0.1")
clmin_entry.bind("<Key-Return>", doIt)

currentIndex = getIndex()
clmax_label = Label(root,text="clmax")
clmax_label.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
clmax = StringVar()
clmax_entry = Entry(textvariable=clmax)
clmax_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
clmax.set("1.50")
clmax_entry.bind("<Key-Return>", doIt)


currentIndex = getIndex()
pcl = Label(root, text="punti")
pcl.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
pcl = StringVar()
pcl_entry = Entry(textvariable=pcl)
pcl_entry.place(x=getPositionGrid(currentIndex, 2)[0], y=getPositionGrid(currentIndex, 2)[1])
pcl.set("10")
pcl_entry.bind("<Key-Return>", doIt)

currentIndex = getIndex()
doIt_button = Button(text="Esegui")
doIt_button.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
doIt_button.bind("<Button-1>", doIt)
doIt_button = Button(text="Polare Aer.")
doIt_button.place(x=getPositionGrid(currentIndex, 2.5)[0], y=getPositionGrid(currentIndex, 2.5)[1])
doIt_button.bind("<Button-1>", doPlot01)
doIt_button = Button(text="Eff. Aer.")
doIt_button.place(x=getPositionGrid(currentIndex, 4.5)[0], y=getPositionGrid(currentIndex, 4.5)[1])
doIt_button.bind("<Button-1>", doPlot02)


currentIndex = getIndex()
showResultsFrame = Frame()
xscrollbar = Scrollbar(showResultsFrame,orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)
yscrollbar = Scrollbar(showResultsFrame)
yscrollbar.pack(side=RIGHT, fill=Y)
showResultsFrame.place(x=getPositionGrid(currentIndex, 1)[0], y=getPositionGrid(currentIndex, 1)[1])
showResults = Text(showResultsFrame,height = 15, width = 65, wrap=NONE, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
showResults.pack()
xscrollbar.config(command=showResults.xview)
yscrollbar.config(command=showResults.yview)

root.mainloop()