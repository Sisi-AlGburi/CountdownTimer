import sys
import os
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Countdown App")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(500, 380)

        # Set background image
        image_path = os.path.join(os.path.dirname(__file__), "beach.jpg")
        background_image = QPixmap(image_path)
        self.background_label = QLabel(self)
        self.background_label.setPixmap(background_image.scaled(self.size(), Qt.IgnoreAspectRatio))
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # Set up widgets
        self.time_label = QLabel("Enter time in seconds:", self)
        self.time_input = QLineEdit(self)
        self.start_button = QPushButton("Start", self)
        self.pause_button = QPushButton("Pause", self)
        self.pause_button.setDisabled(True)
        self.countdown_label = QLabel(self)

        # Set up layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.time_label)
        input_layout.addWidget(self.time_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.countdown_label)
        main_layout.addStretch()

        self.setLayout(main_layout)

        # Set up timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_countdown)

        # Connect button signals
        self.start_button.clicked.connect(self.start_countdown)
        self.pause_button.clicked.connect(self.pause_countdown)

    def start_countdown(self):
        try:
            self.total_seconds = int(self.time_input.text())
        except ValueError:
            return
        self.timer.start(1000)
        self.start_button.setDisabled(True)
        self.pause_button.setDisabled(False)

    def pause_countdown(self):
        self.timer.stop()
        self.start_button.setDisabled(False)
        self.pause_button.setDisabled(True)

    def update_countdown(self):
        self.total_seconds -= 1
        if self.total_seconds <= 0:
            self.timer.stop()
            self.countdown_label.setText("Countdown complete!")
            self.start_button.setDisabled(False)
            self.pause_button.setDisabled(True)
        else:
            time = QTime(0, 0, 0).addSecs(self.total_seconds).toString("hh:mm:ss")
            self.countdown_label.setText(time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CountdownApp()
    ex.show()
    sys.exit(app.exec_())
