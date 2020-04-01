from PyQt5.QtGui import QPixmap, QFont
import sys
import os
import sqlite3
from sqlite3 import Error


class ventaDB:
    '''Base de datos para la venta '''

    def __init__(self, UMA):
        """ Inicializador de la clase """
        self.connection = self.create_connection(UMA)
        self.venta_query = """ CREATE TABLE IF NOT EXISTS venta (
                                    id_venta integer PRIMARY KEY,
                                    id_cliente integer NOT NULL,
                                    id_empleado integer NOT NULL,
                                    fechaHora numeric NOT NULL,
                                    isv numeric NOT NULL,
                                    descuento numeric,
                                    total numeric
                                  );
                                """
        self.create_table(self.connection, self.venta_query)


    def create_connection(self, UMA):
        """ Crear una conexión a la base de datos SQLite """
        conn = None

        # Tratar de conectarse con SQLite y crear la base de datos
        try:
            conn = sqlite3.connect(UMA)
            print("Conexión realizada. Versión {}".format(sqlite3.version))
        except Error as e:
            print(e)
        finally:
            return conn

    def create_table(self, conn, query):
        """
        Crea una tabla basado en los valores de query.
        :param conn: Conexión con la base de datos.
        :param query: La instrucción CREATE TABLE.
        :return:
        """
        try:
            cursor = conn.cursor()
            cursor.execute(query)
        except Error as e:
            print(e)        

    #def add_venta(self, venta):
            """
        #Realiza una inserción a la tabla de ventas.
        
        
        #"""
        #sqlInsert = """ INSERT INTO venta(
                            #identidad, nombre, telefono, email,
                            #direccion, imagen)
                        #VALUES(?, ?, ?, ?, ?, ?) """

        #try:
         #   cursor = self.connection.cursor()
          #  cursor.execute(sqlInsert, employee)
        #except Error as e:
         #   print(e)



#def main():
    #app = QApplication(sys.argv)
    
    #window = Main()
    #sys.exit(app.exec_())


#if __name__ == "__main__":
#    main()
