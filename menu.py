
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
    #------------------------------Pantalla Agregar Inventario---------------------------------
    

    #------------------------------------------------------------------------------------------

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


    def agregar_cliente(self):
        """Manda a llamar la pantalla agregar cliente """
        self.llamar = AgregarCliente()

    
    def modificar_cliente(self):
        """Manda a llamar la pantalla modificar cliente"""
        self.modificar = ModificarCliente()

    
    def cargarDatosAModificar(self):
        """Carga los datos que seran modificados por el usuario"""
        global id
        if self.lista_clientes.selectedItems():
            cliente = self.lista_clientes.currentItem().text()
            id =  cliente.split(" -- ")[0]
            self.ModificarCliente()
        else:
            QMessageBox.information(self,"Informacion","No selecciono ningun cliente")  


    def botonesCliente(self):
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
        self.top_layout.addWidget(self.encabezadoCliente())
        self.setLayout(self.main_layout)

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
        btn_guardar_cliente.clicked.connect(self.insertarCliente)

        btn_menu = QPushButton("Menu Principal", self)
        btn_menu.setFixedWidth(135)
        btn_menu.setFixedHeight(28)
        btn_menu.move(415, 510)
        btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        btn_menu.setFont(fuente)     


    def llamar_cliente(self):
        """Llamando la ventana de cliente"""
        self.cliente = VentanaCliente()
        self.close()

    def insertarCliente(self):
        """ Insertar los valores del formulario a la tabla de cliente """
        # Verificar si los valores requeridos fueron agregados
        if (self.input_nombre_cliente.text() or self.input_id_cliente.text() or
                self.input_telefono_cliente.text() or self.input_celular_cliente.text() or
                self.input_rtn_cliente.text() or self.input_direccion_cliente.text() or
                self.input_correo_cliente.text() != ""):
            cliente = (str(self.input_id_cliente.text()), str(self.input_nombre_cliente.text()),
                        str(self.input_telefono_cliente.text()) , str(self.input_celular_cliente.text()),
                        str(self.input_direccion_cliente.text()) ,  str(self.input_correo_cliente.text()),
                        str(self.input_rtn_cliente.text()))

            try:
                self.basedatos.add_cliente(cliente)
                QMessageBox.information(
                    self, "Guardar", "Cliente agregado correctamente")
                self.close()
                
                self.llamar_cliente()
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

    ###########################################
    def GestionarEmpleado(self):
        self.gestionarEmpleado = AgregarEmpleado()
        self.close()
####################################################

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

    ########################################################################
    def llenar_lista_empleado(self):
        """ Obtiene las tuplas de empleados y las muestra en la lista """
        empleados = self.basedatos.obtenerEmpleados()

        if empleados:
            for empleado in empleados:
                self.lista_empleados.addItem(
                    "{0} -- {1} -- {2} -- {3} -- {4} -- {5} -- {6} -- {7}"
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
                question_text = f"¿Está seguro de eliminar el empleado {empleado[0]}?"
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
##############################################################################################


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
        self.btn_menu = QPushButton("Cancelar")
        
        self.btn_menu.setFixedWidth(135)
        self.btn_menu.setFixedHeight(28)
        self.btn_menu.move(415, 580)
        self.btn_menu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: \'white\';")
        #self.btn_menu.clicked.connect(self.llamar_menu)
        self.btn_menu.setFont(self.fuente)
        
        
#######################################################################
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

    ###################################################################
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
    ############################################################################

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
           
           
    