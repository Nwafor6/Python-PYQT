# import modules
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random word app")
main_window.resize(300, 200)

# create all app objects
title = QLabel("Random Word")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me!")
button2 = QPushButton("Click Me!")
button3 = QPushButton("Click Me!")

randmon_words = ["Hello", "Hey", "Glory", "Me", "Prince"]

# design goes here

master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()


row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)


master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)


# create functions
def get_randmon_word(text_lable):
    word = choice(randmon_words)
    if text_lable == 1:
        text1.setText(word)
    elif text_lable == 2:
        text2.setText(word)
    elif text_lable == 3:
        text3.setText(word)
    else:
        raise ValueError(f"{text_lable} not a valid label")


# event

button1.clicked.connect(lambda: get_randmon_word(1))
button2.clicked.connect(lambda: get_randmon_word(2))
button3.clicked.connect(lambda: get_randmon_word(3))

# show/run the app
main_window.show()
app.exec()
