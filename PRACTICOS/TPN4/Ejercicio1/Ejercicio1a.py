# '''
# 1. Desarrolle dos ejemplos del uso de un dialog:
# a. Un cuadro de diálogo que indique el siguiente mensaje “Está seguro que quiere
# dar de baja al usuario”, con los botones de aceptar y cancelar.


# '''
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from custom_dialog import CustomDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ejercicio-1-a")
        
        button = QPushButton("Ejercicio A")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        
    def button_clicked(self,s):
        print("Presionar",s)
        
        dlg = CustomDialog(self)
        
        if dlg.exec():
            print("Si estoy seguro")
        else:
            print("Cancelar")
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

