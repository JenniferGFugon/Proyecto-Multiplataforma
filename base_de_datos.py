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
        self.queryTablaServicio(self.connection)
        self.queryTablaCliente(self.connection)
        self.queryCategoria(self.connection)

    #--------------------CREACION DE TABLAS---------------
    #--------------------TABLA VENTA----------------------
    def queryTabla(self,conexión):

        self.venta_query = """ CREATE TABLE IF NOT EXISTS venta(
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    cliente text NOT NULL,
                                    empleado text NOT NULL,
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
    def  queryTablaProducto ( self , conexión ):
        self.producto_query  = """CREATE TABLE IF NOT EXISTS producto (
                                    idProducto integer PRIMARY KEY AUTOINCREMENT,
                                    CategoriaProducto text NOT NULL,
                                    nombreProducto text NOT NULL,
                                    precioCompra NUMERIC NO NULL,
                                    precioVenta NUMERIC NO NULL,
                                    cantidad NUMERIC NO NULL"""
        self.create_Table(conexión, self.producto_query)         
                            

    #------------------------TABLA CATEGORIA---------------------------------
    def queryCategoria(self,conexión):                                
        self.categoria_query ="""CREATE TABLE IF NOT EXISTS Categoria( 
                                    idCategoria  integer PRIMARY KEY AUTOINCREMENT,
                                    nombreCategoriaProducto  text  NOT NULL
                                  );
                                """
  
        self.create_Table(conexión, self.categoria_query)         
    
   
    
    

    #---------------------Tabla Productos Varios------------------------------------
    def queryTablaProductosVarios(self, conexión):
        self.producto_query="""CREATE TABLE IF NOT EXISTS productosVarios ( 
                                    idProductoVario integer PRIMARY KEY AUTOINCREMENT,
                                    NombreProducto   TEXT  NOT NULL,
                                    marca   TEXT  NOT NULL,
                                    existencia   integer  NOT NULL,
                                    precioVenta  numeric  NOT NULL,
                                    precioCompra  numeric NOT NULL);
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
    
    #---------------------TABLA SERVICIO------------------------------------
    def queryTablaServicio(self,conexión): 
        self.servicio_query = """CREATE TABLE IF NOT EXISTS servicio (
                                            idServicio INTEGER  PRIMARY KEY AUTOINCREMENT,
                                            
                                            NombreServicio TEXT     NOT NULL,
                                            PrecioVenta NUMERIC    NOT NULL
                                            );
                                            """

        self.create_Table(conexión, self.servicio_query) 

    #-----------------------------Tabla cliente---------------------------------------------
    def queryTablaCliente(self,conexión):
        self.cliente = """CREATE TABLE IF NOT EXISTS Cliente (
                                            idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
                                            identidadCliente TEXT    NOT NULL,
                                            nombreCliente TEXT       NOT NULL,
                                            numeroTelefonico TEXT    NOT NULL,
                                            numeroCelular TEXT       NOT NULL,
                                            RTN TEXT                 NOT NULL,
                                            direccionCliente TEXT    NOT NULL,
                                            correoElectronico TEXT   NOT NULL
                                            );
                                            """

        self.create_Table(conexión, self.cliente) 

    #--------------------------------Tabla TipoCliente--------------------------------------
    

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

    #------------------------SERVICIO--------------------------------
    def add_servicio(self, servicio):
        """
        Realiza una inserción a la tabla de servicio.
        """
        sqlInsert = """
                    INSERT INTO servicio(
                        idServicio,NombreServicio,PrecioVenta
                    )
                    VALUES(?,?,?)    
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert,servicio)
            self.connection.commit()
        except Error as e:
            print(e)

    #----------------------- CLIENTE -----------------------------------
    def add_cliente(self, cliente):
        """
        Realiza una inserción a la tabla de servicio.
        """
        sqlInsert = """
                    INSERT INTO Cliente(
                        identidadCliente,nombreCliente,numeroTelefonico,
                        numeroCelular, RTN, direccionCliente, correoElectronico
                    )
                    VALUES(?,?,?,?,?,?,?)    
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert,cliente)
            self.connection.commit()
        except Error as e:
            print(e)

    #------------------------ TIPO CLIENTE ----------------------------
    def add_tipoCliente(self, TipoCliente):
        """
        Realiza una inserción a la tabla de servicio.
        """
        sqlInsert = """
                    INSERT INTO TipoCliente(
                        idTipoCliente,TipoCliente
                    )
                    VALUES(?,?)    
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert, TipoCliente)
            self.connection.commit()
        except Error as e:
            print(e)

    #------------------TABLA PRODUCTO----------------------
    def add_producto(self, TablaProducto):
        """ Realiza una inserción a la tabla de producto. """
        sqlInsert = """
                    INSERT INTO Producto(
                        CategoriaProducto,
                        NombreProducto, PrecioCompra,
                        PrecioVenta, Cantidad
                    
                    )
                    VALUES(?,?,?,?,?)    
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert, TablaProducto)
            self.connection.commit()
        except Error as e:
            print(e)


    #------------------ELIMINACION EN TABLAS-----------------
    #------------------TABLA Producto----------------------
    def eliminar_Producto(self, id):
        """
        Elimina un producto mediante el valor de la idProducto.

        param: id: El valor del registro del producto.
        :return: True si el producto se eliminó. None en caso contrario.
        """
        sqlQuery = "DELETE FROM producto WHERE idProducto =  ? ; "

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id ,))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None



    #------------------VENTA----------------------
    def add_venta(self, venta):
        """ Realiza una inserción a la tabla de Venta. """
        sqlInsert = """
                    insert into venta( cliente,empleado,total) 
                    values(?,?,?);
                     
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert, venta)
            self.connection.commit()
        except Error as e:
            print(e)  
            
    #------------------DETALLE----------------------
    def add_detalle(self, detalle):
        """ Realiza una inserción a la tabla de Detalle. """
        sqlInsert = """
                    insert into detalle( id_venta,id_producto,cantidad,
                    precio,subtotal,descuento,isv)
                    values(?,?,?,?,?,?,?);
                     
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert, detalle)
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

    #-------------------- TABLA SERVICIO ----------------------------------
    def eliminar_servicio(self, id):
        """
        Elimina un empleado mediante el valor de la identidad.

        param: id: El valor del registro de servicio.
        :return: True si servico se eliminó. None en caso contrario.
        """
        sqlQuery = "DELETE FROM Servicio WHERE idServicio =  ? ; "

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None
    #----------------------- CLIENTE --------------------------------------
    def eliminar_cliente(self, id):
        """
        Elimina un cliente mediante el valor de la identidad.

        param: id: El valor del registro del cliente.
        :return: True si el empleado se eliminó. None en caso contrario.
        """
        sqlQuery = "DELETE FROM Cliente WHERE idCliente =  ? ; "

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id,))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None

    #----------------------- Tipo Cliente -----------------------------------
    def eliminar_tipoCliente(self, id):
        """
        Elimina un tipoCliente mediante el valor de la identidad.

        param: id: El valor del registro del tipo cliente.
        :return: True si el empleado se eliminó. None en caso contrario.
        """
        sqlQuery = "DELETE FROM TipoCliente WHERE idTipoCliente =  ? ; "

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None


    def eliminar_venta(self, id):
        """
        Elimina una venta seleccionada .

        param: id: El del id de la venta.
        :return: True si la venta  se eliminó. None en caso contrario.
        """
        sqlQuery = "DELETE FROM detalle WHERE id_venta =  ? ; "
        sqlQuery2 = "DELETE FROM venta WHERE id =  ?;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id,))
            cursor.execute(sqlQuery2, (id,))

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

    #--------------------- SERVICIO -------------------------------
    def obtenerServicio(self):
        """ Obtiene todas las tuplas de la tabla servicio """
        sqlQuery = " SELECT *FROM Servicio ORDER BY ROWID ASC "

        try:
            cursor = self.connection.cursor()
            servicios = cursor.execute(sqlQuery).fetchall()

            return servicios
        except Error as e:
            print(e)


    def obtenerCategoria(self):
        """ Obtiene todas las tuplas de la tabla Categoria """
        sqlQuery = " SELECT nombreCategoriaProducto FROM Categoria ORDER BY ROWID ASC "

        try:
            cursor = self.connection.cursor()
            clientes = cursor.execute(sqlQuery).fetchall()

            return clientes
        except Error as e:
            print(e)


    #----------------------- CLIENTE----------------------------------
    def obtenerCliente(self):
        """ Obtiene todas las tuplas de la tabla Cliente """
        sqlQuery = " SELECT *FROM Cliente ORDER BY ROWID ASC "

        try:
            cursor = self.connection.cursor()
            clientes = cursor.execute(sqlQuery).fetchall()

            return clientes
        except Error as e:
            print(e)

    #------------------------ TIPO CLIENTE -----------------------------
    def obtenerTipoCliente(self):

        """ Obtiene todas las tuplas de la tabla servicio """

        """Obtiene todas las tuplas de la tabla servicio """

        """Obtiene todas las tuplas de la tabla servicio """
        sqlQuery = " SELECT *FROM TipoCliente ORDER BY ROWID ASC "
        
        try:
            cursor = self.connection.cursor()
            TipoClientes = cursor.execute(sqlQuery).fetchall()
            return TipoClientes
        except Error as e:
            print(e)

    #------------------------VENTA-------------------------
    def obtenerVenta(self):
        '''Obtiene el numero de la venta'''
        sqlQuery = 'SELECT max(id) FROM venta ; '
        try:
            cursor = self.connection.cursor()
            ventas = cursor.execute(sqlQuery).fetchone()
            return ventas
        except Error as e:
            print(e)
    #-----------------VENTA----------------------------
    def obtenerVentaPorId(self,id):
        '''Obtiene el numero de la venta'''
        sqlQuery = 'SELECT * FROM venta where id = ? ; '
        try:
            cursor = self.connection.cursor()
            ventas = cursor.execute(sqlQuery,(id,)).fetchone()
            return ventas
        except Error as e:
            print(e)        

    #----------------------DETALLE DE VENTA -----------------
    def obtenerDetalleVenta(self,id):
        '''Obtiene el numero de la venta'''
        sqlQuery = 'SELECT * FROM detalle where id_venta = ? ; '
        try:
            cursor = self.connection.cursor()
            detalle = cursor.execute(sqlQuery,(id,)).fetchall()
            return detalle
        except Error as e:
            print(e)        
    
    #----------------------VENTA-----------------------------
    def obtenerTablaVenta(self):
        '''Obtiene los campos de la tabla venta'''
        sqlQuery = 'SELECT * FROM venta ; '
        try:
            cursor = self.connection.cursor()
            ventas = cursor.execute(sqlQuery).fetchall()
            return ventas
        except Error as e:
            print(e)        

    #----------------------PRODUCTO------------------------
    def ObtenerNombreProductos(self):
        '''Obtiene el nombre de los productos 
        para cargarlos en un ComboBox'''
        sqlQuery = '''SELECT nombreProducto FROM producto ;'''
        try:
            cursor = self.connection.cursor()
            productos = cursor.execute(sqlQuery).fetchall()
            return productos
        except Error as e:
            print(e) 

    #-----------------------CLIENTES---------------------
    def ObtenerNombreClientes(self):
        '''Obtiene el nombre de los clientes
        para cargarlos en un ComboBox'''
        sqlQuery = "SELECT nombreCliente FROM cliente ;"
        try:
            cursor = self.connection.cursor()
            productos = cursor.execute(sqlQuery).fetchall()
            return productos
        except Error as e:
            print(e) 

    #-----------------EMPLEADOS------------------------
    def ObtenerNombreEmpleados(self):
        '''Obtiene el nombre de los empleados
        para cargarlos en un ComboBox'''
        sqlQuery = "SELECT nombreEmpleado FROM empleado ;"
        try:
            cursor = self.connection.cursor()
            productos = cursor.execute(sqlQuery).fetchall()
            return productos
        except Error as e:
            print(e)                 

    #----------------------PRODUCTO----------------------
    def ObtenerProducto(self,id):
        '''Obtiene los productos 
        Parametros : id valor '''
        sqlQuery = ''' SELECT idProducto,CategoriaProducto, nombreProducto ,precioVenta
                        FROM producto where nombreProducto = ?;'''
        try:
            cursor = self.connection.cursor()
            producto = cursor.execute(sqlQuery,(id,)).fetchall()
            return producto
        except Error as e:
            print(e)       

    #---------------------Obtener Producto-------------------
    def obtenerProducto(self):
        """ Obtiene todas las tuplas de la tabla Producto """
        sqlQuery = " SELECT *FROM producto ORDER BY ROWID ASC "

        try:
            cursor = self.connection.cursor()
            producto = cursor.execute(sqlQuery).fetchall()

            return producto
        except Error as e:
            print(e)

        return None

    #------------------MODIFICACION DE TABLAS---------------
    #---------------------TABLA Producto-------------------
    def modificarProductoPorId(self, producto):
        '''Modifica datos del empleado
        Parametros : id  del prodcuto del cual se modificaran 
        los datos'''
        sqlQuery = """update producto
                        SET CategoriaProducto =?,
                        nombreProducto =?,
                        precioCompra =?,
                        precioVenta =?,
                        cantidad =?
                        WHERE idProducto = ?;"""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery,producto)
            self.connection.commit()
        except Error as e:
            print(e)    



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

    #---------------------TABLA CLIENTE----------------       
    def modificarClientePorId(self,cliente):
        '''Modifica datos del cliente
        Parametros : id  del cliente del cual se modificaran 
        los datos'''
        sqlQuery = """  update cliente
                        SET 
                        identidadCliente =?,
                        nombreCliente =?,
                        numeroTelefonico = ?,
                        numeroCelular = ?,
                        RTN = ?,
                        direccionCliente = ?,
                        correoElectronico = ?
                        WHERE idCliente = ?;"""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery,cliente)
            self.connection.commit()
        except Error as e:
            print(e)                    
     
            print(e)    
            
    #------------------PRODUCTO--------------------
    def obtenerProductoPorId(self, id):
        """
        Busca un producto mediante el valor de id.

        param: id: El valor del id del producto.
        :return: Un arreglo con los atributos del producto.
        """
        sqlQuery = " SELECT *FROM producto WHERE idProducto = ? ;"

        try:
            cursor = self.connection.cursor()
            producto = cursor.execute(sqlQuery, (id,)).fetchone()

            return producto
        except Error as e:
            print(e)

        return None     

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

    def obtenerUserandPassword(self, nameUser):
        """
        Buscara entre todos los empleados el empleado que contenga el 
        Parametro
        Nameuser = donde se encuentre el nombre usuario traera 
        la contraseñan(pass)
        """

        sqlQuery = "SELECT pass from empleado WHERE userName = ? " 

        try:
            cursor = self.connection.cursor()
            empleado = cursor.execute(sqlQuery, (nameUser,)).fetchone()

            return empleado
        except Error as e:
            print(e)

        return None  


    def obtenerClientesPorId(self, id):
        """        Busca un cliente mediante el valor del id.

        param: id: El valor del id del empleado.
        :return: Un arreglo con los atributos del empleado."""
        
        sqlQuery = " SELECT *FROM Cliente WHERE idCliente =  ? ;"

        try:
            cursor = self.connection.cursor()
            cliente = cursor.execute(sqlQuery, (id,)).fetchone()

            return cliente
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





