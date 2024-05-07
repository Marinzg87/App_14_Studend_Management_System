from PyQt6.QtWidgets import (QApplication, QLabel, QWidget,
                             QGridLayout, QLineEdit, QPushButton,
                             QComboBox)
import sys
from datetime import datetime


class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Metric (km)', 'Imperial (miles)'])

        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_average_speed)
        self.output_label = QLabel("")

        # Add widgets to the grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_average_speed(self):
        distance = self.distance_line_edit.text()
        distance = int(distance)
        if self.combo.currentText () == 'Metric (km)':
            time = self.time_line_edit.text()
            time = int(time)
            average_speed = distance / time
            label = "kmh"
        if self.combo.currentText () == 'Imperial (miles)':
            time = self.time_line_edit.text()
            time = int(time)
            average_speed = distance / (time * 1.6)
            label = "mph"

        self.output_label.setText(f"Average speed is: {average_speed} {label}")


app = QApplication(sys.argv)
average_speed_calculator = AverageSpeedCalculator()
average_speed_calculator.show()
app.exit(app.exec())
