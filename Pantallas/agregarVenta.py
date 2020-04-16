
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
        self.setGeometry(430, 120, 650, 690)
        self.UI()
        self.show()

    def UI(self):
        """ Componentes del diseño de la ventana """
        self.encabezado()
        self.labels()
        self.botones()
        self.layouts()

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

        self.lbl_Titulo = QLabel("<font color='white'>Nueva Venta</font>", self.frame)
        self.lbl_Titulo.setFont(self.fuenteTitulo)
        self.lbl_Titulo.move(270, 25)

    def labels(self):
        """ Labels que conforman la ventana de agregar venta """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.lbl_num_venta = QLabel("Venta N°: ", self)
        self.lbl_num_venta.setFont(self.fuente)
        self.lbl_num_venta.move(50, 100)
        self.input_num_venta = QLineEdit(self)
        self.input_num_venta.move(150, 100)
        self.input_num_venta.setFixedWidth(100)
        self.lbl_cliente = QLabel("Cliente: ", self)
        self.lbl_cliente.setFont(self.fuente)
        self.lbl_cliente.move(50, 150)
        self.input_cliente = QLineEdit(self)
        self.input_cliente.move(150, 150)
        self.input_cliente.setFixedWidth(200)
        self.lbl_id_empleado = QLabel("Id Empleado: ", self)
        self.lbl_id_empleado.setFont(self.fuente)
        self.lbl_id_empleado.move(50, 200)
        self.input_id_empleado = QLineEdit(self)
        self.input_id_empleado.move(150, 200)
        self.input_id_empleado.setFixedWidth(200)  
        self.lbl_id_producto = QLabel("Id Producto: ", self)
        self.lbl_id_producto.setFont(self.fuente)
        self.lbl_id_producto.move(50, 250)
        self.input_id_producto = QLineEdit(self)
        self.input_id_producto.move(150, 250)
        self.input_id_producto.setFixedWidth(200)
        self.lbl_cantidad_venta = QLabel("Cantidad: ", self)
        self.lbl_cantidad_venta.setFont(self.fuente)
        self.lbl_cantidad_venta.move(50, 300)
        self.input_cantidad_venta = QLineEdit(self)
        self.input_cantidad_venta.move(150, 300)
        self.input_cantidad_venta.setFixedWidth(100)
        

    def botones(self):
        """ Botones que conforman la ventana de agregar venta """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)
        self.lista_detalle = QListWidget()
        self.btn_Buscar = QPushButton("Buscar", self)
        self.btn_Buscar.setFixedWidth(135)
        self.btn_Buscar.setFixedHeight(28)
        self.btn_Buscar.move(390, 254)
        self.btn_Buscar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_Buscar.setFont(fuente)
        self.btn_Agregar = QPushButton("Agregar", self)
        self.btn_Agregar.setFixedWidth(135)
        self.btn_Agregar.setFixedHeight(28)
        self.btn_Agregar.move(390, 300)
        self.btn_Agregar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_Agregar.setFont(fuente)

        self.btn_guardar = QPushButton("Guardar Venta", self)
        self.btn_guardar.setFixedWidth(135)
        self.btn_guardar.setFixedHeight(28)
        self.btn_guardar.move(390, 400)
        self.btn_guardar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_guardar.setFont(fuente)

        
    def layouts(self):
    
        self.main_layout = QVBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.middle_main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.left_layout, 50)
        self.main_layout.addLayout(self.right_main_layout, 40)
        self.main_layout.addLayout(self.middle_main_layout, 10)
        self.right_main_layout.addWidget(self.lista_detalle)
        self.middle_main_layout.addWidget(self.btn_guardar)

        #self.top_layout.addWidget(self.encabezadoEmpleado())
        self.setLayout(self.main_layout) 
      
        

            


if __name__ == '__main__':
        
  aplicacion = QApplication(sys.argv)
    
  ventana = AgregarVenta()
  ventana.show()
    
  sys.exit(aplicacion.exec_())