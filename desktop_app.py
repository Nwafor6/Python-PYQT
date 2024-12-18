import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QGraphicsDropShadowEffect,
    QFrame,
    QStackedWidget,
)
from PyQt5.QtGui import QFont, QColor, QLinearGradient, QPalette, QPainter
from PyQt5.QtCore import Qt, QSize


class GradientWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(53, 132, 228))  # Blue
        gradient.setColorAt(1, QColor(36, 58, 94))  # Dark Blue
        painter.fillRect(self.rect(), gradient)


class ModernStyledApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def create_shadow_effect(self, blur_radius=20, color=QColor(0, 0, 0, 100)):
        """Create a sophisticated shadow effect"""
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(blur_radius)
        shadow.setColor(color)
        shadow.setOffset(0, 5)
        return shadow

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Modern Interactive App")
        self.setGeometry(100, 100, 500, 600)
        self.setMinimumSize(400, 500)

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Background Widget
        background = GradientWidget()
        background_layout = QVBoxLayout(background)
        main_layout.addWidget(background)

        # Content Frame
        content_frame = QFrame()
        content_frame.setStyleSheet(
            """
            QFrame {
                background-color: rgba(255, 255, 255, 230);
                border-radius: 15px;
            }
        """
        )
        content_frame.setGraphicsEffect(self.create_shadow_effect())

        # Content Layout
        content_layout = QVBoxLayout(content_frame)

        # Title
        title_label = QLabel("Welcome to Interactive App")
        title_label.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            color: #2C3E50;
            margin-bottom: 20px;
            text-align: center;
        """
        )
        content_layout.addWidget(title_label)

        # Name Input Section
        name_layout = QVBoxLayout()
        name_label = QLabel("Enter Your Name:")
        name_label.setStyleSheet(
            """
            font-size: 16px;
            color: #34495E;
        """
        )

        self.name_input = QLineEdit()
        self.name_input.setStyleSheet(
            """
            QLineEdit {
                padding: 10px;
                border: 2px solid #3498DB;
                border-radius: 10px;
                font-size: 16px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #2980B9;
            }
        """
        )
        self.name_input.setPlaceholderText("Type your name here...")

        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        content_layout.addLayout(name_layout)

        # Button Layout
        button_layout = QHBoxLayout()

        # Greeting Button
        self.greet_button = QPushButton("Say Hello")
        self.greet_button.setStyleSheet(
            """
            QPushButton {
                background-color: #3498DB;
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 10px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #21618C;
            }
        """
        )
        self.greet_button.clicked.connect(self.show_greeting)

        # Clear Button
        clear_button = QPushButton("Clear")
        clear_button.setStyleSheet(
            """
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 10px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
            QPushButton:pressed {
                background-color: #A93226;
            }
        """
        )
        clear_button.clicked.connect(self.clear_input)

        button_layout.addWidget(self.greet_button)
        button_layout.addWidget(clear_button)
        content_layout.addLayout(button_layout)

        # Add content frame to background
        background_layout.addStretch(1)
        background_layout.addWidget(content_frame)
        background_layout.addStretch(1)

    def show_greeting(self):
        name = self.name_input.text().strip()
        if name:
            greeting_dialog = QMessageBox(self)
            greeting_dialog.setWindowTitle("Greeting")
            greeting_dialog.setText(f"Hello, {name}!")
            greeting_dialog.setIcon(QMessageBox.Information)
            greeting_dialog.exec_()
        else:
            error_dialog = QMessageBox(self)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Please enter a name.")
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.exec_()

    def clear_input(self):
        """Clear the name input field"""
        self.name_input.clear()


def main():
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    main_window = ModernStyledApp()
    main_window.show()

    # Run the application
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
