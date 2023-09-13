import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de Input con PyQt5")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Texto ingresado:", self)
        self.label.setGeometry(20, 20, 200, 30)

        self.button = QPushButton("Ingresar Texto", self)
        self.button.setGeometry(20, 60, 150, 30)
        self.button.clicked.connect(self.mostrar_input_dialog)

    def mostrar_input_dialog(self):
        texto, ok_presionado = QInputDialog.getText(self, "Ingresar Texto", "Por favor, ingrese un texto:")

        if ok_presionado:
            self.label.setText(f"Texto ingresado: {texto}")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
