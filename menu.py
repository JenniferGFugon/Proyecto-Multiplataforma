# -*- coding: utf8 -*-
# Programa: 
# Objetivo: 
# Autores: Jennifer Guerrero 
#          Dina Guerrero
#          Kattia Bodden
#          Carlos Molina
#          Diego Diaz
# Fecha: 17 de Abril de 2020

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

#variable global para modificacion de los empleados
id  
global idCliente
total = 0


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
        btn_inventario.clicked.connect(self.inventario)
        btn_inventario.show()
        

        btn_clientes = QPushButton("CLIENTES", self)
        btn_clientes.setFixedWidth(115)
        btn_clientes.setFixedHeight(50)
        btn_clientes.move(165, 135) 
        btn_clientes.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_clientes.clicked.connect(self.cliente)
        btn_clientes.show();                                 

        btn_ventas = QPushButton("VENTAS", self)
        btn_ventas.setFixedWidth(115)
        btn_ventas.setFixedHeight(50)
        btn_ventas.move(290, 135)
        btn_ventas.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_ventas.clicked.connect(self.ventas)
        btn_ventas.show();

        btn_empleados = QPushButton("EMPLEADOS", self)
        btn_empleados.setFixedWidth(115)
        btn_empleados.setFixedHeight(50)
        btn_empleados.move(415, 135)
        btn_empleados.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")

        btn_empleados.clicked.connect(self.empleado)
        btn_empleados.show()

    def empleado(self):
        """ Inicia el formulario de ingreso de datos del empleado """
        self.empleado =  empleados()
        self.close()     


    def inventario(self):
        """ Inicia el formulario de ingreso de datos del Inventario """
        self.inventario = VentanaInventario()
        self.close() 

    def ventas(self):
        """ Inicia el formulario de ingreso de datos del Inventario """
        self.ventas = VentanaVentas()
        self.close() 

    def cliente(self):
        """ Inicia el formulario de ingreso de datos del Inventario """
        self.cliente = VentanaCliente()
        self.close()          

    #------------PANTALLA INVENTARIO---------------------
class VentanaInventario(QWidget):
    """ Ventana de listado de inventario del sistema """
    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Ventas")
        self.setGeometry(430, 110, 700, 600)
        self.principal_inventario()    
        self.show()


    def principal_inventario(self):
        """ Componentes del diseño de la ventana Inventario """
        self.encabezado_inventario()
        self.botones_inventario()
        self.layouts_inventario()
        self.llenar_lista_Producto()
        self.show()
       


    def encabezado_inventario(self):
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


    def botones_inventario(self):
        """ Botones que conforman la ventana de inventario """
        self.lista_inventario = QListWidget()
        self.btn_agregar_inventario = QPushButton("Agregar Producto")
        self.btn_agregar_inventario.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_agregar_inventario.clicked.connect(self.Llamar_agregar)

        self.btn_agregar_inventario.setFixedWidth(165)
        self.btn_agregar_inventario.setFixedHeight(40)
        
        self.btn_modificar_inventario = QPushButton("Modificar Producto")
        self.btn_modificar_inventario.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_modificar_inventario.clicked.connect(self.cargarDatosAModificarProducto)                                 
        self.btn_modificar_inventario.setFixedWidth(165)
        self.btn_modificar_inventario.setFixedHeight(40)

        self.btn_eliminar_inventario = QPushButton("Eliminar Producto")
        self.btn_eliminar_inventario.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar_inventario.clicked.connect(self.eliminar_inventario)   

        self.btn_eliminar_inventario.setFixedWidth(165)
        self.btn_eliminar_inventario.setFixedHeight(40)

        self.btn_menu = QPushButton("Menu Principal")
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.clicked.connect(self.llamar_menu)                                 
        
        self.btn_menu.setFixedWidth(165)
        self.btn_menu.setFixedHeight(40)


    def layouts_inventario(self):
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
        self.right_top_layout.addWidget(self.btn_agregar_inventario)
        self.right_bottom_layout.addWidget(self.btn_modificar_inventario)
        self.right_main_layout.addWidget(self.btn_eliminar_inventario)
        self.btn_menu.move(415, 400)
        self.right_main_layout.addWidget(self.btn_menu)
        self.top_layout.addWidget(self.encabezado_inventario())
        self.setLayout(self.main_layout)
    

    def llenar_lista_Producto(self):
        """ Obtiene las tuplas de productos y las muestra en la lista """
        productos = self.basedatos.obtenerProducto()

        if productos:
            for producto in productos:
                self.lista_inventario.addItem(
                    "{0} -- {1} -- {2} -- {3} -- {4} -- {5}"
                    .format(producto[0], producto[1], producto[2], producto[3],
                     producto[4], producto[5]))


    def modificarProducto(self):
        self.modificaproducto = EditarProducto()
        self.close()


    def cargarDatosAModificarProducto(self):
        '''Carga los datos que seran modificados por el usuario'''
        global id
        if self.lista_inventario.selectedItems():
            producto = self.lista_inventario.currentItem().text()
            id =  producto.split(" -- ")[0]
            self.modificarProducto()
        else:
            QMessageBox.information(self,"Informacion","No selecciono ningun producto")  


    def eliminar_inventario(self):
        """ Eliminar el inventario segun el id del producto """
        if self.lista_inventario.selectedItems():
            inventario = self.lista_inventario.currentItem().text()
            id = inventario.split(" -- ")[0]

            inventario = self.basedatos.obtenerProductoPorId(id)

            yes = QMessageBox.Yes

            if inventario:
                question_text = f"¿Está seguro de eliminar el producto {inventario[0]}?"
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.basedatos.eliminar_Producto(inventario[0])
                    QMessageBox.information(self, "Información", "¡producto eliminado satisfactoriamente!")
                    self.lista_inventario.clear()
                    self.llenar_lista_Producto()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")
        
        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar un producto a eliminar")

    def Llamar_agregar(self):
        self.llamar_agregar = AgregarProducto()
        self.close()


    def Llamar_agregar(self):
        self.llamar_agregar = AgregarProducto()
        self.close()

    def llamar_menu(self):
        self.call = Menu()
        self.close()


#------------------------------Pantalla Agregar Inventario---------------------------------
class AgregarProducto(QWidget):
    """ Ventana para agregar nuevos productos """

    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar Producto")
        self.setGeometry(430, 120, 750, 550)
        self.UI()
        self.show()
        
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

        self.lbl_Titulo = QLabel("<font color='white'>Agregar Producto</font>", frame)
        self.lbl_Titulo.setFont(fuenteTitulo)
        self.lbl_Titulo.move(270, 25)

    def widgets(self):
        """ Widgets que conforman la ventana de agregar un producto """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)
        
        self.lbl_nombre_producto = QLabel("Nombre del Producto: ", self)
        self.lbl_nombre_producto.setFont(fuente)
        self.lbl_nombre_producto.move(60, 140)
        self.input_nombre_producto = QLineEdit(self)
        self.input_nombre_producto.move(225, 140)
        self.input_nombre_producto.setFixedWidth(400)
        self.lbl_categoria_producto = QLabel("Categoria: ", self)
        self.lbl_categoria_producto.setFont(fuente)
        self.lbl_categoria_producto.move(60, 180)
        self.input_categoria_producto = QLineEdit(self)
        self.input_categoria_producto.move(225, 180)
        self.input_categoria_producto.setFixedWidth(400)
        self.lbl_existencia_producto = QLabel("Existencia: ", self)
        self.lbl_existencia_producto.setFont(fuente)
        self.lbl_existencia_producto.move(60, 220)
        self.input_existencia_producto = QLineEdit(self)
        self.input_existencia_producto.move(225, 220)
        self.input_existencia_producto.setFixedWidth(400)  
        self.lbl_precio_compra = QLabel("Precio de Compra: ", self)
        self.lbl_precio_compra.setFont(fuente)
        self.lbl_precio_compra.move(60, 260)
        self.input_precio_compra = QLineEdit(self)
        self.input_precio_compra.move(225, 260)
        self.input_precio_compra.setFixedWidth(400)
        self.lbl_precio_venta = QLabel("Precio de venta: ", self)
        self.lbl_precio_venta.setFont(fuente)
        self.lbl_precio_venta.move(60, 300)
        self.input_precio_venta = QLineEdit(self)
        self.input_precio_venta.move(225, 300)
        self.input_precio_venta.setFixedWidth(400)  

    def botones(self):
        """ Botones que conforman la ventana de agregar un producto """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.btn_guardar_producto = QPushButton("Guardar", self)
        self.btn_guardar_producto.setFixedWidth(135)
        self.btn_guardar_producto.setFixedHeight(28)
        self.btn_guardar_producto.move(215, 400)
        self.btn_guardar_producto.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: \'white\';")
        self.btn_guardar_producto.clicked.connect(self.insertar_inventario)                                 
        self.btn_guardar_producto.setFont(fuente)
        self.btn_menu = QPushButton("Menu Principal", self)
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(415, 400)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.clicked.connect(self.Llamar_inventario)     
        self.btn_menu.setFont(fuente)
    

    def insertar_inventario(self):
        """ Insertar los valores del formulario a la tabla de empleado """
        # Verificar si los valores requeridos fueron agregados
        if (self.input_nombre_producto.text() or self.input_categoria_producto.text() 
            or self.input_existencia_producto.text() or self.input_precio_compra.text() or
            self.input_precio_venta.text() != ""):
            inventario = (str(self.input_categoria_producto.text()),str(self.input_nombre_producto.text()) ,
                        str(self.input_existencia_producto.text()) , str(self.input_precio_compra.text()),
                        str(self.input_precio_venta.text()))
            try:
                self.basedatos.add_producto(inventario)
                QMessageBox.information(
                    self, "Guardar", "Producto agregado correctamente")
                self.close()
                
                self.Llamar_inventario()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar el producto")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")    
    
    def Llamar_inventario(self):
        self.ventaInve = VentanaInventario()
        self.close()    

    #------------------------------Pantalla Agregar Inventario---------------------------------
class AgregarProducto(QWidget):

    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar Producto")
        self.setGeometry(430, 120, 750, 550)
        self.UI()
        self.show()
        
    def UI(self):
        """ Componentes del diseño de la ventana """
        self.encabezado()
        self.widgets()
        self.botones() 
        self.CargarComboBoxCategoria()

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

        self.lbl_Titulo = QLabel("<font color='white'>Agregar Producto</font>", frame)
        self.lbl_Titulo.setFont(fuenteTitulo)
        self.lbl_Titulo.move(270, 25)

    def widgets(self):
        """ Widgets que conforman la ventana de agregar un producto """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)
        
        self.lbl_nombre_producto = QLabel("Nombre del Producto: ", self)
        self.lbl_nombre_producto.setFont(fuente)
        self.lbl_nombre_producto.move(60, 140)
        self.input_nombre_producto = QLineEdit(self)
        self.input_nombre_producto.move(225, 140)
        self.input_nombre_producto.setFixedWidth(400)
        self.lbl_categoria_producto = QLabel("Categoria: ", self)
        self.lbl_categoria_producto.setFont(fuente)
        self.lbl_categoria_producto.move(60, 180)
        self.input_categoria_producto = QComboBox(self)
        self.input_categoria_producto.move(225, 180)
        self.input_categoria_producto.setFixedWidth(400)
        self.lbl_existencia_producto = QLabel("Existencia: ", self)
        self.lbl_existencia_producto.setFont(fuente)
        self.lbl_existencia_producto.move(60, 220)
        self.input_existencia_producto = QLineEdit(self)
        self.input_existencia_producto.move(225, 220)
        self.input_existencia_producto.setFixedWidth(400)  
        self.lbl_precio_compra = QLabel("Precio de Compra: ", self)
        self.lbl_precio_compra.setFont(fuente)
        self.lbl_precio_compra.move(60, 260)
        self.input_precio_compra = QLineEdit(self)
        self.input_precio_compra.move(225, 260)
        self.input_precio_compra.setFixedWidth(400)
        self.lbl_precio_venta = QLabel("Precio de venta: ", self)
        self.lbl_precio_venta.setFont(fuente)
        self.lbl_precio_venta.move(60, 300)
        self.input_precio_venta = QLineEdit(self)
        self.input_precio_venta.move(225, 300)
        self.input_precio_venta.setFixedWidth(400)  

    def botones(self):
        """ Botones que conforman la ventana de agregar un producto """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.btn_guardar_producto = QPushButton("Guardar", self)
        self.btn_guardar_producto.setFixedWidth(135)
        self.btn_guardar_producto.setFixedHeight(28)
        self.btn_guardar_producto.move(215, 400)
        self.btn_guardar_producto.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: \'white\';")
        self.btn_guardar_producto.clicked.connect(self.insertar_inventario)                                 
        self.btn_guardar_producto.setFont(fuente)
        self.btn_menu = QPushButton("Menu Principal", self)
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(415, 400)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.clicked.connect(self.Llamar_inventario)     
        self.btn_menu.setFont(fuente)
    
    def insertar_inventario(self):
        """ Insertar los valores del formulario a la tabla de empleado """
        # Verificar si los valores requeridos fueron agregados
        if (self.input_nombre_producto.text() or self.input_categoria_producto.text() 
            or self.input_existencia_producto.text() or self.input_precio_compra.text() or
            self.input_precio_venta.text() != ""):
            inventario = (str(self.input_categoria_producto.text()), str(self.input_nombre_producto.text()), 
                         str(self.input_precio_compra.text()), str(self.input_precio_venta.text()),
                         str(self.input_existencia_producto.text()) )
            try:
                self.basedatos.add_producto(inventario)
                QMessageBox.information(
                    self, "Guardar", "Producto agregado correctamente")
                self.close()
                
                self.Llamar_inventario()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar el producto")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")   


    def CargarComboBoxCategoria(self):
        'Carga productos en el combobox'
        items = self.basedatos.obtenerCategoria()
        for item in range(0 , len(items)):
            self.input_categoria_producto.addItems(items[item])
         
             
    def Llamar_inventario(self):
        self.ventaInve = VentanaInventario()
        self.close()        
#------------------------------------------------------------------------------------------------------------
#----------------------------Pantalla Modificar Producto----------------------------------------------------
class EditarProducto(QWidget):
    """ Ventana para Editar productos """

    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Editar Producto")
        self.setGeometry(430, 120, 750, 550)
        self.UI()
        self.show()

    def UI(self):
        """ Componentes del diseño de la edicion """
        self.encabezado()
        self.widgets()
        self.botones() 
        self.cargarDatosProducto()

    def encabezado(self):
        """ Encabezado de la edicion """
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

        self.lbl_Titulo = QLabel("<font color='white'>Editar Producto</font>", frame)
        self.lbl_Titulo.setFont(fuenteTitulo)
        self.lbl_Titulo.move(270, 25)

    def widgets(self):
        """ Widgets que conforman la ventana de Editar Producto """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)
        
        self.lbl_nombre_producto = QLabel("Nombre del Producto: ", self)
        self.lbl_nombre_producto.setFont(fuente)
        self.lbl_nombre_producto.move(60, 140)
        self.input_nombre_producto = QLineEdit(self)
        self.input_nombre_producto.move(225, 140)
        self.input_nombre_producto.setFixedWidth(400)
        self.lbl_categoria_producto = QLabel("Categoria: ", self)
        self.lbl_categoria_producto.setFont(fuente)
        self.lbl_categoria_producto.move(60, 180)
        self.input_categoria_producto = QLineEdit(self)
        self.input_categoria_producto.move(225, 180)
        self.input_categoria_producto.setFixedWidth(400)
        self.lbl_existencia_producto = QLabel("Existencia: ", self)
        self.lbl_existencia_producto.setFont(fuente)
        self.lbl_existencia_producto.move(60, 220)
        self.input_existencia_producto = QLineEdit(self)
        self.input_existencia_producto.move(225, 220)
        self.input_existencia_producto.setFixedWidth(400)  
        self.lbl_precio_compra = QLabel("Precio de Compra: ", self)
        self.lbl_precio_compra.setFont(fuente)
        self.lbl_precio_compra.move(60, 260)
        self.input_precio_compra = QLineEdit(self)
        self.input_precio_compra.move(225, 260)
        self.input_precio_compra.setFixedWidth(400)
        self.lbl_precio_venta = QLabel("Precio de venta: ", self)
        self.lbl_precio_venta.setFont(fuente)
        self.lbl_precio_venta.move(60, 300)
        self.input_precio_venta = QLineEdit(self)
        self.input_precio_venta.move(225, 300)
        self.input_precio_venta.setFixedWidth(400)  

    def botones(self):
        """ Botones que conforman la edicion del producto """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.btn_editar_producto = QPushButton("Modificar", self)
        self.btn_editar_producto.setFixedWidth(135)
        self.btn_editar_producto.setFixedHeight(28)
        self.btn_editar_producto.move(215, 400)
        self.btn_editar_producto.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: \'white\';")
        self.btn_editar_producto.setFont(fuente)
        self.btn_editar_producto.clicked.connect(self.modificarProducto)
        self.btn_menu = QPushButton("Menu Principal", self)
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(415, 400)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: \'white\';")
        self.btn_menu.setFont(fuente)
        self.btn_menu.clicked.connect(self.pantallaPrincipal)


    def  cargarDatosProducto(self):
        '''Carga los datos seleccionados en la lista para luego ser 
        modificados por el usuario''' 
        products = self.basedatos.obtenerProductoPorId(id)
        if products:
            for product in products:
                    
                self.input_nombre_producto.setText(products[2]) 
                self.input_categoria_producto.setText(products[1]) 
                self.input_existencia_producto.setText(str(products[5])) 
                self.input_precio_compra.setText(str(products[3])) 
                self.input_precio_venta.setText(str(products[4])) 

    def modificarProducto(self):
        """ Modifica los valores del formulario a la tabla de productos """


        if (self.input_nombre_producto.text () or self.input_categoria_producto.text() or
                self.input_existencia_producto.text() or self.input_precio_compra.text() or
                self.input_precio_venta.text() != ""):
                producto = (str(self.input_categoria_producto.text()), str(self.input_nombre_producto.text()), 
                         str(self.input_precio_compra.text()), str(self.input_precio_venta.text()),
                         str(self.input_existencia_producto.text()), id)

                try: 
                    self.basedatos.modificarProductoPorId(producto)
                    QMessageBox.information(self,"Guardar","Datos modificados correctamente ")
                    
                    
                    self.close()
                    self.pantallaPrincipal()
                except Error as e:
                    QMessageBox.information(
                        self, "Error", "Error al momento de modificar datos")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")    

    def pantallaPrincipal(self):
        self.pantala = VentanaInventario()
        self.close() 

#----------------------------------------------------------------------------------------------------------
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

    #------------------------------------------------------------------------------------------

    #-------------PANTALLA VENTA--------------
class VentanaVentas(QWidget):
    """ Ventana de listado de ventas del sistema """
    def __init__(self):
        super().__init__()
        self.basedatos  = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Ventas")
        self.setGeometry(430, 110, 700, 600)
        self.principal_ventas()    
        self.show()


    def principal_ventas(self):
        """ Componentes del diseño de la ventana ventas """
        self.encabezado_ventas()
        self.botones_ventas()
        self.layouts_ventas()
        self.llenar_lista_venta()
        #self.llenar_detalle()

    def encabezado_ventas(self):
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


    def botones_ventas(self):
        """ Botones que conforman la ventana de venta """
        self.lista_ventas = QListWidget()
        self.lista_ventas.setFixedHeight(500)
        self.lista_ventas.setFixedWidth(400)
        #self.lista_ventas.clicked.connect(self.llenar_detalle)
        self.lbl_detalle = QLabel("<font color='black'>Ventasbhbhjbhjbj</font>")
        self.btn_nueva_venta = QPushButton("Nueva Venta")
        self.btn_nueva_venta.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_nueva_venta.setFixedWidth(165)
        self.btn_nueva_venta.setFixedHeight(40)
        self.btn_nueva_venta.clicked.connect(self.nuevaVenta)


        self.btn_eliminar = QPushButton("Eliminar Venta")
        self.btn_eliminar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar.clicked.connect(self.eliminar_venta)                                 
        self.btn_eliminar.setFixedWidth(165)
        self.btn_eliminar.setFixedHeight(40)
       

        self.btn_menu = QPushButton("Menu Principal")
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.clicked.connect(self.llamar_menu)                                 
        self.btn_menu.setFixedWidth(165)
        self.btn_menu.setFixedHeight(40)


    def eliminar_venta(self):
        """ Elimina la venta que se encuentra seleccionada """
        if self.lista_ventas.selectedItems():
            venta = self.lista_ventas.currentItem().text()
            id_venta = venta.split(" -- ")[0]

            venta = self.basedatos.obtenerVentaPorId(id_venta)

            yes = QMessageBox.Yes

            if venta:
                question_text = "¿Está seguro de eliminar la venta ?"
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.basedatos.eliminar_venta(venta[0])
                    QMessageBox.information(self, "Información", "¡Venta eliminada satisfactoriamente!")
                    self.lista_ventas.clear()
                    self.llenar_lista_venta()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar un empleado a eliminar")   


    def llenar_lista_venta(self):
        """ Obtiene las tuplas de ventas y las muestra en la lista """
        ventas = self.basedatos.obtenerTablaVenta()
        self.lista_ventas.addItem("N°--Cliente--Empleado--Total")

        if ventas:
            for venta in ventas:
                self.lista_ventas.addItem(
                    "{0} -- {1} -- {2} -- {3} "
                    .format(venta[0], venta[1], venta[2], venta[3]))

    #Tratamos de cargar el detalle de la venta en un label    
    #def llenar_detalle(self):
        # Obtiene el detalle de la venta seleccionada 
        #if self.lista_ventas.selectedItems():
            #det = self.lista_ventas.currentItem().text()
            #id_venta = det.split(" -- ")[1]
            #detalles = self.basedatos.obtenerDetalleVenta(id_venta)
            #if detalles:
                #for detalle in detalles:
                    #self.lbl_detalle.setText(
                        #"{2} -- {3} -- {4} -- {5} -- {6}  "
                        #.format(detalle[2], detalle[3], detalle[4], detalle[5],detalle[6]))"""




    def nuevaVenta(self):
        self.NuevaVenta = AgregarVenta() 
        self.close()


    def layouts_ventas(self):
        """ Layouts que componen la ventana de Venta. """
        # Layouts
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 60)
        self.main_layout.addLayout(self.right_main_layout, 40)
        self.main_layout.addLayout(self.top_layout)

        self.left_layout.addWidget(self.lista_ventas)
        #self.left_layout.addWidget(self.lbl_detalle)

        self.right_top_layout.addWidget(self.btn_nueva_venta)
        self.right_main_layout.addWidget(self.btn_menu)
        self.right_bottom_layout.addWidget(self.btn_eliminar)
        self.top_layout.addWidget(self.encabezado_ventas())
        self.setLayout(self.main_layout)


    def llamar_menu(self):
        self.call = Menu()
        self.close()    
   

#------PANTALLA CLIENTE ------------
class VentanaCliente(QWidget):
    """ Ventana de listado de clientes """
    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Clientes")
        self.setGeometry(430, 110, 700, 600)
        self.principalCliente()
        self.show()


    def principalCliente(self):
        """ Componentes del diseño de la ventana """    
        self.encabezado_cliente()
        self.botones_cliente()
        self.layouts_cliente()
        self.llenar_lista_cliente()

    def encabezado_cliente(self):
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


    def agregar_cliente(self):
        """Manda a llamar la pantalla agregar cliente """
        self.llamar = AgregarCliente()
        self.close()

    
    def modificar_cliente(self):
        """Manda a llamar la pantalla modificar cliente"""
        self.modificar = ModificarCliente()
        self.close()


    
    def cargarDatosAModificar(self):
        """Carga los datos que seran modificados por el usuario"""
        global idCliente
        if self.lista_clientes.selectedItems():
            cliente = self.lista_clientes.currentItem().text()
            idCliente =  cliente.split(" -- ")[0]
            #QMessageBox.information(self,"Informacion",cliente[0])  

            self.modificar_cliente()
        else:
            QMessageBox.information(self,"Informacion","No selecciono ningun cliente")  


    def botones_cliente(self):
        """ Botones que conforman la ventana de clientes """
        self.lista_clientes = QListWidget()
        self.btn_editar_cliente = QPushButton("Agregar Cliente")
        self.btn_editar_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_editar_cliente.setFixedWidth(165)
        self.btn_editar_cliente.setFixedHeight(40)
        self.btn_editar_cliente.clicked.connect(self.agregar_cliente)

        self.btn_modificar_cliente = QPushButton("Modificar Cliente")
        self.btn_modificar_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_modificar_cliente.setFixedWidth(165)
        self.btn_modificar_cliente.setFixedHeight(40)
        self.btn_modificar_cliente.clicked.connect(self.cargarDatosAModificar)

        self.btn_eliminar_cliente = QPushButton("Eliminar Cliente")
        self.btn_eliminar_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar_cliente.setFixedWidth(165)
        self.btn_eliminar_cliente.setFixedHeight(40)
        self.btn_eliminar_cliente.clicked.connect(self.eliminar_cliente)
        self.btn_menu_cliente = QPushButton("Menu Principal")
        self.btn_menu_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu_cliente.setFixedWidth(165)
        self.btn_menu_cliente.setFixedHeight(40)
        self.btn_menu_cliente.clicked.connect(self.llamar_menu)


    def layouts_cliente(self):
        """ Layouts que componen la ventana """
        
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_middle_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()
        self.top_layout = QVBoxLayout()

        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_middle_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 70)
        self.main_layout.addLayout(self.right_main_layout, 30)
        self.main_layout.addLayout(self.top_layout)
        
        self.left_layout.addWidget(self.lista_clientes)
        self.right_middle_layout.addWidget(self.btn_modificar_cliente)
        self.right_top_layout.addWidget(self.btn_editar_cliente)
        self.right_main_layout.addWidget(self.btn_menu_cliente)
        self.right_bottom_layout.addWidget(self.btn_eliminar_cliente)
        self.top_layout.addWidget(self.encabezado_cliente())
        self.setLayout(self.main_layout)


    def eliminar_cliente(self):
        """ Elimina el cliente que se encuentra seleccionado """
        if self.lista_clientes.selectedItems():
            cliente = self.lista_clientes.currentItem().text()
            idCliente = cliente.split(" -- ")[0]

            cliente = self.basedatos.obtenerClientesPorId(idCliente)

            yes = QMessageBox.Yes

            if cliente:
                question_text = "¿Está seguro de eliminar el cliente ?"
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.basedatos.eliminar_cliente(cliente[0])
                    QMessageBox.information(self, "Información", "¡Cliente eliminado satisfactoriamente!")
                    self.lista_clientes.clear()
                    self.llenar_lista_cliente()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar un empleado a cliente")   


    def llenar_lista_cliente(self):
        """ Obtiene las tuplas de clientes y las muestra en la lista """
        clientes = self.basedatos.obtenerCliente()

        if clientes:
            for cliente in clientes:
                self.lista_clientes.addItem(
                    "{0} -- {1} -- {2} -- {3} -- {4} -- {5} -- {6} "
                    .format(cliente[0], cliente[1], cliente[2], cliente[3],
                     cliente[4], cliente[5], cliente[6]))    

    def llamar_menu(self):
        self.call = Menu()
        self.close()    



    #-----------PANTALLA EMPLEADOS-------------------
        
#------Agregar Cliente---------------
class AgregarCliente(QWidget):
    """ Ventana para agregar nuevos clientes """

    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Agregar un cliente")
        self.setGeometry(430, 120, 750, 650)
        self.UI()
        self.show()
        
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

        self.lbl_id_cliente = QLabel("Identidad: ", self)
        self.lbl_id_cliente.setFont(fuente)
        self.lbl_id_cliente.move(60, 140)
        self.input_id_cliente = QLineEdit(self)
        self.input_id_cliente.move(250, 140)
        self.input_id_cliente.setFixedWidth(400)
        self.lbl_nombre_cliente = QLabel("Nombre del cliente: ", self)
        self.lbl_nombre_cliente.setFont(fuente)
        self.lbl_nombre_cliente.move(60, 180)
        self.input_nombre = QLineEdit(self)
        self.input_nombre.move(250, 180)
        self.input_nombre.setFixedWidth(400)
        self.lbl_telefono_cliente = QLabel("Telefono: ", self)
        self.lbl_telefono_cliente.setFont(fuente)
        self.lbl_telefono_cliente.move(60, 220)
        self.input_telefono_cliente = QLineEdit(self)
        self.input_telefono_cliente.move(250, 220)
        self.input_telefono_cliente.setFixedWidth(400)
        self.lbl_celular_cliente = QLabel("Celular: ", self)
        self.lbl_celular_cliente.setFont(fuente)
        self.lbl_celular_cliente.move(60, 260)
        self.input_celular_cliente = QLineEdit(self)
        self.input_celular_cliente.move(250, 260)
        self.input_celular_cliente.setFixedWidth(400)  
        self.lbl_rtn_cliente = QLabel("RTN: ", self)
        self.lbl_rtn_cliente.setFont(fuente)
        self.lbl_rtn_cliente.move(60, 300)
        self.input_rtn_cliente = QLineEdit(self)
        self.input_rtn_cliente.move(250, 300)
        self.input_rtn_cliente.setFixedWidth(400)
        self.lbl_direccion_cliente = QLabel("Direccion: ", self)
        self.lbl_direccion_cliente.setFont(fuente)
        self.lbl_direccion_cliente.move(60, 340)
        self.input_direccion_cliente = QLineEdit(self)
        self.input_direccion_cliente.move(250, 340)
        self.input_direccion_cliente.setFixedWidth(400)
        self.lbl_correo_cliente = QLabel("Correo Electronico: ", self)
        self.lbl_correo_cliente.setFont(fuente)
        self.lbl_correo_cliente.move(60, 380)
        self.input_correo_cliente = QLineEdit(self)
        self.input_correo_cliente.move(250, 380)
        self.input_correo_cliente.setFixedWidth(400)


    def botones(self):
        """ Botones que conforman la ventana de agregar cliente """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)

        self.btn_guardar_cliente = QPushButton("Guardar", self)
        self.btn_guardar_cliente.setFixedWidth(135)
        self.btn_guardar_cliente.setFixedHeight(28)
        self.btn_guardar_cliente.move(215, 510)
        self.btn_guardar_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_guardar_cliente.setFont(fuente)
        self.btn_guardar_cliente.clicked.connect(self.insertarCliente)

        self.btn_menu = QPushButton("Menu Principal", self)
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(415, 510)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.setFont(fuente)
        self.btn_menu.clicked.connect(self.llamar_cliente)     


    def llamar_cliente(self):
        """Llamando la ventana de cliente"""
        self.cliente = VentanaCliente()
        self.close()


    def insertarCliente(self):
        """ Insertar los valores del formulario a la tabla de cliente """
        # Verificar si los valores requeridos fueron agregados
        if(self.input_nombre.text() or self.input_id_cliente.text() or
            self.input_telefono_cliente.text() or self.input_celular_cliente.text() or
            self.input_rtn_cliente.text() or self.input_direccion_cliente.text() or
            self.input_correo_cliente.text() != ""):
            cliente = (str(self.input_id_cliente.text()), str(self.input_nombre.text()),
                        str(self.input_telefono_cliente.text()) , str(self.input_celular_cliente.text()),
                        str(self.input_direccion_cliente.text()) ,  str(self.input_correo_cliente.text()),
                        str(self.input_rtn_cliente.text()))

            try:
                self.basedatos.add_cliente(cliente)
                QMessageBox.information(
                self, "Guardar", "Cliente agregado correctamente")
                self.close()
                self.llamar_cliente()
                
                #self.llamar_cliente()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar el cliente")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")    







class ModificarCliente(QWidget):
    """ Ventana para agregar nuevos clientes """

    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Modificar un cliente")
        self.setGeometry(430, 120, 750, 650)
        self.UI()
        self.show()
        
    def UI(self):
        """ Componentes del diseño de la ventana """
        self.encabezado()
        self.labels()
        self.botones()
        self.cargarDatos()

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

        lbl_Titulo = QLabel("<font color='white'>Modificar Cliente</font>", frame)
        lbl_Titulo.setFont(fuenteTitulo)
        lbl_Titulo.move(280, 25)

    def labels(self):
        """ Botones que conforman la ventana de agregar cliente """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)
        self.lbl_id_cliente = QLabel("Identidad: ", self)
        self.lbl_id_cliente.setFont(fuente)
        self.lbl_id_cliente.move(60, 140)
        self.input_id_cliente = QLineEdit(self)
        self.input_id_cliente.move(250, 140)
        self.input_id_cliente.setFixedWidth(400)
        self.lbl_nombre_cliente = QLabel("Nombre del cliente: ", self)
        self.lbl_nombre_cliente.setFont(fuente)
        self.lbl_nombre_cliente.move(60, 180)
        self.input_nombre_cliente = QLineEdit(self)
        self.input_nombre_cliente.move(250, 180)
        self.input_nombre_cliente.setFixedWidth(400)
        self.lbl_telefono_cliente = QLabel("Telefono: ", self)
        self.lbl_telefono_cliente.setFont(fuente)
        self.lbl_telefono_cliente.move(60, 220)
        self.input_telefono_cliente = QLineEdit(self)
        self.input_telefono_cliente.move(250, 220)
        self.input_telefono_cliente.setFixedWidth(400)
        self.lbl_celular_cliente = QLabel("Celular: ", self)
        self.lbl_celular_cliente.setFont(fuente)
        self.lbl_celular_cliente.move(60, 260)
        self.input_celular_cliente = QLineEdit(self)
        self.input_celular_cliente.move(250, 260)
        self.input_celular_cliente.setFixedWidth(400)  
        self.lbl_rtn_cliente = QLabel("RTN: ", self)
        self.lbl_rtn_cliente.setFont(fuente)
        self.lbl_rtn_cliente.move(60, 300)
        self.input_rtn_cliente = QLineEdit(self)
        self.input_rtn_cliente.move(250, 300)
        self.input_rtn_cliente.setFixedWidth(400)
        self.lbl_direccion_cliente = QLabel("Direccion: ", self)
        self.lbl_direccion_cliente.setFont(fuente)
        self.lbl_direccion_cliente.move(60, 340)
        self.input_direccion_cliente = QLineEdit(self)
        self.input_direccion_cliente.move(250, 340)
        self.input_direccion_cliente.setFixedWidth(400)
        self.lbl_correo_cliente = QLabel("Correo Electronico: ", self)
        self.lbl_correo_cliente.setFont(fuente)
        self.lbl_correo_cliente.move(60, 380)
        self.input_correo_cliente = QLineEdit(self)
        self.input_correo_cliente.move(250, 380)
        self.input_correo_cliente.setFixedWidth(400)


    def botones(self):
        """ Botones que conforman la ventana de agregar cliente """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)
        self.btn_guardar_cliente = QPushButton("Guardar", self)
        self.btn_guardar_cliente.setFixedWidth(135)
        self.btn_guardar_cliente.setFixedHeight(28)
        self.btn_guardar_cliente.move(215, 510)
        self.btn_guardar_cliente.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_guardar_cliente.setFont(fuente)
        self.btn_guardar_cliente.clicked.connect(self.Modificar_Cliente)
        self.btn_menu = QPushButton("Menu Principal", self)
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(415, 510)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.setFont(fuente) 
        self.btn_menu.clicked.connect(self.Menu)



    def  cargarDatos(self):
        '''Carga los datos seleccionados en la lista para luego ser 
        modificados por el usuario'''    
        clientes = self.basedatos.obtenerClientesPorId(idCliente)
        if clientes:
            for cliente in clientes:
                self.input_id_cliente.setText(clientes[1]) 
                self.input_nombre_cliente.setText(clientes[2])
                self.input_telefono_cliente.setText(clientes[3]) 
                self.input_celular_cliente.setText(clientes[4]) 
                self.input_rtn_cliente.setText(clientes[7]) 
                self.input_direccion_cliente.setText(clientes[5]) 
                self.input_correo_cliente.setText(clientes[6]) 

    

    def Modificar_Cliente(self):
        """ Modifica los valores del formulario a la tabla de cliente """
        if(self.input_nombre_cliente.text() or self.input_id_cliente.text() or
            self.input_telefono_cliente.text() or self.input_celular_cliente.text() or
            self.input_rtn_cliente.text() or self.input_direccion_cliente.text() or
            self.input_correo_cliente.text() != ""):
            cliente = (str(self.input_id_cliente.text()), str(self.input_nombre_cliente.text()),
                        str(self.input_telefono_cliente.text()) , str(self.input_celular_cliente.text()),
                        str(self.input_direccion_cliente.text()) ,  str(self.input_correo_cliente.text()),
                        str(self.input_rtn_cliente.text()),idCliente)

            try:
                self.basedatos.modificarClientePorId(cliente)
                QMessageBox.information(
                    self, "Guardar", "Datos modificados correctamente")
                self.close()
                self.pantallaAnterior()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de modificar datos")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")    


    def pantallaAnterior(self):
        self.pantalla = VentanaCliente()
        self.close()     

    def Menu(self):
        self.call = Menu()      
        self.close()      





class empleados(QWidget):
    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
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
        self.llenar_lista_empleado()

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
        
        self.btn_editar_empleado = QPushButton("Guardar Empleado")
        self.btn_editar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_editar_empleado.setFixedWidth(165)
        self.btn_editar_empleado.setFixedHeight(40)
        self.btn_editar_empleado.clicked.connect(self.GestionarEmpleado)

        self.btn_modificar_empleado = QPushButton("Modificar Empleado")
        self.btn_modificar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_modificar_empleado.setFixedWidth(165)
        self.btn_modificar_empleado.setFixedHeight(40)
        self.btn_modificar_empleado.clicked.connect(self.cargarDatosAModificar)

        self.btn_eliminar_empleado = QPushButton("Eliminar Empleado")
        self.btn_eliminar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_eliminar_empleado.clicked.connect(self.eliminar_empleado)                                 
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
        self.close()


    def layoutsEmpleado(self):
        """ Layouts que componen la aplicación. """
        # Layouts
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_middle_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()
        self.top_layout = QVBoxLayout()

        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_middle_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 70)
        self.main_layout.addLayout(self.right_main_layout, 30)
        self.main_layout.addLayout(self.top_layout)
        
        self.left_layout.addWidget(self.lista_empleados)
        self.right_middle_layout.addWidget(self.btn_modificar_empleado)
        self.right_top_layout.addWidget(self.btn_editar_empleado)
        self.right_main_layout.addWidget(self.btn_menu)
        self.right_bottom_layout.addWidget(self.btn_eliminar_empleado)
        self.top_layout.addWidget(self.encabezadoEmpleado())
        self.setLayout(self.main_layout) 

    
    def llenar_lista_empleado(self):
        """ Obtiene las tuplas de empleados y las muestra en la lista """
        empleados = self.basedatos.obtenerEmpleados()

        if empleados:
            for empleado in empleados:
                self.lista_empleados.addItem(
                    "{0} -- {1} -- {2} -- {3} -- {4} -- {5}-- {6} -- {7}"
                    .format(empleado[0], empleado[1], empleado[2], empleado[3],
                     empleado[4], empleado[5], empleado[6], empleado[7]))


    def eliminar_empleado(self):
        """ Elimina el empleado que se encuentra seleccionado """
        if self.lista_empleados.selectedItems():
            empleado = self.lista_empleados.currentItem().text()
            id = empleado.split(" -- ")[0]

            empleado = self.basedatos.obtenerEmpleadosPorId(id)

            yes = QMessageBox.Yes

            if empleado:
                question_text = "¿Está seguro de eliminar el empleado ?"
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.basedatos.eliminar_empleado(empleado[0])
                    QMessageBox.information(self, "Información", "¡Empleado eliminado satisfactoriamente!")
                    self.lista_empleados.clear()
                    self.llenar_lista_empleado()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar un empleado a eliminar")                
    
    def ModificarEmpleado(self):
        self.pantallaModificar = ModificarEmpleado()

    def ModificarEmpleado(self):
        self.pantallaModificar = ModificarEmpleado()


    def cargarDatosAModificar(self):
        '''Carga los datos que seran modificados por el usuario'''
        global id
        if self.lista_empleados.selectedItems():
            empleado = self.lista_empleados.currentItem().text()
            id =  empleado.split(" -- ")[0]
            self.ModificarEmpleado()
        else:
            QMessageBox.information(self,"Informacion","No selecciono ningun empleado")  
     

    def llamar_menu(self):
        self.call = Menu()
        self.close()



 #---------------PANTALLA AGREGAR  VENTA----------------------
class AgregarVenta(QWidget):
    """ Ventana para agregar una venta """

    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
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
        self.ObtenerVenta()
        self.CargarComboBox()
        self.CargarComboBoxClientes()
        self.CargarComboBoxEmpleados()


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
        self.lbl_num_venta.move(20, 100)
        self.input_num_venta = QLineEdit(self)
        self.input_num_venta.move(120, 100)
        self.input_num_venta.setFixedWidth(100)
        self.lbl_cliente = QLabel("Cliente: ", self)
        self.lbl_cliente.setFont(self.fuente)
        self.lbl_cliente.move(350, 100)
        self.input_cliente = QComboBox(self)
        self.input_cliente.move(450, 100)
        self.input_cliente.setFixedWidth(150)
        self.lbl_id_empleado = QLabel("Empleado: ", self)
        self.lbl_id_empleado.setFont(self.fuente)
        self.lbl_id_empleado.move(20, 150)
        self.input_id_empleado = QComboBox(self)
        self.input_id_empleado.move(120, 150)
        self.input_id_empleado.setFixedWidth(200)  
        self.lbl_id_producto = QLabel("Id Producto: ", self)
        self.lbl_id_producto.setFont(self.fuente)
        self.lbl_id_producto.move(20, 200)
        self.input_id_producto = QComboBox(self)
        self.input_id_producto.move(120, 200)
        self.input_id_producto.setFixedWidth(200)
        self.lbl_cantidad_venta = QLabel("Cantidad: ", self)
        self.lbl_cantidad_venta.setFont(self.fuente)
        self.lbl_cantidad_venta.move(350, 200)
        self.input_cantidad_venta = QLineEdit(self)
        self.input_cantidad_venta.move(450, 200)
        self.input_cantidad_venta.setFixedWidth(100)
        self.lbl_descuento = QLabel("Descuento: ", self)
        self.lbl_descuento.setFont(self.fuente)
        self.lbl_descuento.move(20, 250)
        self.input_descuento = QLineEdit(self)
        self.input_descuento.move(120, 250)
        self.input_descuento.setFixedWidth(100)
        self.lbl_total = QLabel("Total: ", self)
        self.lbl_total.setFont(self.fuente)
        self.lbl_total.move(20, 250)
        self.input_total = QLineEdit(self)
        self.input_total.move(120, 250)
        self.input_total.setFixedWidth(100)
       
        

    def botones(self):
        """ Botones que conforman la ventana de agregar venta """
        fuente = QFont()
        fuente.setPointSize(10)
        fuente.setFamily("Bahnschrift Light")
        fuente.setBold(True)
        self.lista_detalle = QListWidget()

        
        self.btn_Agregar = QPushButton("Agregar", self)
        self.btn_Agregar.setFixedWidth(135)
        self.btn_Agregar.setFixedHeight(28)
        self.btn_Agregar.move(250, 290)
        self.btn_Agregar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_Agregar.setFont(fuente)
        self.btn_Agregar.clicked.connect(self.CargarDetalle)

        self.btn_guardar = QPushButton("Guardar Venta", self)
        self.btn_guardar.setFixedWidth(135)
        self.btn_guardar.setFixedHeight(28)
        self.btn_guardar.move(390, 450)
        self.btn_guardar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_guardar.setFont(fuente)
        self.btn_guardar.clicked.connect(self.insertarVenta)

        self.btn_cancelar = QPushButton("Cancelar", self)
        self.btn_cancelar.setFixedWidth(135)
        self.btn_cancelar.setFixedHeight(28)
        self.btn_cancelar.move(390, 450)
        self.btn_cancelar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_cancelar.setFont(fuente)
        self.btn_cancelar.clicked.connect(self.llamarMenu)

    def llamarMenu(self):
        self.call = VentanaVentas() 
        self.close() 
        

    def layouts(self):
    
        self.main_layout = QVBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.middle_main_layout = QVBoxLayout()
        self.top_main_layout = QHBoxLayout()

        self.main_layout.addLayout(self.left_layout, 50)
        self.main_layout.addLayout(self.right_main_layout, 40)
        self.main_layout.addLayout(self.middle_main_layout, 10)
        self.main_layout.addLayout(self.top_main_layout, 10)
        self.right_main_layout.addWidget(self.lista_detalle)
        self.top_main_layout.addWidget(self.btn_guardar)
        self.top_main_layout.addWidget(self.btn_cancelar)

        self.middle_main_layout.addWidget(self.lbl_total)
        self.middle_main_layout.addWidget(self.input_total)
        self.setLayout(self.main_layout) 

    def ObtenerVenta(self):
        idventa = 0
        venta = self.basedatos.obtenerVenta()
        if(venta):
            idventa = (venta[0] + 1)
            self.input_num_venta.setText(str(idventa))
        else :
            idventa =  1
            self.input_num_venta.setText(str(idventa))


    def CargarComboBox(self):
        'Carga productos en el combobox'
        items = self.basedatos.ObtenerNombreProductos()
        for item in range(0 , len(items)):
            self.input_id_producto.addItems(items[item])


    def CargarComboBoxClientes(self):
        'Carga clientes en el combobox'
        items = self.basedatos.ObtenerNombreClientes()
        for item in range(0 , len(items)):
            self.input_cliente.addItems(items[item])

    def CargarComboBoxEmpleados(self):
        'Carga empleados en el combobox'
        items = self.basedatos.ObtenerNombreEmpleados()
        
        for item in range(0 , len(items)):
            self.input_id_empleado.addItems(items[item])        



    def CargarDetalle(self):
        'Carga el producto en el detalle de Venta' 
        global total
        idproducto = (self.input_id_producto.currentText())
        productos = self.basedatos.ObtenerProducto(idproducto)
        if productos:
            
            for producto in productos:
                subtotal = (producto[3] * int(self.input_cantidad_venta.text()))
                descuento = (subtotal * (int(self.input_descuento.text())/100)) 
                isv = (subtotal - descuento) * 0.15
                self.lista_detalle.addItem("""{0}           -- {1}    -- {2}            -- {3}       -- {4}          -- {5}         -- {6}    -- {7} """
                .format(producto[0], producto[1], producto[2], producto[3],self.input_cantidad_venta.text(),
                subtotal,descuento,isv))
                total += (subtotal -descuento) + isv
                id_venta = int(self.input_num_venta.text())
                tupladetalle = (id_venta, producto[0],
                            self.input_cantidad_venta.text(),producto[3],subtotal,descuento,isv) 
                self.input_total.setText(str(total))  
                self.basedatos.add_detalle(tupladetalle)  
                self.input_cantidad_venta.setText("")
                self.input_descuento.setText("")

               
    
 

    def insertarVenta(self):
        """ Insertar los valores del formulario a la tabla de empleado """
        # Verificar si los valores requeridos fueron agregados
        
        venta = (str(self.input_cliente.currentText()), str(self.input_id_empleado.currentText()),
                    str(self.input_total.text()))  
            
        try:
            self.basedatos.add_venta(venta)
            QMessageBox.information(
                self, "Guardar", "Venta agregado correctamente")
            self.close()
                
            self.ventana_ventas()
        except Error as e:
            QMessageBox.information(
                self, "Error", "Error al momento de agregar la venta")
        
        

    def ventana_ventas(self):
        self.call = VentanaVentas()
    

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

        self.btn_guardar_empleado = QPushButton("Guardar Cambios", self)
        self.btn_guardar_empleado.setFixedWidth(135)
        self.btn_guardar_empleado.setFixedHeight(28)
        self.btn_guardar_empleado.move(165, 510)
        self.btn_guardar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_guardar_empleado.setFont(self.fuente)
        self.btn_guardar_empleado.clicked.connect(self.insertarEmpleado)

        self.btn_menu = QPushButton("Cancelar",self)
        self.btn_menu.clicked.connect(self.llamar_empleados)
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(350, 510)
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
            empleado = ( str(self.input_id_empleado.text()), str(self.input_nombre_empleado.text()),
                        str(self.input_telefono_empleado.text()) , str(self.input_direccion_empleado.text()),
                        str(self.input_correo_empleado.text()) ,  str(self.input_user_empleado.text()),
                        str(self.input_contrasenia_empleado.text()) )

            try:
                self.basedatos.add_empleado(empleado)
                QMessageBox.information(
                    self, "Guardar", "Empleado agregado correctamente")
                self.close()
                
                self.llamar_empleados()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar el empleado")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")    


    def llamar_empleados(self):
        self.call = empleados()
        self.close()

    

    ########################################################################    
    

###########################################################################3
class ModificarEmpleado(QWidget):
    """ Ventana para modificar empleados """

    def __init__(self):
        super().__init__()
        self.basedatos = VentaDB("base_UMA.db")
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(229, 25, 25))
        self.setPalette(paleta)
        self.setWindowTitle("Modificar un Empleado")
        self.setGeometry(400, 120, 650, 600)
        self.principalModificarEmpleado()
        self.show()


    def principalModificarEmpleado(self):
        """ Componentes del diseño de la ventana """
        self.encabezadoModificarEmpleado()
        self.labelsModificarEmpleado()
        self.botonesModificarEmpleado()
        self.cargarDatos()
     

    def encabezadoModificarEmpleado(self):
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

        self.lbl_Titulo = QLabel("<font color='white'>Modificar Empleado</font>", self.frame)
        self.lbl_Titulo.setFont(self.fuenteTitulo)
        self.lbl_Titulo.move(270, 25)


    def labelsModificarEmpleado(self):
        """ Labels que conforman la ventana de agregar empleado """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.lbl_nombre_empleadoM = QLabel("Nombre: ", self)
        self.lbl_nombre_empleadoM.setFont(fuente)
        self.lbl_nombre_empleadoM.move(50, 130)
        self.input_nombre_empleadoM = QLineEdit(self)
        self.input_nombre_empleadoM.move(240, 130)
        self.input_nombre_empleadoM.setFixedWidth(360)
        self.lbl_id_empleadoM = QLabel("Identidad: ", self)
        self.lbl_id_empleadoM.setFont(fuente)
        self.lbl_id_empleadoM.move(50, 170)
        self.input_id_empleadoM = QLineEdit(self)
        self.input_id_empleadoM.move(240, 170)
        self.input_id_empleadoM.setFixedWidth(360) 

        self.lbl_telefono_empleadoM = QLabel("Telefono: ", self)
        self.lbl_telefono_empleadoM.setFont(fuente)
        self.lbl_telefono_empleadoM.move(50, 210)
        self.input_telefono_empleadoM = QLineEdit(self)
        self.input_telefono_empleadoM.move(240, 210)
        self.input_telefono_empleadoM.setFixedWidth(360) 
        self.lbl_direccion_empleadoM = QLabel("Direccion: ", self)
        self.lbl_direccion_empleadoM.setFont(fuente)
        self.lbl_direccion_empleadoM.move(50, 250)
        self.input_direccion_empleadoM = QLineEdit(self)
        self.input_direccion_empleadoM.move(240, 250)
        self.input_direccion_empleadoM.setFixedWidth(360)
        self.lbl_correo_empleadoM= QLabel("Correo Electronico: ", self)
        self.lbl_correo_empleadoM.setFont(fuente)
        self.lbl_correo_empleadoM.move(50, 290)
        self.input_correo_empleadoM = QLineEdit(self)
        self.input_correo_empleadoM.move(240, 290)
        self.input_correo_empleadoM.setFixedWidth(360)
        self.lbl_user_empleadoM = QLabel("Usuario: ", self)
        self.lbl_user_empleadoM.setFont(fuente)
        self.lbl_user_empleadoM.move(50, 330)
        self.input_user_empleadoM = QLineEdit(self)
        self.input_user_empleadoM.move(240, 330)
        self.input_user_empleadoM.setFixedWidth(360)
        self.lbl_contrasenia_empleadoM = QLabel("Contraseña: ", self)
        self.lbl_contrasenia_empleadoM.setFont(fuente)
        self.lbl_contrasenia_empleadoM.move(50, 370)
        self.input_contrasenia_empleadoM = QLineEdit(self)
        self.input_contrasenia_empleadoM.move(240, 370)
        self.input_contrasenia_empleadoM.setFixedWidth(360)


    def botonesModificarEmpleado(self):
        """ Botones que conforman la ventana de agregar empleado """
        self.fuente = QFont()
        self.fuente.setPointSize(10)
        self.fuente.setFamily("Bahnschrift Light")
        self.fuente.setBold(True)

        self.btn_modificar_empleado = QPushButton("Guardar Cambios", self)
        self.btn_modificar_empleado.setFixedWidth(135)
        self.btn_modificar_empleado.setFixedHeight(28)
        self.btn_modificar_empleado.move(165, 510)
        self.btn_modificar_empleado.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_modificar_empleado.setFont(self.fuente)
        self.btn_modificar_empleado.clicked.connect(self.modificarEmpleado)

        self.btn_menu = QPushButton("Cancelar",self)
        self.btn_menu.clicked.connect(self.pantallaAnterior)
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(350, 510)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        self.btn_menu.setFont(fuente)    
    


   
    def  cargarDatos(self):
        '''Carga los datos seleccionados en la lista para luego ser 
        modificados por el usuario'''    
        employees = self.basedatos.obtenerEmpleadosPorId(id)
        if employees:
            for  employee in employees:
                    
                self.input_nombre_empleadoM.setText(employees[1]) 
                self.input_id_empleadoM.setText(employees[2]) 
                self.input_telefono_empleadoM.setText(employees[3]) 
                self.input_direccion_empleadoM.setText(employees[4]) 
                self.input_correo_empleadoM.setText(employees[5]) 
                self.input_user_empleadoM.setText(employees[6]) 
                self.input_contrasenia_empleadoM.setText(employees[7]) 


    def modificarEmpleado(self):
        """ Modifica los valores del formulario a la tabla de empleado """


        if (self.input_nombre_empleadoM.text () or self.input_id_empleadoM.text() or
                self.input_telefono_empleadoM.text() or self.input_direccion_empleadoM.text() or
                self.input_correo_empleadoM.text() or self.input_user_empleadoM.text() or
                self.input_contrasenia_empleadoM.text() != ""):
            empleado = (str(self.input_nombre_empleadoM.text()), str(self.input_id_empleadoM.text()),
                        str(self.input_telefono_empleadoM.text()) , str(self.input_direccion_empleadoM.text()),
                        str(self.input_correo_empleadoM.text()) ,  str(self.input_user_empleadoM.text()),
                        str(self.input_contrasenia_empleadoM.text()) , id )

            try:
                self.basedatos.modificarEmpleadoPorId(empleado)
                QMessageBox.information(
                    self, "Guardar", "Datos modificados correctamente")
                
                    
                self.close()
                self.pantallaAnterior()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de modificar datos")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")    

    def pantallaAnterior(self):
        self.pantalla = empleados() 
        self.close()
    

class VentanaLogin(QWidget):
    """ Ventana de login para que el usuario ingrese al sistema """

    def __init__(self, parent=None):

      super(VentanaLogin, self).__init__(parent)
      self.basedatos = VentaDB("base_UMA.db")  
      self.setWindowTitle("LOGIN")
      self.setWindowIcon(QIcon("Logo.png"))
      self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
      self.setFixedSize(400, 380)
      #Color de fondo de la ventana
      paleta = QPalette()
      paleta.setColor(QPalette.Background, QColor(229, 25, 25))
      self.setPalette(paleta)

      self.UI()
      self.show()

    def UI(self):
      """ Cargar lo que es el diseño de la ventana """
      self.encabezado()
      self.widgets()
      self.boton()


    def encabezado(self):
      """ Encabezado de la ventana """
      #Color de fondo del encabezado
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

      font = QFont()
      font.setPointSize(19)
      font.setBold(True) 

      lbl_titulo = QLabel("<font color='white'>LOGIN</font>", frame)
      lbl_titulo.setFont(font)
      lbl_titulo.move(165, 25)

    def widgets(self):      
      """ Creacion de los respectivos widgets que forman parte de la interfaz """
      # Usuario

      lbl_Usuario = QLabel("Usuario", self)
      lbl_Usuario.move(60, 120)
      font = QFont()
      font.setBold(True)
      font.setPointSize(10)
      font.setFamily("Bahnschrift Light")
      lbl_Usuario.setFont(font)
      frameUsuario = QFrame(self)
      frameUsuario.setFrameShape(QFrame.StyledPanel)
      frameUsuario.setFixedWidth(280)
      frameUsuario.setFixedHeight(28)
      frameUsuario.move(60, 146)

      imagenUsuario = QLabel(frameUsuario)
      imagenUsuario.setPixmap(QPixmap("user.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
      imagenUsuario.move(10, 4)

      self.lineEditUsuario = QLineEdit(frameUsuario)
      self.lineEditUsuario.setFrame(False)
      self.lineEditUsuario.setTextMargins(8, 0, 4, 1)
      self.lineEditUsuario.setFixedWidth(238)
      self.lineEditUsuario.setFixedHeight(26)
      self.lineEditUsuario.move(40, 1)

      # Contraseña 

      lbl_Contrasenia = QLabel("Contraseña", self)
      lbl_Contrasenia.move(60, 200)
      font = QFont()
      font.setBold(True)
      font.setPointSize(10)
      font.setFamily("Bahnschrift Light")
      lbl_Contrasenia.setFont(font)

      frameContrasenia = QFrame(self)
      frameContrasenia.setFrameShape(QFrame.StyledPanel)
      frameContrasenia.setFixedWidth(280)
      frameContrasenia.setFixedHeight(28)
      frameContrasenia.move(60, 226)

      imagenContrasenia = QLabel(frameContrasenia)
      imagenContrasenia.setPixmap(QPixmap("lock.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
      imagenContrasenia.move(10, 4)

      self.lineEditContrasenia = QLineEdit(frameContrasenia)
      self.lineEditContrasenia.setFrame(False)
      self.lineEditContrasenia.setEchoMode(QLineEdit.Password)
      self.lineEditContrasenia.setTextMargins(8, 0, 4, 1)
      self.lineEditContrasenia.setFixedWidth(238)
      self.lineEditContrasenia.setFixedHeight(26)
      self.lineEditContrasenia.move(40, 1)

    def boton(self):
      """ Boton de iniciar sesion del login """
      btn_login = QPushButton("Iniciar sesión", self)
      btn_login.setFixedWidth(135)
      btn_login.setFixedHeight(28)
      btn_login.move(130, 296)
      btn_login.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "color: \'white\';")
      btn_login.clicked.connect(self.login)
      font = QFont()
      font.setBold(True)
      font.setPointSize(10)
      font.setFamily("Bahnschrift Light")
      btn_login.setFont(font)
    
    def login(self):
        """funcion donde se verificaran el user y password del empleado"""
        usuario = (str(self.lineEditUsuario.text()))

        self.contrasena = self.basedatos.obtenerUserandPassword(usuario)
        if(str(self.contrasena[0])== str(self.lineEditContrasenia.text())):
            QMessageBox.information(self, "Ingresar","Bienvenido a UMA")
            self.ingresar = Menu()
            self.close()
        else:
            QMessageBox.information(
                self, "Ingresar", "Verifique si su usuario o contraseña es correcto")
    

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    fuente.setBold(True)
    app.setFont(fuente)
    window = VentanaLogin()
    window.show()
    sys.exit(app.exec_())
           
           
    