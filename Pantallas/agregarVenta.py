
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image

class AgregarVenta(QWidget):
    """ Ventana para agregar una venta """

    def __init__(self):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar una venta")
        self.setGeometry(430, 120, 750, 690)
        self.UI()
        self.show()

    def UI(self):
        """ Componentes del diseño de la ventana """
        self.encabezado()
        self.labels()
        self.botones()

    def encabezado(self):
        """ Encabezado de la ventana agregar venta """
        self.paleta = QPalette()
        self.paleta.setColor(QPalette.Background, QColor(0, 0, 0))

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setAutoFillBackground(True)
        self.frame.setPalette(self.paleta)
        self.frame.setFixedWidth(2000)
        self.frame.setFixedHeight(84)
        self.frame.move(0, 0)

        self.logo = QLabel(self.frame)
        self.logo.setFixedWidth(90)
        self.logo.setFixedHeight(50)
        self.logo.setPixmap(QPixmap("Logo.png").scaled(90, 90, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        self.logo.move(20, 12)

        self.fuenteTitulo = QFont()
        self.fuenteTitulo.setPointSize(19)
        self.fuenteTitulo.setBold(True) 

        self.lbl_Titulo = QLabel("<font color='white'>Nueva Venta</font>", frame)
        self.lbl_Titulo.setFont(self.fuenteTitulo)
        self.lbl_Titulo.move(270, 25)

    def labels(self):
        """ Labels que conforman la ventana de agregar venta """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.lbl_id_venta = QLabel("Id Venta: ", self)
        self.lbl_id_venta.setFont(self.fuente)
        self.lbl_id_venta.move(155, 140)
        self.input_id_venta = QLineEdit(self)
        self.input_id_venta.move(320, 140)
        self.input_id_venta.setFixedWidth(200)
        self.lbl_id_cliente = QLabel("Id Cliente: ", self)
        self.lbl_id_cliente.setFont(self.fuente)
        self.lbl_id_cliente.move(155, 180)
        self.input_id_cliente = QLineEdit(self)
        self.input_id_cliente.move(320, 180)
        self.input_id_cliente.setFixedWidth(200)
        self.lbl_id_empleado = QLabel("Id Empleado: ", self)
        self.lbl_id_empleado.setFont(self.fuente)
        self.lbl_id_empleado.move(155, 220)
        self.input_id_empleado = QLineEdit(self)
        self.input_id_empleado.move(320, 220)
        self.input_id_empleado.setFixedWidth(200)  
        self.lbl_id_producto = QLabel("Id Producto: ", self)
        self.lbl_id_producto.setFont(self.fuente)
        self.lbl_id_producto.move(155, 260)
        self.input_id_producto = QLineEdit(self)
        self.input_id_producto.move(320, 260)
        self.input_id_producto.setFixedWidth(200)
        self.lbl_cantidad_venta = QLabel("Cantidad: ", self)
        self.lbl_cantidad_venta.setFont(self.fuente)
        self.lbl_cantidad_venta.move(155, 300)
        self.input_cantidad_venta = QLineEdit(self)
        self.input_cantidad_venta.move(320, 300)
        self.input_cantidad_venta.setFixedWidth(200)
        self.lbl_precio_venta = QLabel("Precio de Venta: ", self)
        self.lbl_precio_venta.setFont(self.fuente)
        self.lbl_precio_venta.move(155, 340)
        self.input_precio_venta = QLineEdit(self)
        self.input_precio_venta.move(320, 340)
        self.input_precio_venta.setFixedWidth(200)
        self.lbl_isv_venta = QLabel("ISV: ", self)
        self.lbl_isv_venta.setFont(self.fuente)
        self.lbl_isv_venta.move(155, 380)
        self.input_isv_venta = QLineEdit(self)
        self.input_isv_venta.move(320, 380)
        self.input_isv_venta.setFixedWidth(200)
        self.lbl_descuento_venta = QLabel("Descuento: ", self)
        self.lbl_descuento_venta.setFont(self.fuente)
        self.lbl_descuento_venta.move(155, 420)
        self.input_descuento_venta = QLineEdit(self)
        self.input_descuento_venta.move(320, 420)
        self.input_descuento_venta.setFixedWidth(200)
        self.lbl_total_venta = QLabel("Total: ", self)
        self.lbl_total_venta.setFont(self.fuente)
        self.lbl_total_venta.move(400, 480)
        self.input_total_venta = QLineEdit(self)
        self.input_total_venta.move(470, 480)
        self.input_total_venta.setFixedWidth(90)

    def botones(self):
        """ Botones que conforman la ventana de agregar venta """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.btn_guardar_venta = QPushButton("Guardar")
        self.btn_guardar_venta.setFixedWidth(135)
        self.btn_guardar_venta.setFixedHeight(28)
        self.btn_guardar_venta.move(215, 580)
        self.btn_guardar_venta.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
                                         
        self.btn_guardar_venta.setFont(self.fuente)
        self.btn_menu = QPushButton("Menu Principal")
        
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(415, 580)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.clicked.connection(Menu)
        self.btn_menu.setFont(self.fuente)
        
        
        

            


if __name__ == '__main__':
        
  aplicacion = QApplication(sys.argv)
    
  ventana = AgregarVenta()
  ventana.show()
    
  sys.exit(aplicacion.exec_())