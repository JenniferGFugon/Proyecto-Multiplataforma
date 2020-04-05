
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image
import base_de_datos
from base_de_datos import VentaDB

class Menu(QWidget):
    """ Ventanas del sistema. """
    
    #-------------PANTALLA MENU--------------
    #inicializador de la clase menu
    def __init__(self):
        super().__init__()
        self.baseDatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Menu")
        self.setGeometry(450, 150, 590, 285)
        self.UI()
        self.show()
       

    
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
        btn_inventario.clicked.connect(self.Inventario)
        btn_inventario.show()
        

        btn_clientes = QPushButton("CLIENTES", self)
        btn_clientes.setFixedWidth(115)
        btn_clientes.setFixedHeight(50)
        btn_clientes.move(165, 135) 
        btn_clientes.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_clientes.clicked.connect(self.Cliente)
        btn_clientes.show();                                 

        btn_ventas = QPushButton("VENTAS", self)
        btn_ventas.setFixedWidth(115)
        btn_ventas.setFixedHeight(50)
        btn_ventas.move(290, 135)
        btn_ventas.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_ventas.clicked.connect(self.Ventas)
        btn_ventas.show();

        btn_empleados = QPushButton("EMPLEADOS", self)
        btn_empleados.setFixedWidth(115)
        btn_empleados.setFixedHeight(50)
        btn_empleados.move(415, 135)
        btn_empleados.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")

        btn_empleados.clicked.connect(self.Empleado)
        btn_empleados.show()



    def Empleado(self):
        """ Inicia el formulario de ingreso de datos del empleado """
        self.empleado =  empleados()
        self.close()     


    def Inventario(self):
        """ Inicia el formulario de ingreso de datos del Inventario """
        self.inventario = VentanaInventario()
        self.close() 

    def Ventas(self):
        """ Inicia el formulario de ingreso de datos del Inventario """
        self.ventas = VentanaVentas()
        self.close() 

    def Cliente(self):
        """ Inicia el formulario de ingreso de datos del Inventario """
        self.cliente = VentanaCliente()
        self.close()          



    #------------PANTALLA INVENTARIO---------------------
class VentanaInventario(QWidget):
    """ Ventana de listado de inventario del sistema """
    def __init__(self):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        #self.setQPalette(paleta)
        app.setFont(fuente)  
        self.setWindowTitle("Inventario")
        self.setGeometry(430, 110, 700, 600)
        self.principalInventario()
        self.show()


    def principalInventario(self):
        """ Componentes del diseño de la ventana Inventario """
        self.encabezadoInventario()
        self.botonesInventario()
        self.layoutsInventario()
        self.show()
       


    def encabezadoInventario(self):
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


    def botonesInventario(self):
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
        self.btn_menu.clicked.connect(self.llamar_menu)                                 
        
        self.btn_menu.setFixedWidth(165)
        self.btn_menu.setFixedHeight(40)


    def layoutsInventario(self):
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
        self.top_layout.addWidget(self.encabezadoInventario())
        self.setLayout(self.main_layout)


    def llamar_menu(self):
        self.call = Menu()
        self.close()    
        

    #-------------PANTALLA VENTA--------------
class VentanaVentas(QWidget):
    """ Ventana de listado de ventas del sistema """
    def __init__(self):
        super().__init__()
        
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Ventas")
        self.setGeometry(430, 110, 700, 600)
        self.principalVentas()    
        self.show()


    def principalVentas(self):
        """ Componentes del diseño de la ventana ventas """
        self.encabezadoVentas()
        self.botonesVentas()
        self.layoutsVentas()

    def encabezadoVentas(self):
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
        self.btn_nueva_venta.clicked.connect(self.nuevaVenta)

        self.btn_eliminar_venta = QPushButton("Eliminar Venta")
        self.btn_eliminar_venta.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar_venta.setFixedWidth(165)
        self.btn_eliminar_venta.setFixedHeight(40)

        self.btn_menu = QPushButton("Menu Principal")
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.clicked.connect(self.llamar_menu)                                 
        
        self.btn_menu.setFixedWidth(165)
        self.btn_menu.setFixedHeight(40)


    #funcion para  instanciar una variable de tipo AgregarVenta
    def nuevaVenta(self):
        self.NuevaVenta = AgregarVenta() 


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
        self.top_layout.addWidget(self.encabezadoVentas())
        self.setLayout(self.main_layout)


    def llamar_menu(self):
        self.call = Menu()
        self.close()    
   

       

#------PANTALLA CLIENTE ------------
class VentanaCliente(QWidget):
    """ Ventana de listado de clientes """
    def __init__(self):
        super().__init__()

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Clientes")
        self.setGeometry(430, 110, 700, 600)
        self.principalCliente()
        self.show()


    def principalCliente(self):
        """ Componentes del diseño de la ventana """    
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
        self.top_layout.addWidget(self.encabezadoCliente())
        self.setLayout(self.main_layout)

    def llamar_menu(self):
        self.call = Menu()
        self.close()    


    #-----------PANTALLA EMPLEADOS-------------------
        
        
class empleados(QWidget):
    def __init__(self):
        super().__init__()
        
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Empleados")
        self.setGeometry(430, 110, 700, 600)
        self.principalEmpleado()
        self.show()


    def principalEmpleado(self):
        """ Componentes del diseño de la ventana """
        self.encabezadoEmpleado()
        self.botonesEmpleado()
        self.layoutsEmpleado()

    def encabezadoEmpleado(self):
        """ Encabezado de la ventana """
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(0, 0, 0))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(1400)
        frame.setFixedHeight(74)
        frame.move(0, 0)

        logo = QLabel(frame)
        logo.setFixedWidth(90)
        logo.setFixedHeight(50)
        logo.setPixmap(QPixmap("Logo.png").scaled(90, 90, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        logo.move(570, 1)

        font = QFont()
        font.setPointSize(19)
        font.setBold(True) 

        lbl_titulo = QLabel("<font color='white'>Empleados</font>", frame)
        lbl_titulo.setFont(font)
        lbl_titulo.move(545, 40)


    def botonesEmpleado(self):
        """ Botones que conforman la ventana de empleados """
        self.lista_empleados = QListWidget()
        self.btn_editar_empleado = QPushButton("Gestionar Empleado")
        self.btn_editar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_editar_empleado.setFixedWidth(165)
        self.btn_editar_empleado.setFixedHeight(40)
        self.btn_editar_empleado.clicked.connect(self.GestionarEmpleado)

        self.btn_eliminar_empleado = QPushButton("Eliminar Empleado")
        self.btn_eliminar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar_empleado.setFixedWidth(165)
        self.btn_eliminar_empleado.setFixedHeight(40)

        self.btn_menu = QPushButton("Menu Principal")
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.clicked.connect(self.llamar_menu)
        self.btn_menu.setFixedWidth(165)
        self.btn_menu.setFixedHeight(40)

    def GestionarEmpleado(self):
        self.gestionarEmpleado = AgregarEmpleado()


    def layoutsEmpleado(self):
        """ Layouts que componen la aplicación. """
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
        
        self.left_layout.addWidget(self.lista_empleados)
        self.right_top_layout.addWidget(self.btn_editar_empleado)
        self.right_main_layout.addWidget(self.btn_menu)
        self.right_bottom_layout.addWidget(self.btn_eliminar_empleado)
        self.top_layout.addWidget(self.encabezadoEmpleado())
        self.setLayout(self.main_layout) 

   
    def llamar_menu(self):
        self.call = Menu()
        self.close()



 #---------------PANTALLA AGREGAR  VENTA----------------------

class AgregarVenta(QWidget):
    """ Ventana para agregar una venta """

    def __init__(self):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar una venta")
        self.setGeometry(430, 120, 750, 690)
        self.principalAgregarVenta()
        self.show()

    def principalAgregarVenta(self):
        """ Componentes del diseño de la ventana """
        self.encabezadoAgregarVenta()
        self.labelsAgregarVenta()
        self.botonesAgregarVenta()

    def encabezadoAgregarVenta(self):
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
        lbl_Titulo.setFont(self.fuenteTitulo)
        lbl_Titulo.move(270, 25)

    def labelsAgregarVenta(self):
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


    def botonesAgregarVenta(self):
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
        self.btn_menu.clicked.connect(self.llamar_menu)
        self.btn_menu.setFont(self.fuente)
        
        
    def llamar_menu(self):
        self.call = Menu()
        self.close()    


    #----------------Funcion -----------------
        
class AgregarEmpleado(QWidget):
    """ Ventana para agregar nuevos empleados """

    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar un Empleado")
        self.setGeometry(400, 120, 650, 600)
        self.principalAgregarEmpleado()
        self.show()

    
    def principalAgregarEmpleado(self):
        """ Componentes del diseño de la ventana """
        self.encabezadoAgregarEmpleado()
        self.labelsAgregarEmpleado()
        self.botonesAgregarEmpleado()

    def encabezadoAgregarEmpleado(self):
        """ Encabezado de la ventana """
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

        self.lbl_Titulo = QLabel("<font color='white'>Agregar Empleado</font>", self.frame)
        self.lbl_Titulo.setFont(self.fuenteTitulo)
        self.lbl_Titulo.move(270, 25)


    def labelsAgregarEmpleado(self):
        """ Labels que conforman la ventana de agregar empleado """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.lbl_nombre_empleado = QLabel("Nombre: ", self)
        self.lbl_nombre_empleado.setFont(fuente)
        self.lbl_nombre_empleado.move(50, 130)
        self.input_nombre_empleado = QLineEdit(self)
        self.input_nombre_empleado.move(240, 130)
        self.input_nombre_empleado.setFixedWidth(360)
        self.lbl_id_empleado = QLabel("Identidad: ", self)
        self.lbl_id_empleado.setFont(fuente)
        self.lbl_id_empleado.move(50, 170)
        self.input_id_empleado = QLineEdit(self)
        self.input_id_empleado.move(240, 170)
        self.input_id_empleado.setFixedWidth(360) 

        self.lbl_telefono_empleado = QLabel("Telefono: ", self)
        self.lbl_telefono_empleado.setFont(fuente)
        self.lbl_telefono_empleado.move(50, 210)
        self.input_telefono_empleado = QLineEdit(self)
        self.input_telefono_empleado.move(240, 210)
        self.input_telefono_empleado.setFixedWidth(360) 
        self.lbl_direccion_empleado = QLabel("Direccion: ", self)
        self.lbl_direccion_empleado.setFont(fuente)
        self.lbl_direccion_empleado.move(50, 250)
        self.input_direccion_empleado = QLineEdit(self)
        self.input_direccion_empleado.move(240, 250)
        self.input_direccion_empleado.setFixedWidth(360)
        self.lbl_correo_empleado = QLabel("Correo Electronico: ", self)
        self.lbl_correo_empleado.setFont(fuente)
        self.lbl_correo_empleado.move(50, 290)
        self.input_correo_empleado = QLineEdit(self)
        self.input_correo_empleado.move(240, 290)
        self.input_correo_empleado.setFixedWidth(360)
        self.lbl_user_empleado = QLabel("Usuario: ", self)
        self.lbl_user_empleado.setFont(fuente)
        self.lbl_user_empleado.move(50, 330)
        self.input_user_empleado = QLineEdit(self)
        self.input_user_empleado.move(240, 330)
        self.input_user_empleado.setFixedWidth(360)
        self.lbl_contrasenia_empleado = QLabel("Contraseña: ", self)
        self.lbl_contrasenia_empleado.setFont(fuente)
        self.lbl_contrasenia_empleado.move(50, 370)
        self.input_contrasenia_empleado = QLineEdit(self)
        self.input_contrasenia_empleado.move(240, 370)
        self.input_contrasenia_empleado.setFixedWidth(360)


    def botonesAgregarEmpleado(self):
        """ Botones que conforman la ventana de agregar empleado """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.btn_guardar_empleado = QPushButton("Guardar", self)
        self.btn_guardar_empleado.setFixedWidth(135)
        self.btn_guardar_empleado.setFixedHeight(28)
        self.btn_guardar_empleado.move(165, 510)
        self.btn_guardar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_guardar_empleado.setFont(self.fuente)
        self.btn_guardar_empleado.clicked.connect(self.insertarEmpleado)
        self.btn_menu = QPushButton("Menu Principal", self)
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(365, 510)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.setFont(fuente)


    def insertarEmpleado(self):
        """ Insertar los valores del formulario a la tabla de empleado """
        # Verificar si los valores requeridos fueron agregados
        if (self.input_nombre_empleado.text () or self.input_id_empleado.text() or
                self.input_telefono_empleado.text() or self.input_direccion_empleado.text() or
                self.input_correo_empleado.text() or self.input_user_empleado.text() or
                self.input_contrasenia_empleado.text() != ""):
            empleado = (str(self.input_nombre_empleado.text()), str(self.input_id_empleado.text()),
                        str(self.input_telefono_empleado.text()) , str(self.input_direccion_empleado.text()),
                        str(self.input_correo_empleado.text()) ,  str(self.input_user_empleado.text()),
                        str(self.input_contrasenia_empleado.text()) )

            try:
                self.basedatos.add_empleado(empleado)
                QMessageBox.information(
                    self, "Guardar", "Empleado agregado correctamente")
                    
                self.close()
                #self.main = Main()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar el empleado")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")    

    

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
           
           
    