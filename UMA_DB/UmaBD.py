import sqlite3

conn = sqlite3.connect('UMA.db')
import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_tables(con):

    cursorObj = con.cursor()

    cursorObj.execute("""CREATE TABLE IF NOT EXISTS Producto( idProducto           INT IDENTITY    NOT NULL,
                                                        idCategoriaProducto  INT             NOT NULL,
                                                        nombreProducto       NVARCHAR(50)        NOT NULL
                                                        )
                    """)
        
    cursorObj.execute("""CREATE TABLE IF NOT EXISTS CategoriaProducto(idcategoria     INT IDENTITY    NOT NULL,
                                                                idTipoProducto  INT             NOT NULL,
                                                                nombreProducto  NVARCHAR(50)    NOT NULL
                                                                )
                    """)
    cursorObj.execute("""CREATE TABLE IF NOT EXISTS Repuesto(idRepuesto  INT IDENTITY  NOT NULL,
                                                       marca       NVARCHAR(50)  NOT NULL,
                                                       modelo      NVARCHAR(50)  NOT NULL,
                                                       fabricante  NVARCHAR(50)  NOT NULL,
                                                       existencia  INT           NOT NULL,
                                                       costoCompra DECIMAL(9,2)  NOT NULL,
                                                       precioVenta DECIMAL(9,2)  NOT NULL         
                                                       )
                     """)
    con.commit()

con = sql_connection()

sql_tables(con)