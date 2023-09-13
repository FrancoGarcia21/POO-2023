import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit ,QLabel
import random
from PyQt6.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana que insulta")
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color: slategray; color: black;")
        
        
        # Crear un cuadro de texto
        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Ingresa tu nombre")
        self.input.setStyleSheet("background-color:white;")
        ### agregado----------------- 
        
        #-------------------------

        # Crear un botón
        self.button = QPushButton("Insultar", self)
        self.button.clicked.connect(self.insultar)
        self.button.setStyleSheet("background-color:white;")

        # Crear un layout vertical y agregar widgets
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        # Crear un widget contenedor y establecer el layout
        container = QWidget()
        container.setLayout(layout)

        # Establecer el widget contenedor como el widget central de la ventana
        self.setCentralWidget(container)
        
        self.label1= QLabel("")
        self.label1.setStyleSheet("background-color:white;")
        #self.label1.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label1)
        
        font = self.label1.font()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        #self.setCentralWidget(self.label1)##agregue esto lo rompio
        
    # def guardar_nombre(self):# calculo que esta demas 
    #     self.nombre_guardado = self.input.text()
    #     print(f"Nombre guardado: {self.nombre_guardado}")   
        

    def insultar(self):
        texto = self.input.text()
        lista = ["Tarado","Bolas tristes","Pecho Frio","Hincha de mexico"]
        opcion= random.choice(lista)
        if texto:
            insulto = f" Sos un {opcion}!"# esta mal usado creo que debo almacenar el nombre
        else:
            insulto = "Eres un sinvergüenza ni tu nombre supiste poner!"
        self.label1.setText(insulto)###

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
