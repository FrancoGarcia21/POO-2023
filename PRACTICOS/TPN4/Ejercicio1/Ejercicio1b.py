'''
b. Un cuadro de diálogo que sea capaz de obtener un texto ingresado por el
usuario y que luego lo muestre en otro cuadro de diálogo

'''

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MianWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1-B")
        self.label = QLabel()
        self.input = QLineEdit()
        
        self.input.textChanged.connect(self.label.setText)## ESTO DEBO CAMBIAR
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        
        container.setLayout(layout)
        self.setCentralWidget(container)
        
app = QApplication(sys.argv)
window = MianWindow()
window.show()
app.exec()