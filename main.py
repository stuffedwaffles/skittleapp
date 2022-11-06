import tkinter
from tkinter import *
import time as t
import asyncio 
import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
import os



folder = os.path.dirname(os.path.abspath(__file__))
skittleFilePath = os.path.join(folder, "skittlestat.txt")


windowHeight = 500
windowWidth = 500


app = QApplication([])

class InputWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Data")
        self.setFixedSize(QSize(windowWidth, windowHeight))

        dialogLayout = QVBoxLayout()
        layout = QFormLayout()

        self.totalLine = QLineEdit()
        self.colorLine = QLineEdit()
        self.numLine = QLineEdit()

        layout.addRow("Total Skittles in pack: ", self.totalLine)
        layout.addRow("Enter skittle color (green, red, orange, yellow, purple): ", self.colorLine)
        layout.addRow("Enter the number of skittles of this color: ", self.numLine)
        dialogLayout.addLayout(layout)

        submit = QPushButton("Submit Data!")
        submit.clicked.connect(self.onSubmit)
        dialogLayout.addWidget(submit)

        self.setLayout(dialogLayout)
    
    def onSubmit(self):
        global totalPerPack
        totalPerPack = int(self.totalLine.text())
        global color
        color = self.colorLine.text()
        global totalColor
        totalColor = int(self.numLine.text())

        percentAsDecimalColor = round(totalColor/totalPerPack, 4)
        percentColor = percentAsDecimalColor *100

        with open(skittleFilePath, 'r') as f:
            file = f.read()
            skittle_dict = eval(file)
        skittle_dict[color].append(percentAsDecimalColor)

        with open(skittleFilePath, 'w') as f:
            file = f.write(str(skittle_dict))


        self.close()

class ShowWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Skittle Statistics")
        self.setFixedSize(QSize(windowWidth*2, windowHeight))
        self.mainlayout = QVBoxLayout()
        self.layout = QFormLayout()
        

        self.totalLine = QLineEdit()
        
        self.layout.addRow("Total Skittles in pack: ", self.totalLine)
        submit = QPushButton("Submit!")
        submit.clicked.connect(self.onSubmit)
        self.layout.addWidget(submit)

        self.datalayout = QFormLayout()
        self.greenLabel = QLabel()
        self.layout.addRow(f"Green: ", self.greenLabel)

        self.redLabel = QLabel()
        self.layout.addRow(f"Red: ", self.redLabel)

        self.orangeLabel = QLabel()
        self.layout.addRow(f"Orange: ", self.orangeLabel)

        self.purpleLabel = QLabel()
        self.layout.addRow(f"Purple: ", self.purpleLabel)

        self.yellowLabel = QLabel()
        self.layout.addRow(f"Yellow: ", self.yellowLabel)

        self.mainlayout.addLayout(self.layout)
        self.setLayout(self.mainlayout)
    
    def getLabel(self, color, percent_list, label):
        if len(percent_list) ==0:
                avg_percent_label = f"No data for {color}"
                avg_percent = None
                print("average percent",avg_percent,color)

        else:
            percent_sum = 0
            for percent in percent_list:
                percent_sum += percent
            avg_percent = (percent_sum/len(percent_list))*100
            print("average percent",avg_percent,color)
            avg_percent_label = f"Average Percent for {color}: {avg_percent}%"

        if avg_percent == None:
            in_pack = None
            print("inpack", in_pack, color)
            in_pack_label = f"Cannot calculate number of {color} skittles in pack"
        else:
            in_pack = (avg_percent/100)*totalPerPack
            print("inpack", in_pack, color)
            in_pack_label = f"There are approximately {int(in_pack)} {color} skittles in your pack."

        label.setText(f"{avg_percent_label}\t{in_pack_label}")


    def onSubmit(self):
        global totalPerPack
        totalPerPack = int(self.totalLine.text())

        

        with open(skittleFilePath, 'r') as f:
            file = f.read()
            skittle_dict = eval(file)

        
        
        for color, percent_list in skittle_dict.items():
            if color == "green":
                print("green label done")
                self.getLabel(color, percent_list, self.greenLabel)
            elif color == "red":
                print("red label done")
                self.getLabel(color, percent_list, self.redLabel)
            elif color == "orange":
                print("orange label done")
                self.getLabel(color, percent_list, self.orangeLabel)
            elif color == "purple":
                print("purple label done")
                self.getLabel(color, percent_list, self.purpleLabel)
            elif color == "yellow":
                print("yellow label done")
                self.getLabel(color, percent_list, self.yellowLabel)
        

        
        
        self.mainlayout.addLayout(self.datalayout)
        self.setLayout(self.mainlayout)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Skittle Stats 1.0")
        self.setFixedSize(QSize(windowWidth, windowHeight))

        title = QLabel("<h1>Welcome to the Skittle Stats App!</h1>", parent=self)
        title.setFixedSize(480,30)
        title.move(60,10)

        inputbtn = QPushButton("Input Data!", parent=self)
        inputbtn.setFixedSize(150,50)
        inputbtn.move(175,200)
        inputbtn.clicked.connect(self.input_window)

        showbtn = QPushButton("Show Stats!", parent=self)
        showbtn.setFixedSize(150,50)
        showbtn.move(175,300)
        showbtn.clicked.connect(self.show_window)

        closebtn = QPushButton("Close App", parent=self)
        closebtn.setFixedSize(150,50)
        closebtn.move(175,400)
        closebtn.clicked.connect(app.exit)

    def input_window(self, checked):
        self.w = InputWindow()
        self.w.show()

    def show_window(self, checked):
        self.w = ShowWindow()
        self.w.show()
        



window = MainWindow()

window.show()
sys.exit(app.exec())
