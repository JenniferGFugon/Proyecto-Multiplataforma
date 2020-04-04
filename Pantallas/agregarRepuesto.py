from menu import Menu
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image

class AgregarRepuesto(QWidget):
    """ preciolbl_precio_compra_repuestona para agregar un nuevo repuesto """

    def __init__(self):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar un repuesto")
        self.setGeometry(430, 120, 750, 620)
        self.UI()

    def UI(self):
        """ Componentes del diseño de la preciolbl_precio_compra_repuestona """
        self.encabezado()
        self.widgets()
        self.botones()

    def encabezado(self):
        """ Encabezado de la preciolbl_precio_compra_repuestona """
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

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(19)
        fuenteTitulo.setBold(True) 

        lbl_Titulo = QLabel("<font color='white'>Agregar Repuesto</font>", frame)
        lbl_Titulo.setFont(fuenteTitulo)
        lbl_Titulo.move(270, 25)


    def widgets(self):
        """ Widgets que conforman la preciolbl_precio_compra_repuestona de agregar un repuesto """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Arial")
        fuente.setBold(True)

        lbl_nombre_repuesto = QLabel("Nombre del Repuesto: ", self)
        lbl_nombre_repuesto.setFont(fuente)
        lbl_nombre_repuesto.move(60, 140)
        input_nombre_repuesto = QLineEdit(self)
        input_nombre_repuesto.move(225, 140)
        input_nombre_repuesto.setFixedWidth(400)
        lbl_marca_repuesto = QLabel("Marca: ", self)
        lbl_marca_repuesto.setFont(fuente)
        lbl_marca_repuesto.move(60, 180)
        input_marca_repuesto = QLineEdit(self)
        input_marca_repuesto.move(225, 180)
        input_marca_repuesto.setFixedWidth(400)
        lbl_modelo_repuesto = QLabel("Modelo: ", self)
        lbl_modelo_repuesto.setFont(fuente)
        lbl_modelo_repuesto.move(60, 220)
        input_modelo_repuesto = QLineEdit(self)
        input_modelo_repuesto.move(225, 220)
        input_modelo_repuesto.setFixedWidth(400)  
        lbl_fabricante_repuesto = QLabel("Fabricante: ", self)
        lbl_fabricante_repuesto.setFont(fuente)
        lbl_fabricante_repuesto.move(60, 260)
        input_fabricante_repuesto = QLineEdit(self)
        input_fabricante_repuesto.move(225, 260)
        input_fabricante_repuesto.setFixedWidth(400)
        lbl_existencia_repuesto = QLabel("Existencia: ", self)
        lbl_existencia_repuesto.setFont(fuente)
        lbl_existencia_repuesto.move(60, 300)
        input_existencia_repuesto = QLineEdit(self)
        input_existencia_repuesto.move(225, 300)
        input_existencia_repuesto.setFixedWidth(400)
        lbl_precio_compra_repuesto = QLabel("Precio de compra: ", self)
        lbl_precio_compra_repuesto.setFont(fuente)
        lbl_precio_compra_repuesto.move(60, 340)
        input_precio_compra_repuesto = QLineEdit(self)
        input_precio_compra_repuesto.move(225, 340)
        input_precio_compra_repuesto.setFixedWidth(400)
        lbl_precio_venta_repuesto = QLabel("Precio de venta: ", self)
        lbl_precio_venta_repuesto.setFont(fuente)
        lbl_precio_venta_repuesto.move(60, 380)
        input_precio_venta_repuesto = QLineEdit(self)
        input_precio_venta_repuesto.move(225, 380)
        input_precio_venta_repuesto.setFixedWidth(400)

    def botones(self):
        """ Botones que conforman la preciolbl_precio_compra_repuestona de agregar un repuesto """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        btn_guardar_repuesto = QPushButton("Guardar", self)
        btn_guardar_repuesto.setFixedWidth(135)
        btn_guardar_repuesto.setFixedHeight(28)
        btn_guardar_repuesto.move(215, 476)
        btn_guardar_repuesto.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_guardar_repuesto.setFont(fuente)
        btn_menu = QPushButton("Menu Principal", self)
        btn_menu.setFixedWidth(135)
        btn_menu.setFixedHeight(28)
        btn_menu.move(415, 476)
        btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_menu.setFont(fuente)

if __name__ == '__main__':
        
    aplicacion = QApplication(sys.argv)

    window = AgregarRepuesto()
    window.show()
    
    sys.exit(aplicacion.exec_())
