# coding=utf-8
"""
Aquí vendrán todas las funciones que afectan a la ¡gestión de los
habitaciones
"""

import conexion, sqlite3, variables

def insertarhab(fila):
    """
    Insrtar una habitacion

    :param fila:    valores para la habitacion a insertar
    :return:        Void
    """
    try:
        conexion.cur.execute('insert into habitacion(numero,tipo,prezo,libre) values(?,?,?,?)', fila)
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listarhab():
    """
    Coge todas las habitaciones de la base de datos

    :return: el listado con las habitaciones
    """
    try:
        conexion.cur.execute('select * from habitacion')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def limpiarentry(fila):
    """
    Vacia los entry que le pasas

    :param fila:    entry a limpiar
    :return:        Void
    """
    for i in range(len(fila)):
        fila[i].set_text('')
    variables.filarbt[1].set_active(True)

def listadohab(listhab):
    """
    Carga el treeview habitaciones

    :param listhab:     Listado de habitaciones a cargar
    :return:            Void
    """
    try:
        variables.listado = listarhab()
        variables.listhab.clear()
        for registro in variables.listado:
            listhab.append(registro)
    except:
        print("error en cargar treeview de hab")
def buscarpreciohabitacion(numhabitacion):
    """
    Busca el precio de una habitacion a traves del numero de la habitacion

    :param numhabitacion:   Numero de la habitacion a buscar el precio
    :return:                Void
    """
    try:
        conexion.cur.execute('select prezo from habitacion where numero = ?', (numhabitacion,))
        precio = conexion.cur.fetchone()
        conexion.conex.commit()
        return precio

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def bajahab(numhab):
    """
    Da de baja una habitacion con su numero

    :param numhab:      Numero de la habitacion a eliminar
    :return:            Void
    """
    try:
        conexion.cur.execute('delete from habitacion where numero = ?', (numhab,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def modifhab(registro, numhab):
    """
    Modifica una habitacion

    :param registro:    Nuevos valores para la habitacion a modificar
    :param numhab:      Numero de la habitacion a modificar
    :return:            Void
    """
    try:
        conexion.cur.execute('update habitacion set tipo = ?, prezo = ?, libre = ? where numero = ?',
                             (registro[1], registro[0], registro[2], numhab))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadonumhab(self):
    """
    Pone los numeros de las habitaciones en una variable para que en el combobox

    :return:    Void
    """
    try:
        conexion.cur.execute('select numero from habitacion')
        listado = conexion.cur.fetchall()
        variables.listcmbhab.clear()
        for row in listado:
            variables.listcmbhab.append(row)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadonumhabres():
    """
    Busca los numeros de las habitaciones

    :return:    Listado con todos los numeros de las habitaciones
    """
    try:
        conexion.cur.execute('select numero from habitacion')
        lista = conexion.cur.fetchall()
        return lista
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def cambiaestadohab(libre, numhabres):
    """
    Cambia el estado de una habitacion

    :param libre:       Dice SI or NO dependiendo de si esta libre o no la habitacion
    :param numhabres:   Numero de la habitacion en la que se va a cambiar el estado
    :return:            Void
    """
    try:
        print(libre)
        conexion.cur.execute('update habitacion set libre = ? where numero = ?',
                             (libre, numhabres))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
       print(e)
       conexion.conex.rollback()