# coding=utf-8
"""
Contiene las funciones referentes a los clientes
"""
from xlrd import sheet
import conexion
import sqlite3
import funciones_excel
import variables

def limpiarentry(fila):
    """
    Limpia todos los datos introducidos en los entry

    :param fila: Datos a limpiar
    :return:     Void
    """
    try:
        variables.menslabel[1].set_text('')
        for i in range(len(fila)):
            fila[i].set_text('')
    except:
        print("Error")


def validoDNI(dni):
    """
    Funcion que comprueba que un dni sea valido

    :param dni: Dni a validar
    :return:    Boolean
    """
    try:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"  # letras del dni, es estandar
        dig_ext = "XYZ"
        # tabla letras extranjeroreemp_
        reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
        numeros = "1234567890"
        dni = dni.upper()
        if len(dni) == 9:  # el dni debe tener 9 caracteres
            dig_control = dni[8]
            dni = dni[:8]  # el numero que son los 8 primeros
            if dni[0] in dig_ext:
                print(dni)
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
        return False
    except:
        print("Error")
        return None


def insertarcli(fila):
    """
    Inserta un cliente en la base de datos

    :param fila:    Datos a insertar en la base de datos
    :return:        Void
    """
    try:
        conexion.cur.execute('insert into  clientes(dni,apel,nome, data) values(?,?,?,?)', fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


# select para utilizar en las operaciones de datos
def listar():
    """
    Actualiza el treeview

    :return:    Retorna los datos de la base de datos clientes
    """
    try:
        conexion.cur.execute('select * from clientes')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


# esta funcion da de baja un clieente
def bajacli(dni):
    """
    Da de baja un cliente con su dni

    :param dni: dni del cliente a eliminar en la base de datos
    :return: void
    """
    try:
        conexion.cur.execute('delete from clientes where dni = ?', (dni,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


# esta funcion modifica datos de clientes
def modifcli(registro, cod):
    """
    Modificar un cliente de la base de datos

    :param registro: lista de valores a modificar del cliente
    :param cod: Codigo del cliente a modificar
    :return: Void
    """
    try:
        conexion.cur.execute('update clientes set dni = ?, apel= ?, nome = ?, data = ? where id = ?',
                             (registro[0], registro[1], registro[2], registro[3], cod))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadocli(listclientes):
    """
    esta funcion carga el treeview con los datos de la tabla clientes

    :param listclientes: lista de los clientes de la base de datos
    :return: Void
    """
    try:
        variables.listado = listar()
        listclientes.clear()
        for registro in variables.listado:
            listclientes.append(registro[1:5])
    except:
        print("error en cargar treeview")


def selectcli(dni):
    """
    Buscar un cliente con su dni
    :param dni: dni del cliente que se usara para buscar
    :return: El resultado de la consulta
    """
    try:
        conexion.cur.execute('select id from clientes where dni = ?', (dni,))
        listado = conexion.cur.fetchone()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def apelnomfac(dni):
    """

    Busca el nombre y apellidos de un cliente con su dni
    :param dni: dni con el que se va a buscar al cliente
    :return: retorna los resultados de la consulta
    """
    try:
        conexion.cur.execute('select apel, nome from clientes where dni = ?', (dni,))
        listado = conexion.cur.fetchone()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def insertar_cliente_excel_BD(celdas_clientes):
    """
    Importa los clientes a traves de un excel

    :param celdas_clientes: Lista de cada celda de un cliente del excel
    :return:Void
    """
    cliente = []
    for celda_cliente in celdas_clientes:
        if celda_cliente.ctype == sheet.XL_CELL_DATE:
            cliente.append(funciones_excel.formatear_fecha_excel(celda_cliente))
        else:
            cliente.append(celda_cliente.value)
    insertarcli(cliente)
