# Importing PyQT Modules. I use PyQT-5 module 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

# Main App Object and Settings
app=QApplication([])
mainWindow=QWidget()
mainWindow.setWindowTitle("Random Words Generator")
mainWindow.resize(300,200)

# Creating Widgets
title=QLabel("Random Keywords")

text1=QLabel("?")
text2=QLabel("?")
text3=QLabel("?")

button1=QPushButton("Generate")
button2=QPushButton("Generate")
button3=QPushButton("Generate")

# Design Section with Box Layout
masterLayout=QVBoxLayout()

row1=QHBoxLayout()
row2=QHBoxLayout()
row3=QHBoxLayout()

row1.addWidget(title,alignment=Qt.AlignCenter)

row2.addWidget(text1,alignment=Qt.AlignCenter)
row2.addWidget(text2,alignment=Qt.AlignCenter)
row2.addWidget(text3,alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

masterLayout.addLayout(row1)
masterLayout.addLayout(row2)
masterLayout.addLayout(row3)

mainWindow.setLayout(masterLayout)

# Functions to Create Own Random Words Generator
import random
myWords=["Sample", "Random", "Words", "Generator", "with", "PyQT", "by", "Sudhanex",
         "Provide", "Star", "for", "this", "Work"]

def randomWord():
    word=random.choice(myWords)
    text1.setText(word)
def randomWord1():
    word=random.choice(myWords)
    text2.setText(word)
def randomWord2():
    word=random.choice(myWords)
    text3.setText(word)

# Trigger Events with Buttons
button1.clicked.connect(randomWord)
button2.clicked.connect(randomWord1)
button3.clicked.connect(randomWord2)

# Show and Execute App
mainWindow.show()
app.exec_()
