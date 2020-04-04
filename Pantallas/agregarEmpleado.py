from menu import Menu
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image

class AgregarEmpleado(QWidget):
    """ Ventana para agregar nuevos empleados """

    def __init__(self):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar un Empleado")
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

        lbl_Titulo = QLabel("<font color='white'>Agregar Empleado</font>", frame)
        lbl_Titulo.setFont(fuenteTitulo)
        lbl_Titulo.move(270, 25)


    def labels(self):
        """ Labels que conforman la ventana de agregar empleado """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        lbl_nombre_empleado = QLabel("Nombre del Empleado: ", self)
        lbl_nombre_empleado.setFont(fuente)
        lbl_nombre_empleado.move(60, 130)
        input_nombre_empleado = QLineEdit(self)
        input_nombre_empleado.move(250, 130)
        input_nombre_empleado.setFixedWidth(400)
        lbl_telefono_empleado = QLabel("Telefono: ", self)
        lbl_telefono_empleado.setFont(fuente)
        lbl_telefono_empleado.move(60, 170)
        input_telefono_empleado = QLineEdit(self)
        input_telefono_empleado.move(250, 170)
        input_telefono_empleado.setFixedWidth(400)
        lbl_celular_empleado = QLabel("Celular: ", self)
        lbl_celular_empleado.setFont(fuente)
        lbl_celular_empleado.move(60, 210)
        input_celular_empleado = QLineEdit(self)
        input_celular_empleado.move(250, 210)
        input_celular_empleado.setFixedWidth(400)  
        lbl_rtn_empleado = QLabel("RTN: ", self)
        lbl_rtn_empleado.setFont(fuente)
        lbl_rtn_empleado.move(60, 250)
        input_rtn_empleado = QLineEdit(self)
        input_rtn_empleado.move(250, 250)
        input_rtn_empleado.setFixedWidth(400)
        lbl_direccion_empleado = QLabel("Direccion: ", self)
        lbl_direccion_empleado.setFont(fuente)
        lbl_direccion_empleado.move(60, 290)
        input_direccion_empleado = QLineEdit(self)
        input_direccion_empleado.move(250, 290)
        input_direccion_empleado.setFixedWidth(400)
        lbl_correo_empleado = QLabel("Correo Electronico: ", self)
        lbl_correo_empleado.setFont(fuente)
        lbl_correo_empleado.move(60, 330)
        input_correo_empleado = QLineEdit(self)
        input_correo_empleado.move(250, 330)
        input_correo_empleado.setFixedWidth(400)
        lbl_user_empleado = QLabel("Usuario de Empleado: ", self)
        lbl_user_empleado.setFont(fuente)
        lbl_user_empleado.move(60, 370)
        input_user_empleado = QLineEdit(self)
        input_user_empleado.move(250, 370)
        input_user_empleado.setFixedWidth(400)
        lbl_contrasenia_empleado = QLabel("Contraseña de Empleado: ", self)
        lbl_contrasenia_empleado.setFont(fuente)
        lbl_contrasenia_empleado.move(60, 410)
        input_contrasenia_empleado = QLineEdit(self)
        input_contrasenia_empleado.move(250, 410)
        input_contrasenia_empleado.setFixedWidth(400)

    def botones(self):
        """ Botones que conforman la ventana de agregar empleado """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        btn_guardar_empleado = QPushButton("Guardar", self)
        btn_guardar_empleado.setFixedWidth(135)
        btn_guardar_empleado.setFixedHeight(28)
        btn_guardar_empleado.move(215, 510)
        btn_guardar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_guardar_empleado.setFont(fuente)
        btn_menu = QPushButton("Menu Principal", self)
        btn_menu.setFixedWidth(135)
        btn_menu.setFixedHeight(28)
        btn_menu.move(415, 510)
        btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_menu.setFont(fuente)


if __name__ == '__main__':
        
  aplicacion = QApplication(sys.argv)

  ventana = AgregarEmpleado()
  ventana.show()
    
  sys.exit(aplicacion.exec_())