import sqlite3

conn = sqlite3.connect('UMA_DB/uma')

miCursor = conn.cursor()
miCursor.execute("""CREATE TABLE IF NOT EXISTS Producto( idProducto           INT IDENTITY    NOT NULL,
                                                        idCategoriaProducto  INT             NOT NULL,
                                                        nombreProducto       NVARCHAR(50)        NOT NULL
                                                        )
                    """)
miCursor.execute("""CREATE TABLE IF NOT EXISTS Producto( idProducto           INT IDENTITY    NOT NULL,
                                                        idCategoriaProducto  INT             NOT NULL,
                                                        nombreProducto       NVARCHAR(50)        NOT NULL
                                                        )
                    """)
miCursor.execute("""CREATE TABLE IF NOT EXISTS CategoriaProducto(idcategoria     INT IDENTITY    NOT NULL,
                                                                idTipoProducto  INT             NOT NULL,
                                                                nombreProducto  NVARCHAR(50)    NOT NULL
                                                                )
                    """)
miCursor.execute("""CREATE TABLE IF NOT EXISTS Repuesto(idRepuesto  INT IDENTITY  NOT NULL,
                                                       marca       NVARCHAR(50)  NOT NULL,
                                                       modelo      NVARCHAR(50)  NOT NULL,
                                                       fabricante  NVARCHAR(50)  NOT NULL,
                                                       existencia  INT           NOT NULL,
                                                       costoCompra DECIMAL(9,2)  NOT NULL,
                                                       precioVenta DECIMAL(9,2)  NOT NULL         
                                                       )
                     """)
conn.close()