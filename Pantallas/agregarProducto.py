from menu import Menu
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image

class AgregarProducto(QWidget):
    """ Ventana para agregar nuevos productos """

    def __init__(self):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar Producto")
        self.setGeometry(430, 120, 750, 550)
        self.UI()
        
    def UI(self):
        """ Componentes del diseño de la ventana """
        self.encabezado()
        self.widgets()
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

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(19)
        fuenteTitulo.setBold(True) 

        lbl_Titulo = QLabel("<font color='white'>Agregar Producto</font>", frame)
        lbl_Titulo.setFont(fuenteTitulo)
        lbl_Titulo.move(270, 25)

    def widgets(self):
        """ Widgets que conforman la ventana de agregar un producto """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)
        
        lbl_nombre_producto = QLabel("Nombre del Producto: ", self)
        lbl_nombre_producto.setFont(fuente)
        lbl_nombre_producto.move(60, 140)
        input_nombre_producto = QLineEdit(self)
        input_nombre_producto.move(225, 140)
        input_nombre_producto.setFixedWidth(400)
        lbl_marca_producto = QLabel("Marca: ", self)
        lbl_marca_producto.setFont(fuente)
        lbl_marca_producto.move(60, 180)
        input_marca_producto = QLineEdit(self)
        input_marca_producto.move(225, 180)
        input_marca_producto.setFixedWidth(400)
        lbl_existencia_producto = QLabel("Existencia: ", self)
        lbl_existencia_producto.setFont(fuente)
        lbl_existencia_producto.move(60, 220)
        input_existencia_producto = QLineEdit(self)
        input_existencia_producto.move(225, 220)
        input_existencia_producto.setFixedWidth(400)  
        lbl_precio_compra = QLabel("Precio de Compra: ", self)
        lbl_precio_compra.setFont(fuente)
        lbl_precio_compra.move(60, 260)
        input_precio_compra = QLineEdit(self)
        input_precio_compra.move(225, 260)
        input_precio_compra.setFixedWidth(400)
        lbl_precio_venta = QLabel("Precio de venta: ", self)
        lbl_precio_venta.setFont(fuente)
        lbl_precio_venta.move(60, 300)
        input_precio_venta = QLineEdit(self)
        input_precio_venta.move(225, 300)
        input_precio_venta.setFixedWidth(400)  

    def botones(self):
        """ Botones que conforman la ventana de agregar un producto """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        btn_guardar_producto = QPushButton("Guardar", self)
        btn_guardar_producto.setFixedWidth(135)
        btn_guardar_producto.setFixedHeight(28)
        btn_guardar_producto.move(215, 400)
        btn_guardar_producto.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_guardar_producto.setFont(fuente)
        btn_menu = QPushButton("Menu Principal", self)
        btn_menu.setFixedWidth(135)
        btn_menu.setFixedHeight(28)
        btn_menu.move(415, 400)
        btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_menu.setFont(fuente)
        

if __name__ == '__main__':

    aplicacion = QApplication(sys.argv)
    
    ventana = AgregarProducto()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
