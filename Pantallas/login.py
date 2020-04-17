# -*- coding: utf8 -*-
# Programa: 
# Objetivo: 
# Autores: 
# Fecha: 

# Librerias

import sys
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class VentanaLogin(QWidget):
    """ Ventana de login para que el usuario ingrese al sistema """

    def __init__(self, parent=None):

      super(VentanaLogin, self).__init__(parent)
        
      self.setWindowTitle("LOGIN")
      self.setWindowIcon(QIcon("Logo.png"))
      self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
      self.setFixedSize(400, 380)
      #Color de fondo de la ventana
      paleta = QPalette()
      paleta.setColor(QPalette.Background, QColor(229, 25, 25))
      self.setPalette(paleta)

      self.UI()

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
      btn_login.clicked.connect(self.llamar_menu)
      font = QFont()
      font.setBold(True)
      font.setPointSize(10)
      font.setFamily("Bahnschrift Light")
      btn_login.setFont(font)
        
    def llamar_menu(self):
      self.call = self.Menu()
      self.close()

    def Login(self):
        
      usuario = self.lineEditUsuario.text()
      contrasenia = self.lineEditContrasenia.text()

      print("Usuario:", usuario)
      print("Contraseña:", contrasenia)

      self.lineEditUsuario.clear()
      self.lineEditContrasenia.clear()

if __name__ == '__main__':
        
  aplicacion = QApplication(sys.argv)

  ventana = VentanaLogin()
  ventana.show()
    
  sys.exit(aplicacion.exec_())
    