import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import os

os.chdir(f"{os.path.abspath(__file__)}/../../..")

class MenuIzquierdo(qtw.QToolBar):
    def __init__(self):
        super().__init__()

        self.setOrientation(qtc.Qt.Orientation.Vertical)
        self.setFloatable(False)
        self.setMovable(False)

        titulo=qtw.QLabel("Gestiones: ")
        titulo.setObjectName("gestiones-titulo")
        self.gestion1=qtw.QRadioButton('GESTIÓN DE HERRAMIENTAS')
        self.gestion2=qtw.QRadioButton('Gestión de Herramientas viejo')
        self.gestion1.setObjectName("gestion")
        self.gestion2.setObjectName("gestion")

        self.addWidget(titulo)
        self.addWidget(self.gestion1)
        self.addWidget(self.gestion2)

        self.gestion1.toggle()
        
        with open(f"{os.path.abspath(os.getcwd())}/duraam/styles/menu_izquierdo.qss", "r") as qss:
            self.setStyleSheet(qss.read())