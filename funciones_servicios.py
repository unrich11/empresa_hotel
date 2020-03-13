# coding=utf-8
"""
Contiene las funciones referentes a los servicios
"""

import sqlite3
import conexion
import variables


def modificarPrecios(precios):
    """
    Modificar un cliente de la base de datos

    :param registro: lista de valores a modificar del cliente
    :param cod: Codigo del cliente a modificar
    :return: Void
    """
    try:
        conexion.cur.execute('update precios set precioDesayuno = ?, precioComida= ?, precioParking = ?',
                             (precios[0], precios[1], precios[2]))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def insertarServicio(fila):
    """
    Inserta un servicio a un cliente en la base de datos

    :param fila:    Datos para crear el servicio en la base de datos
    :return:        Void
    """
    try:
        conexion.cur.execute('insert into  servicios(codigoReservaServicio,concepto, precio) values(?,?,?)', fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def eliminarServicio(codigo):
    """
    Elimina un servicio a un cliente en la base de datos

    :param fila:    id del servicio a eliminar en la base de datos
    :return:        Void
    """
    try:
        conexion.cur.execute('delete from servicios where codigoServicio = ?', (codigo,))
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listar(codigoReserva):
    """
    Actualiza el treeview servicios

    :return:    Retorna los datos de la base de datos servicios
    """
    try:
        conexion.cur.execute('select codigoServicio,concepto,precio from servicios where codigoReservaServicio=?',(codigoReserva,))
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadoServicio(listServicios,codigoReserva):
    """
    esta funcion carga el treeview con los datos de la tabla servicios

    :param listservicios: lista de los servicios de la base de datos
    :return: Void
    """
    try:
        if(codigoReserva!=""):
            variables.listado = listar(codigoReserva)
            listServicios.clear()
            for registro in variables.listado:
                listServicios.append(registro)
    except Exception as e:
        print("error en cargar treeview servicios")
        print(e)

def limpiarEntry():

    """
    esta limpia la pestaña servicios

    :return: Void
    """
    try:
        variables.rbNinguno.set_active(True)
        variables.chkParking.set_active(False)
        variables.entTipoServicio.set_text("")
        variables.entPrecioServicio.set_text("")
    except Exception as e:
        print("error en cargar treeview servicios")
        print(e)


