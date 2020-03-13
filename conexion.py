import os, sqlite3

class Conexion:
    def abrirbbdd(self):
        """
        Abre la base de datos

        :return:    Void
        """
        try:
            global bbdd, conex, cur
            bbdd = 'empresa.sqlite'         #variable que almacena la base de datos
            conex = sqlite3.connect(bbdd)   #la abrimos
            cur = conex.cursor()            #la variable cursor que hara las operaciones
            print("Conexion realizada correctamente")
        except sqlite3.OperationalError as e:
            print("Error al abrir: ", e)
            return False

    def cerrarbbdd(self):
        """
        Cierra la base de datos

        :return:    Void
        """
        try:
            cur.close()
            conex.close()
            print("Base de datos cerrada correctamente ")

        except sqlite3.OperationalError as e:
            print("Error al cerrar: ", e)

