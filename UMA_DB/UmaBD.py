import sqlite3
import sys

#Variables Globales
conn = sqlite3.connect('UMA_DB/uma')
micursor = conn.cursor()


class connect:
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
                                            idRepuesto  INTEGER INDENTITY   NOT NULL,
                                            marca       TEXT(50)            NOT NULL,
                                            modelo      TEXT(50)            NOT NULL,
                                            fabricante  TEXT(50)            NOT NULL,
                                            existencia  INTENGER               NOT NULL,
                                            costoCompra NUMERIC(9,2)           NOT NULL,
                                            precioVenta NUMERIC(9,2)           NOT NULL         
                                            )
                     """)
        conn.close()

if __name__ == "__main__":
    Connect = connect()
    Connect.Create_tables()
