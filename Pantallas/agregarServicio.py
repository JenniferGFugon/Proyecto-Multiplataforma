from menu import Menu
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image

class AgregarServicio(QWidget):
    """ Ventana para agregar nuevos servicios """

    def __init__(self):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar un servicio")
        self.setGeometry(430, 120, 750, 450)
        self.UI()
        
    def UI(self):
        """ Componentes del diseño de la ventana """
        self.encabezado()
        self.labels()
        self.botones()
        
    def encabezado(self):
        """ Encabezado de la ventana """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(0, 0, 0))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(2000)
        frame.setFixedHeight(84)
        frame.move(0, 0)

        logo = QLabel(frame)
        logo.setFixedWidth(90)
        logo.setFixedHeight(50)
        logo.setPixmap(QPixmap("Logo.png").scaled(90, 90, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        logo.move(20, 12)

        fuente = QFont()
        fuente.setPointSize(19)
        fuente.setBold(True) 

        lbl_Titulo = QLabel("<font color='white'>Agregar Servicio</font>", frame)
        lbl_Titulo.setFont(fuente)
        lbl_Titulo.move(270, 25)

    def labels(self):
        """ Encabezado de la ventana """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        lbl_nombre_servicio = QLabel("Nombre del Servicio: ", self)
        lbl_nombre_servicio.setFont(fuente)
        lbl_nombre_servicio.move(60, 140)
        input_nombre_servicio = QLineEdit(self)
        input_nombre_servicio.move(225, 140)
        input_nombre_servicio.setFixedWidth(400)
        lbl_precio_servicio = QLabel("Precio: ", self)
        lbl_precio_servicio.setFont(fuente)
        lbl_precio_servicio.move(60, 180)
        input_precio_servicio = QLineEdit(self)
        input_precio_servicio.move(225, 180)
        input_precio_servicio.setFixedWidth(400)
         

    def botones(self):
        """ Botones que conforman la ventana de inventario """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        btn_guardar_servicio = QPushButton("Guardar", self)
        btn_guardar_servicio.setFixedWidth(135)
        btn_guardar_servicio.setFixedHeight(28)
        btn_guardar_servicio.move(215, 300)
        btn_guardar_servicio.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_guardar_servicio.setFont(fuente)
        btn_menu = QPushButton("Menu Principal", self)
        btn_menu.setFixedWidth(135)
        btn_menu.setFixedHeight(28)
        btn_menu.move(415, 300)
        btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_menu.setFont(fuente)

if __name__ == '__main__':
        
    aplicacion = QApplication(sys.argv)
    
    ventana = AgregarServicio()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
