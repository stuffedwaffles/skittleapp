import tkinter
from tkinter import *
import time as t
import asyncio 
import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 

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

        with open(r'stuf\actual projects\skittleapp\skittlestat.txt', 'r') as f:
            file = f.read()
            skittle_dict = eval(file)
        skittle_dict[color].append(percentAsDecimalColor)

        with open(r'stuf\actual projects\skittleapp\skittlestat.txt', 'w') as f:
            file = f.write(str(skittle_dict))


        self.close()

        

class ShowWindow(QWidget):
    def __init__(self):
        super().__init__()


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
