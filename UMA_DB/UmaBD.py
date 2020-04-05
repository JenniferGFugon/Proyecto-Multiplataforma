import sqlite3
import sys

#Variables Globales
conn = sqlite3.connect('UMA_DB/uma')
micursor = conn.cursor()


class EmpleadoDB:
    """Crea la base de datos uma"""
        
    def Create_tables(self):
        """Creacion de todas las tablas de la base de datos"""
        conn
        #Tabla Productos
        micursor.execute("""CREATE TABLE IF NOT EXISTS Producto( 
                                                idProducto           INTENGER IDENTITY NOT NULL,
                                                idCategoriaProducto  INTENGER          NOT NULL,
                                                nombreProducto       TEXT(50)          NOT NULL
                                                        )
                    """)
        #tabla CategoriaProducto 
        micursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaProducto(
                                                idcategoria INTENGER IDENTITY         NOT NULL,
                                                idTipoProducto   INTENGER             NOT NULL,
                                                nombreCategoria  TEXT(50)             NOT NULL
                                                        )
                    """)
        #tabla Repuesto
        micursor.execute("""CREATE TABLE IF NOT EXISTS Repuesto(
                                            idRepuesto  INTEGER IDENTITY   NOT NULL,
                                            marca       TEXT(50)            NOT NULL,
                                            modelo      TEXT(50)            NOT NULL,
                                            fabricante  TEXT(50)            NOT NULL,
                                            existencia  INTENGER               NOT NULL,
                                            costoCompra NUMERIC(9,2)           NOT NULL,
                                            precioVenta NUMERIC(9,2)           NOT NULL         
                                            )
                     """)

        #tabla Empleado
        micursor.execute("""CREATE TABLE IF NOT EXIST Empleado (
                                            idEmpleado INTEGER IDENTITY NOT NULL,
                                            identidadEmpleado TEXT(15) NOT NULL,
                                            nombreEmpleado    TEXT(50) NOT NULL,
                                            TelefonoEmpleado  TEXT(9)  NOT NULL,
                                            celularEmpleado   TEXT(9)  NOT NULL,
                                            RTN               TEXT(15) NOT NULL,
                                            direccionEmpleado TEXT(100)NOT NULL,
                                            CorreoEmpleado    TEXT(100)NOT NULL,
                                            UserName          TEXT(10) NOT NULL,
                                            Pass             TEXT(10) NOT NULL
                                            )
                    """)
        #tabla Servicio 
        micursor.execute("""CREATE TABLE IF NOT EXIST Servicio (
                                            idServicio INTEGER IDENTITY NOT NULL,
                                            NombreServicio TEXT(50)     NOT NULL,
                                            PrecioVenta NUMERIC(9,2)    NOT NULL
                                            )
        
        
        
        
                    """)
        conn.close()

if __name__ == "__main__":
    Connect = connect()
    Connect.Create_tables()
