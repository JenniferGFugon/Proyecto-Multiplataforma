import sqlite3
import sys
import os
from sqlite3 import Error




class VentaDB:
    """ Base de datos SQLite para los empleados. """

    
    def __init__(self, db_filename):
        """ Inicializador de la clase """
        #Ejecutar los query de creacion de tablas
        self.connection = self.create_connection(db_filename)
        self.queryTabla(self.connection)
        self.queryTablaDetalle(self.connection)
        self.queryTablaProducto(self.connection)
        self.queryTablaEmpleado(self.connection)

    #--------------------CREACION DE TABLAS---------------
    #--------------------TABLA VENTA----------------------
    def queryTabla(self,conexión):

        self.venta_query = """ CREATE TABLE IF NOT EXISTS venta (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    id_cliente integer NOT NULL,
                                    id_empleado integer NOT NULL,
                                    total numeric NOT NULL 
                                  );
                                """
        self.create_Table(conexión, self.venta_query)   


    #----------------------TABLA DETALLE-----------------------
    def queryTablaDetalle(self,conexión):
        self.detalle_query = """ CREATE TABLE IF NOT EXISTS detalle (
                                    id_detalle integer PRIMARY KEY AUTOINCREMENT,
                                    id_venta integer NOT NULL,
                                    id_producto integer NOT NULL,
                                    cantidad integer NOT NULL,
                                    precio numeric NOT NULL,
                                    subtotal numeric NOT NULL,
                                    descuento numeric NOT NULL,
                                    isv numeric NOT NULL
                                  );
                                """
        self.create_Table(conexión, self.detalle_query)         

    #---------------------TABLA PRODUCTO-------------------------
    def queryTablaProducto(self,conexión):
        self.producto_query ="""CREATE TABLE IF NOT EXISTS producto ( 
                                    idProducto  integer PRIMARY KEY AUTOINCREMENT,
                                    idCategoriaProducto  integer  NOT NULL,
                                    nombreProducto  text NOT NULL,
                                    precioCompra numeric NOT NULL ,
                                    precioVenta numeric NOT NULL,
                                    cantidad numeric NOT NULL
                                  );
                                """
        self.create_Table(conexión, self.producto_query)         



    #--------------------TABLA EMPLEADO-----------------------------
    def queryTablaEmpleado(self,conexión):
        self.empleado_query = """  CREATE TABLE IF NOT EXISTS empleado (
                                            idEmpleado INTEGER PRIMARY KEY AUTOINCREMENT,
                                            identidadEmpleado TEXT  NOT NULL,
                                            nombreEmpleado    TEXT NOT NULL,
                                            telefonoEmpleado  TEXT  NOT NULL,
                                            direccionEmpleado TEXT NOT NULL,
                                            CorreoEmpleado    TEXT NOT NULL,
                                            userName          TEXT NOT NULL,
                                            pass             TEXT NOT NULL
                                            );
                                            """
        self.create_Table(conexión, self.empleado_query) 

    #-------------------INSERCION EN TABLAS -----------------------
    #-----------------------EMPLEADO-----------------------------
    
    def add_empleado(self, empleado):
        """
        Realiza una inserción a la tabla de empleados.
        :param employee: Una estructura que contiene
                         los datos del empleado.
        :return:
        """
        sqlInsert = """
                    INSERT INTO empleado(
                        identidadEmpleado, nombreEmpleado, telefonoEmpleado,
                        direccionEmpleado,CorreoEmpleado,userName,pass)
                    VALUES(?,?,?,?,?,?,?)    
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert,empleado)
            self.connection.commit()
        except Error as e:
            print(e)

    #------------------ELIMINACION EN TABLAS-----------------
    #------------------TABLA EMPLEADOS----------------------
    def eliminar_empleado(self, id):
        """
        Elimina un empleado mediante el valor de la identidad.

        param: id: El valor del registro del empleado.
        :return: True si el empleado se eliminó. None en caso contrario.
        """
        sqlQuery = "DELETE FROM empleado WHERE idEmpleado =  ? ; "

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id,))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None

    #---------------OBTENCION DE DATOS DE LAS TABLAS---------
    #------------------TABLA EMPLEADOS-----------------------
    def obtenerEmpleados(self):
        """ Obtiene todas las tuplas de la tabla empleado """
        sqlQuery = " SELECT *FROM empleado ORDER BY ROWID ASC "

        try:
            cursor = self.connection.cursor()
            empleados = cursor.execute(sqlQuery).fetchall()

            return empleados
        except Error as e:
            print(e)

        return None


    #------------------MODIFICACION DE TABLAS---------------
    #---------------------TABLA EMPLEADOS-------------------
    def modificarEmpleadoPorId(self,empleado):
        '''Modifica datos del empleado
        Parametros : id  del cliente del cual se modificaran 
        los datos'''
        sqlQuery = """update empleado
                        SET nombreEmpleado =?,
                        identidadEmpleado =?,
                        telefonoEmpleado = ?,
                        direccionEmpleado = ?,
                        correoEmpleado = ?,
                        userName = ?,
                        pass = ?
                        WHERE idEmpleado = ?;"""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery,empleado)
            self.connection.commit()
        except Error as e:
            print(e)            


    def obtenerEmpleadosPorId(self, id):
        """
        Busca un empleado mediante el valor de la identidad.

        param: id: El valor del id del empleado.
        :return: Un arreglo con los atributos del empleado.
        """
        sqlQuery = " SELECT *FROM empleado WHERE idEmpleado =  ? ;"

        try:
            cursor = self.connection.cursor()
            empleado = cursor.execute(sqlQuery, (id,)).fetchone()

            return empleado
        except Error as e:
            print(e)

        return None    


    def create_Table(self, connexion, query):
        """
        Crea una tabla basado en los valores de query.
        :param conn: Conexión con la base de datos.
        :param query: La instrucción CREATE TABLE.
        :return:
        """
        try:
            cursor = connexion.cursor()
            cursor.execute(query)
        except Error as e:
            print(e)


    def create_connection(self, db_name):
        """ Crear una conexión a la base de datos SQLite """
        connexion = None

        
        try:
            connexion = sqlite3.connect(db_name)
            print("Conexión realizada. Versión {}".format(sqlite3.version))
        except Error as e:
            print(e)
        finally:
            return connexion





