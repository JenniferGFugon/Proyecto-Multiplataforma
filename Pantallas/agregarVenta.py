from menu import Menu
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

    def UI(self):
        """ Componentes del diseño de la ventana """
        self.encabezado()
        self.labels()
        self.botones()

    def encabezado(self):
        """ Encabezado de la ventana agregar venta """
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

        lbl_Titulo = QLabel("<font color='white'>Nueva Venta</font>", frame)
        lbl_Titulo.setFont(fuenteTitulo)
        lbl_Titulo.move(270, 25)

    def labels(self):
        """ Labels que conforman la ventana de agregar venta """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        lbl_id_venta = QLabel("Id Venta: ", self)
        lbl_id_venta.setFont(fuente)
        lbl_id_venta.move(155, 140)
        input_id_venta = QLineEdit(self)
        input_id_venta.move(320, 140)
        input_id_venta.setFixedWidth(200)
        lbl_id_cliente = QLabel("Id Cliente: ", self)
        lbl_id_cliente.setFont(fuente)
        lbl_id_cliente.move(155, 180)
        input_id_cliente = QLineEdit(self)
        input_id_cliente.move(320, 180)
        input_id_cliente.setFixedWidth(200)
        lbl_id_empleado = QLabel("Id Empleado: ", self)
        lbl_id_empleado.setFont(fuente)
        lbl_id_empleado.move(155, 220)
        input_id_empleado = QLineEdit(self)
        input_id_empleado.move(320, 220)
        input_id_empleado.setFixedWidth(200)  
        lbl_id_producto = QLabel("Id Producto: ", self)
        lbl_id_producto.setFont(fuente)
        lbl_id_producto.move(155, 260)
        input_id_producto = QLineEdit(self)
        input_id_producto.move(320, 260)
        input_id_producto.setFixedWidth(200)
        lbl_cantidad_venta = QLabel("Cantidad: ", self)
        lbl_cantidad_venta.setFont(fuente)
        lbl_cantidad_venta.move(155, 300)
        input_cantidad_venta = QLineEdit(self)
        input_cantidad_venta.move(320, 300)
        input_cantidad_venta.setFixedWidth(200)
        lbl_precio_venta = QLabel("Precio de Venta: ", self)
        lbl_precio_venta.setFont(fuente)
        lbl_precio_venta.move(155, 340)
        input_precio_venta = QLineEdit(self)
        input_precio_venta.move(320, 340)
        input_precio_venta.setFixedWidth(200)
        lbl_isv_venta = QLabel("ISV: ", self)
        lbl_isv_venta.setFont(fuente)
        lbl_isv_venta.move(155, 380)
        input_isv_venta = QLineEdit(self)
        input_isv_venta.move(320, 380)
        input_isv_venta.setFixedWidth(200)
        lbl_descuento_venta = QLabel("Descuento: ", self)
        lbl_descuento_venta.setFont(fuente)
        lbl_descuento_venta.move(155, 420)
        input_descuento_venta = QLineEdit(self)
        input_descuento_venta.move(320, 420)
        input_descuento_venta.setFixedWidth(200)
        lbl_total_venta = QLabel("Total: ", self)
        lbl_total_venta.setFont(fuente)
        lbl_total_venta.move(400, 480)
        input_total_venta = QLineEdit(self)
        input_total_venta.move(470, 480)
        input_total_venta.setFixedWidth(90)

    def botones(self):
        """ Botones que conforman la ventana de agregar venta """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        btn_guardar_venta = QPushButton("Guardar", self)
        btn_guardar_venta.setFixedWidth(135)
        btn_guardar_venta.setFixedHeight(28)
        btn_guardar_venta.move(215, 580)
        btn_guardar_venta.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_guardar_venta.setFont(fuente)
        btn_menu = QPushButton("Menu Principal", self)
        btn_menu.setFixedWidth(135)
        btn_menu.setFixedHeight(28)
        btn_menu.move(415, 580)
        btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_menu.setFont(fuente)

if __name__ == '__main__':
        
  aplicacion = QApplication(sys.argv)
    
  ventana = AgregarVenta()
  ventana.show()
    
  sys.exit(aplicacion.exec_())