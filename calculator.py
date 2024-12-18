from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setting_layout()
        self.initUi()

    def setting_layout(self):
        self.setWindowTitle("Calculator")
        self.resize(300, 400)

    def initUi(self):
        self.master_layout = QVBoxLayout()
        self.bottom_row = QHBoxLayout()

        self.text_box = QLineEdit()
        self.grid = QGridLayout()
        self.clear_btn = QPushButton("C")
        self.delete_btn = QPushButton("<")
        self.buttons = [
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            ".",
            "=",
            "+",
        ]

        # add the bottons to the grids
        for button in self.buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.keyPressEvent)
            self.grid.addWidget(
                btn, self.buttons.index(button) // 4, self.buttons.index(button) % 4
            )

        # add the events to the buttons
        self.clear_btn.clicked.connect(self.keyPressEvent)
        self.delete_btn.clicked.connect(self.keyPressEvent)

        # ADD THE CLEAR AND DELETE BUTTOM TO THE BOTTOM ROW
        self.bottom_row.addWidget(self.clear_btn)
        self.bottom_row.addWidget(self.delete_btn)

        self.master_layout.addWidget(self.text_box)
        self.master_layout.addLayout(self.grid)
        self.master_layout.addLayout(self.bottom_row)

        self.setLayout(self.master_layout)

    def keyPressEvent(self):
        """event to be trigered by buttons"""
        text = self.sender().text()

        if text == "=":
            # the user wants to evealue his result
            try:
                result = eval(self.text_box.text())
                self.text_box.setText(str(result))
            except Exception:
                self.text_box.setText("Error")
        elif text == "C":
            # clear the text box
            self.text_box.clear()
        elif text == "<":
            # delete the last character from the text box
            text = self.text_box.text()
            self.text_box.setText(text[:-1])
        else:
            # add the text to the text box
            self.text_box.setText(str(self.text_box.text()) + text)


if __name__ == "__main__":
    app = QApplication([])
    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())
    calculator = Calculator()
    calculator.show()
    app.exec_()
