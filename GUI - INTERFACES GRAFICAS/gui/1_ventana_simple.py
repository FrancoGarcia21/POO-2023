from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
app = QApplication(sys.argv)
#window = QWidget()
#window = QPushButton("Apreta")
window = QMainWindow()#cada vez que creo una ventana debo decirle que se muestre
window.show()  # las ventanas por defecto no se muestran, hay que mostrarlas
# Comienza el loop de eventos.
app.exec()

#lo que esta aca abajo no se ejecuta.