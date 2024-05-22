import tkinter
from tkinter import *
import math
from threading import Thread 
from collections import defaultdict
from tkinter import ttk
import matplotlib.pyplot as plt 
import numpy as np
import time
import random
import cv2
global vehicle
global labels
global vehicle_x
global vehicle_y
global text
global canvas
global vehicle_list, root
global normal, attack
import cv2
import numpy as np
import math
import ctypes




class ShowMatrixPic():
    def __init__(self, row=0, column=0, atuoTile=False, width=200, height=200, text='None'):
        super(ShowMatrixPic, self).__init__()
        self.row = row
        self.column = column
        self.atuoTile = atuoTile
        self.width = width
        self.height = height
        self.text = text
        if self.row < 0:
            self.row = 0
        if self.column < 0:
            self.column = 0


        # user32 = ctypes.windll.user32
        # screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        # print(screensize)
        #

    def __rawAndColumn(self,imgList):
        r = c = 0
        resSubtraction = 1
        if self.column == 0 and self.row == 0:
            lenList = len(imgList)
            k = round(math.sqrt(lenList))
            if k > 5:
                r = 5
                if lenList % r == 0:
                    c = lenList // k
                else:
                    num2 = lenList // r
                    if num2 > r:
                        c = k + (num2 - r)
                    else:
                        c = k + num2


            else:
                r = k
                if lenList % r == 0:
                    c = lenList // r
                else:
                    u = r ** 2
                    num2 = lenList % r
                    if u < lenList:
                        if num2 < r:
                            c = r + 1
                        else:
                            c = r + num2
                    else:
                        c = r
        elif self.column == 0 and self.row != 0:
            lenList = len(imgList)
            r = self.row
            c = math.ceil(lenList / self.row)
        elif self.column != 0 and self.row == 0:
            lenList = len(imgList)
            c = self.column
            r = math.ceil(lenList / self.column)
        else:
            r = self.row
            c = self.column

        return r, c

    def showVideo(self, imgList):

        r, c = self.__rawAndColumn(imgList)


        image = []
        l = len(imgList)
        print(l)
        for img in imgList:
            # print(img)
            if img is not None:
                img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_AREA)
            else:
                img = np.zeros((self.height, self.width, 3), np.uint8)
                textSize = round(self.width * 0.005, 2)
                textThickness = round(self.width / 100)
                cv2.putText(img, self.text, ((self.width // 4), (self.height // 2)), cv2.FONT_HERSHEY_COMPLEX,
                            textSize, (255, 255, 255), textThickness)

            image.append(img)




        if not self.atuoTile:
            lenOfimg = len(imgList)
            tableNum = r * c
            emptyImg = np.zeros((self.height, self.width, 3), np.uint8)
            h, w = emptyImg.shape[:2]
            textSize = round(w * 0.005, 2)
            textThickness = round(w / 100)
            cv2.putText(emptyImg, self.text, ((w // 4), (h // 2)), cv2.FONT_HERSHEY_COMPLEX,
                        textSize, (255, 255, 255), textThickness)
            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    image.append(emptyImg)
        else:
            lenOfimg = len(imgList)
            tableNum = r * c

            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    if o > lenOfimg:
                        image.append(image[o % lenOfimg])
                    else:
                        image.append(image[o])


        numpy_vertical = []

        for n in range(c):
            numpy_vertical.append(np.vstack((image[n * r:r + (n * r)])))
        numpy_horizontal = np.hstack(numpy_vertical)
        return numpy_horizontal

    def showPic(self, imgList):

        r, c = self.__rawAndColumn(imgList)

        image = []
        l = len(imgList)
        print(l)
        for i in range(l):
            img = cv2.imread(imgList[i])
            img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_AREA)
            image.append(img)
        if not self.atuoTile:
            lenOfimg = len(imgList)
            tableNum = r * c
            emptyImg = np.zeros((self.height, self.width, 3), np.uint8)
            h, w = emptyImg.shape[:2]
            textSize = round(w * 0.005, 2)
            textThick = round(w / 100)
            cv2.putText(emptyImg, self.text, ((w // 4), (h // 2)), cv2.FONT_HERSHEY_COMPLEX,
                        textSize, (255, 255, 255), textThick)
            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    image.append(emptyImg)

        numpy_vertical = []

        for n in range(c):
            numpy_vertical.append(np.vstack((image[n * r:r + (n * r)])))
        numpy_horizontal = np.hstack(numpy_vertical)
        return numpy_horizontal

def checkVelocity(x1, y1, index):
    velo = ""
    for i in range(len(vehicle_x)):
        if i != index:
            velocity = math.sqrt((vehicle_x[i] - x1)**2 + (vehicle_y[i] - y1)**2)
            velo += str(velocity)+" "
    print(velo)

def startDataTransferSimulation(line1, line2):
    class SimulationThread(Thread):
        global vehicle
        global labels
        global vehicle_x
        global vehicle_y
        global normal, attack
        def __init__(self, line1, line2): 
            Thread.__init__(self) 
            self.line1 = line1
            self.line2 = line2
             
        def run(self):
            time.sleep(0.01)
            pos=0
            for i in range(0,30):
                for i in range(0,4):
                    canvas.delete(vehicle[i])
                    canvas.delete(labels[i])
                status = random.randint(0, 2)
                if status == 0:
                    pos = random.randint(20, 60)
                    use_energy = random.randint(2, 10)
                    break_appy=random.randint(1,2)
                    temp_monitor=random.randint(15,28)
                    normaltemp.append(temp_monitor)
                    attacktemp.append(temp_monitor)
                    normal.append(use_energy)
                    attack.append(use_energy)
                    normalbreak.append(break_appy)
                    attackbreak.append(break_appy)
                if status == 1:
                    pos = random.randint(40, 80)
                    use_energy = random.randint(2, 10)
                    
                    break_appy=random.randint(1,2)
                    temp_monitor=random.randint(15,28)
                    normaltemp.append(temp_monitor)
                    normalbreak.append(break_appy)
                    normal.append(use_energy)
                    use_energy = random.randint(10, 20)
                    temp_monitor=random.randint(30,60)
                    attack.append(use_energy)
                    break_appy=random.randint(5,10)
                    attackbreak.append(break_appy)
                    attacktemp.append(temp_monitor)
                    text.insert(END,"Attack Detected Vehicle Velocity increased to "+str(pos)+" from normal range 20 & 60\n") 
                for i in range(len(vehicle_x)):
                    vehicle_x[i] = vehicle_x[i] +  pos
                    checkVelocity(vehicle_x[i], vehicle_y[i], i)
                time.sleep(0.01)
                for i in range(0,4):
                    vehicle[i] = canvas.create_oval(vehicle_x[i],vehicle_y[i],vehicle_x[i]+40,vehicle_y[i]+40, fill="red")
                    labels[i] = canvas.create_text(vehicle_x[i]+20,vehicle_y[i]-10,fill="darkblue",font="Times 8 italic bold",text="V"+str(i+1))
                time.sleep(1)
                canvas.update()
            plt.figure(figsize=(10,6))
            plt.grid(True)
            plt.xlabel('Time')
            plt.ylabel('Energy Consumption')
            plt.plot(normal, 'ro-',color = 'green')
            plt.plot(attack, 'ro-', color = 'red')
            plt.legend(['Energy in Normal Conditions', 'Energy in Attack Conditions'], loc='upper left')
            plt.title('Residual Energy Graph Comparison')
            plt.savefig("./results/Energy.png")
            #plt.show()
            
            plt.figure(figsize=(10,6))
            plt.grid(True)
            plt.xlabel('Time')
            plt.ylabel('Break Usage')
            plt.plot(normalbreak, 'ro-',color = 'green')
            plt.plot(attackbreak, 'ro-', color = 'red')
            plt.legend(['Break Usage in Normal Conditions', 'Break Usage in Attack Conditions'], loc='upper left')
            plt.title('Residual Break Usage Graph Comparison')
            plt.savefig("./results/Break.png")
            #plt.show()

            
            plt.figure(figsize=(10,6))
            plt.grid(True)
            plt.xlabel('Time')
            plt.ylabel('Temperature Monitor')
            plt.plot(normaltemp, 'ro-',color = 'green')
            plt.plot(attacktemp, 'ro-', color = 'red')
            plt.legend(['Temperature Monitor in Normal Conditions', 'Temperature Monitor in Attack Conditions'], loc='upper left')
            plt.title('Temperature Monitork Usage Graph Comparison')
            plt.savefig("./results/etemperature.png")


            
            smp = ShowMatrixPic(width=500, height=500, row=1, column=3, atuoTile=True)
            imgListOne = ['./results/Energy.png','./results/Break.png' ,'./results/etemperature.png']
            numpy_horizontal = smp.showPic(imgListOne)
            cv2.imshow('Output', numpy_horizontal)
            cv2.imwrite("./results/out.png",numpy_horizontal)
            cv2.waitKey(0)
    
    newthread = SimulationThread(line1, line2) 
    newthread.start()

def simulation():
    global vehicle
    global labels
    global vehicle_x
    global vehicle_y
    global normal, attack,normalbreak,attackbreak,normaltemp,attacktemp
    normal = []
    normalbreak=[]
    attackbreak=[]
    normaltemp=[]
    attacktemp=[]
    attack = []
    vehicle = []
    labels = []
    vehicle_x = []
    vehicle_y = []
    line1 = canvas.create_line(10, 100, 1000, 100, fill='black',width=3)
    line2 = canvas.create_line(10, 300, 1000, 300, fill='black',width=3)

    x = 10
    y = 250
    for i in range(0, 4):
        vehicle_x.append(x)
        vehicle_y.append(y)
        name = canvas.create_oval(x,y,x+40,y+40, fill="red")
        lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 8 italic bold",text="V"+str(i+1))
        labels.append(lbl)
        vehicle.append(name)
        x = x + 100
    startDataTransferSimulation(line1, line2)

def Main():
    global root
    global text
    global canvas
    root = tkinter.Tk()
    root.geometry("1300x1200")
    root.title("Systematic Assessment of Cyber-Physical Security of Energy Management System for Connected and Automated Electric Vehicles")
    root.resizable(True,True)
    font1 = ('times', 12, 'bold')

    canvas = Canvas(root, width = 1000, height = 500)
    canvas.pack()

    text=Text(root,height=12,width=130)
    scroll=Scrollbar(text)
    text.configure(yscrollcommand=scroll.set)
    text.place(x=100, y=380)

    simulation()
    
    root.mainloop()

if __name__== '__main__' :
    Main ()
