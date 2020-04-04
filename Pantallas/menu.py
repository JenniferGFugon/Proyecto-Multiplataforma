
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image


class Menu(QWidget):
    """ Ventanas del sistema. """

    #-------------PANTALLA MENU--------------
    #inicializador de la clase menu
    def __init__(self):
        super().__init__()
        
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Menu")
        self.setGeometry(450, 150, 590, 285)
        self.UI()
       

    
    def UI(self):
        """ Cargar lo que es el diseño de la ventana """
        self.frame()
        self.buttons()
    

    def frame(self):
        """ Encabezado de la ventana """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(0, 0, 0))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(590)
        frame.setFixedHeight(74)
        frame.move(0, 0)

        logo = QLabel(frame)
        logo.setFixedWidth(90)
        logo.setFixedHeight(50)
        logo.setPixmap(QPixmap("Logo.png").scaled(90, 90, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        logo.move(250, 12)

   
    def buttons(self):

        """ Botones que conforman la ventana de menu"""
        btn_inventario = QPushButton("INVENTARIO", self)
        btn_inventario.setFixedWidth(115)
        btn_inventario.setFixedHeight(50)
        btn_inventario.move(40, 135)
        btn_inventario.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_inventario.clicked.connect(self.UI2)
        btn_inventario.show();
        

        btn_clientes = QPushButton("CLIENTES", self)
        btn_clientes.setFixedWidth(115)
        btn_clientes.setFixedHeight(50)
        btn_clientes.move(165, 135) 
        btn_clientes.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_clientes.clicked.connect(self.principalcliente)
        btn_clientes.show();                                 

        btn_ventas = QPushButton("VENTAS", self)
        btn_ventas.setFixedWidth(115)
        btn_ventas.setFixedHeight(50)
        btn_ventas.move(290, 135)
        btn_ventas.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_ventas.clicked.connect(self.principalVentas)
        btn_ventas.show();

        btn_empleados = QPushButton("EMPLEADOS", self)
        btn_empleados.setFixedWidth(115)
        btn_empleados.setFixedHeight(50)
        btn_empleados.move(415, 135)
        btn_empleados.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")

    #------------PANTALLA INVENTARIO---------------------
    def UI2(self):
        """ Componentes del diseño de la ventana Inventario """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        #self.setQPalette(paleta)
        app.setFont(fuente)  
        self.setWindowTitle("Inventario")
        self.setGeometry(430, 110, 700, 600)
        
        self.encabezado()
        self.botones()
        self.layouts()
        self.show()
       


    def encabezado(self):
        """ Encabezado de la ventana Inventario """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(0, 0, 0))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(2000)
        frame.setFixedHeight(74)
        frame.move(0, 0)

        logo = QLabel(frame)
        logo.setFixedWidth(90)
        logo.setFixedHeight(50)
        logo.setPixmap(QPixmap("Logo.png").scaled(90, 90, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        logo.move(560, 1)

        font = QFont()
        font.setPointSize(19)
        font.setBold(True) 

        lbl_titulo = QLabel("<font color='white'>Inventario</font>", frame)
        lbl_titulo.setFont(font)
        lbl_titulo.move(545, 40)

    def botones(self):
        """ Botones que conforman la ventana de inventario """
        self.lista_inventario = QListWidget()
        self.btn_modificar_inventario = QPushButton("Modificar Producto")
        self.btn_modificar_inventario.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_modificar_inventario.setFixedWidth(165)
        self.btn_modificar_inventario.setFixedHeight(40)

        self.btn_eliminar_inventario = QPushButton("Eliminar Producto")
        self.btn_eliminar_inventario.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar_inventario.setFixedWidth(165)
        self.btn_eliminar_inventario.setFixedHeight(40)

        self.btn_menu = QPushButton("Menu Principal")
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        
        self.btn_menu.setFixedWidth(165)
        self.btn_menu.setFixedHeight(40)

    def layouts(self):
        """ Layouts que componen la ventana Inventario """
        # Layouts
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()
        self.top_layout = QVBoxLayout()

        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 70)
        self.main_layout.addLayout(self.right_main_layout, 30)
        self.main_layout.addLayout(self.top_layout)
       
        self.left_layout.addWidget(self.lista_inventario)
        self.right_top_layout.addWidget(self.btn_modificar_inventario)
        self.right_main_layout.addWidget(self.btn_menu)
        self.right_bottom_layout.addWidget(self.btn_eliminar_inventario)
        self.top_layout.addWidget(self.encabezado())

        self.setLayout(self.main_layout)
        

    #-------------PANTALLA VENTA--------------

    def principalVentas(self):
        """ Componentes del diseño de la ventana ventas """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Ventas")
        self.setGeometry(430, 110, 700, 600)
        
        self.frameVentas()
        self.botonesVentas()
        self.layoutsVentas()

    def frameVentas(self):
        """ Encabezado de la ventana de ventas """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(0, 0, 0))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(1000)
        frame.setFixedHeight(74)
        frame.move(0, 0)

        logo = QLabel(frame)
        logo.setFixedWidth(90)
        logo.setFixedHeight(50)
        logo.setPixmap(QPixmap("Logo.png").scaled(90, 90, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        logo.move(565, 1)

        font = QFont()
        font.setPointSize(19)
        font.setBold(True) 

        lbl_titulo = QLabel("<font color='white'>Ventas</font>", frame)
        lbl_titulo.setFont(font)
        lbl_titulo.move(570, 40)


    def botonesVentas(self):
        """ Botones que conforman la ventana de venta """
        self.lista_ventas = QListWidget()
        self.btn_nueva_venta = QPushButton("Nueva Venta")
        self.btn_nueva_venta.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_nueva_venta.setFixedWidth(165)
        self.btn_nueva_venta.setFixedHeight(40)

        self.btn_eliminar_venta = QPushButton("Eliminar Venta")
        self.btn_eliminar_venta.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar_venta.setFixedWidth(165)
        self.btn_eliminar_venta.setFixedHeight(40)

        self.btn_menu = QPushButton("Menu Principal")
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        
        self.btn_menu.setFixedWidth(165)
        self.btn_menu.setFixedHeight(40)


    def layoutsVentas(self):
        """ Layouts que componen la ventana de Venta. """
        # Layouts
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()
        self.top_layout = QVBoxLayout()

        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 70)
        self.main_layout.addLayout(self.right_main_layout, 30)
        self.main_layout.addLayout(self.top_layout)

        self.left_layout.addWidget(self.lista_ventas)
        self.right_top_layout.addWidget(self.btn_nueva_venta)
        self.right_main_layout.addWidget(self.btn_menu)
        self.right_bottom_layout.addWidget(self.btn_eliminar_venta)
        self.top_layout.addWidget(self.frame())

        self.setLayout(self.main_layout)
        
   

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Empleados")
        self.setGeometry(430, 110, 700, 600)
        self.UI()

#------PANTALLA CLIENTE ------------

       

    def principalcliente(self):
        """ Componentes del diseño de la ventana """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Clientes")
        self.setGeometry(430, 110, 700, 600)
    
        self.encabezadoCliente()
        self.botonesCliente()
        self.layoutsCliente()

    def encabezadoCliente(self):
        """ Encabezado de la ventana """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(0, 0, 0))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(2000)
        frame.setFixedHeight(74)
        frame.move(0, 0)

        logo = QLabel(frame)
        logo.setFixedWidth(90)
        logo.setFixedHeight(50)
        logo.setPixmap(QPixmap("Logo.png").scaled(90, 90, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        logo.move(555, 1)

        font = QFont()
        font.setPointSize(19)
        font.setBold(True) 

        lbl_titulo = QLabel("<font color='white'>Clientes</font>", frame)
        lbl_titulo.setFont(font)
        lbl_titulo.move(550, 40)

    def botonesCliente(self):
        """ Botones que conforman la ventana de clientes """
        self.lista_clientes = QListWidget()
        self.btn_editar_cliente = QPushButton("Editar Cliente")
        self.btn_editar_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_editar_cliente.setFixedWidth(165)
        self.btn_editar_cliente.setFixedHeight(40)

        self.btn_eliminar_cliente = QPushButton("Eliminar Cliente")
        self.btn_eliminar_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar_cliente.setFixedWidth(165)
        self.btn_eliminar_cliente.setFixedHeight(40)

        self.btn_menu_cliente = QPushButton("Menu Principal")
        self.btn_menu_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu_cliente.setFixedWidth(165)
        self.btn_menu_cliente.setFixedHeight(40)
        self.btn_menu_cliente.clicked.connect(self.llamar_menu)

    def layoutsCliente(self):
        """ Layouts que componen la ventana """
        
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()
        self.top_layout = QVBoxLayout()

        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 70)
        self.main_layout.addLayout(self.right_main_layout, 30)
        self.main_layout.addLayout(self.top_layout)
        
        self.left_layout.addWidget(self.lista_clientes)
        self.right_top_layout.addWidget(self.btn_editar_cliente)
        self.right_main_layout.addWidget(self.btn_menu_cliente)
        self.right_bottom_layout.addWidget(self.btn_eliminar_cliente)
        self.top_layout.addWidget(self.encabezado())

        self.setLayout(self.main_layout)
        
    def llamar_menu(self):
        self.call = self.Menu()
        self.close()

    #----------------Funcion -----------------
        


#-----Base de datos ------------
#-------Ventas-------------

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    fuente.setBold(True)
    app.setFont(fuente)

    window = Menu()
    window.show()
    sys.exit(app.exec_())
           
           
    