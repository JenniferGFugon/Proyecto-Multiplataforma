from menu import Menu
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image

class AgregarCliente(QWidget):
    """ Ventana para agregar nuevos clientes """

    def __init__(self):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar un cliente")
        self.setGeometry(430, 120, 750, 650)
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

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(19)
        fuenteTitulo.setBold(True) 

        lbl_Titulo = QLabel("<font color='white'>Agregar Cliente</font>", frame)
        lbl_Titulo.setFont(fuenteTitulo)
        lbl_Titulo.move(280, 25)

    def labels(self):
        """ Botones que conforman la ventana de agregar cliente """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        lbl_id_cliente = QLabel("Identidad: ", self)
        lbl_id_cliente.setFont(fuente)
        lbl_id_cliente.move(60, 140)
        input_id_cliente = QLineEdit(self)
        input_id_cliente.move(250, 140)
        input_id_cliente.setFixedWidth(400)
        lbl_nombre_cliente = QLabel("Nombre del cliente: ", self)
        lbl_nombre_cliente.setFont(fuente)
        lbl_nombre_cliente.move(60, 180)
        input_nombre_cliente = QLineEdit(self)
        input_nombre_cliente.move(250, 180)
        input_nombre_cliente.setFixedWidth(400)
        lbl_telefono_cliente = QLabel("Telefono: ", self)
        lbl_telefono_cliente.setFont(fuente)
        lbl_telefono_cliente.move(60, 220)
        input_telefono_cliente = QLineEdit(self)
        input_telefono_cliente.move(250, 220)
        input_telefono_cliente.setFixedWidth(400)
        lbl_celular_cliente = QLabel("Celular: ", self)
        lbl_celular_cliente.setFont(fuente)
        lbl_celular_cliente.move(60, 260)
        input_celular_cliente = QLineEdit(self)
        input_celular_cliente.move(250, 260)
        input_celular_cliente.setFixedWidth(400)  
        lbl_rtn_cliente = QLabel("RTN: ", self)
        lbl_rtn_cliente.setFont(fuente)
        lbl_rtn_cliente.move(60, 300)
        input_rtn_cliente = QLineEdit(self)
        input_rtn_cliente.move(250, 300)
        input_rtn_cliente.setFixedWidth(400)
        lbl_direccion_cliente = QLabel("Direccion: ", self)
        lbl_direccion_cliente.setFont(fuente)
        lbl_direccion_cliente.move(60, 340)
        input_direccion_cliente = QLineEdit(self)
        input_direccion_cliente.move(250, 340)
        input_direccion_cliente.setFixedWidth(400)
        lbl_correo_cliente = QLabel("Correo Electronico: ", self)
        lbl_correo_cliente.setFont(fuente)
        lbl_correo_cliente.move(60, 380)
        input_correo_cliente = QLineEdit(self)
        input_correo_cliente.move(250, 380)
        input_correo_cliente.setFixedWidth(400)

    def botones(self):
        """ Botones que conforman la ventana de agregar cliente """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        btn_guardar_cliente = QPushButton("Guardar", self)
        btn_guardar_cliente.setFixedWidth(135)
        btn_guardar_cliente.setFixedHeight(28)
        btn_guardar_cliente.move(215, 510)
        btn_guardar_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_guardar_cliente.setFont(fuente)
        btn_menu = QPushButton("Menu Principal", self)
        btn_menu.setFixedWidth(135)
        btn_menu.setFixedHeight(28)
        btn_menu.move(415, 510)
        btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_menu.setFont(fuente)

if __name__ == '__main__':
        
  aplicacion = QApplication(sys.argv)
    
  ventana = AgregarCliente()
  ventana.show()
    
  sys.exit(aplicacion.exec_())