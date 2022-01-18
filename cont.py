from ast import Global
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog
from gestor_ventana import Ui_gestor
import sys
from venta_tab import Ui_ventana
import time
from threading import Thread


class container(QWidget):
    def __init__(self):
        super().__init__()
        self.Ui = Ui_gestor()
        self.Ui.setupUi(self)
        self.Ui.btn_vent2.clicked.connect(lambda:t.mostrar())

class container2(QDialog):
    def __init__(self, ven):
        super().__init__()
        self.Ui = ven()
        self.Ui.setupUi(self)

class treadding(Thread):
    def __init__(self, windo):
        Thread.__init__(self)
        self.ventan = windo
    
    def mostrar(self):
    
        cot.show()
        return cot




if __name__=="__main__":
    app = QApplication(sys.argv)
    

    ventan = container()
    ventan.show()
    cot = container2(Ui_ventana)
    t = treadding(cot)
    t.start()
    sys.exit(app.exec())