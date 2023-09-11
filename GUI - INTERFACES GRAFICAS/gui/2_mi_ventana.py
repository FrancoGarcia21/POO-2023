import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):# hago mi propia ventnaa que herede de esta clase
    def __init__(self):# porque estoy heredando de ventana
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        button = QPushButton("Apreta")
        self.setFixedSize(QSize(400, 300))#le da el tamanio de la ventana
        self.setCentralWidget(button)# lo centra

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


