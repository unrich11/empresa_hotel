# coding=utf-8
"""
Contiene las funciones referentes a las reservas
"""

import conexion
import sqlite3
import variables
from datetime import datetime

def limpiarentry(fila):
    """
    Vacia los entry que reciba

    :param fila:    lista de entrys a vaciar
    :return:        Void
    """

    for i in range(len(fila)):
        fila[i].set_text('')
    for i in range(len(variables.menslabel)):
        variables.menslabel[i].set_text('')
    variables.cmbhab.set_active(-1)

def calculardias():
    """
    Metodo que calcula cuantos dias dura la reserva

    :return:    Void
    """
    diain = variables.filareserva[2].get_text()
    date_in = datetime.strptime(diain, '%d/%m/%Y').date()
    diaout = variables.filareserva[3].get_text()
    date_out = datetime.strptime(diaout, '%d/%m/%Y').date()
    noches = (date_out-date_in).days
    if noches <= 0:
        variables.menslabel[2].set_text('Check-Out debe ser posterior')
        variables.reserva = 0
    else:
        variables.reserva = 1
        variables.menslabel[2].set_text(str(noches))

def insertares(fila):
    """
    Inserta una reserva en la base de datos

    :param fila:    Lista con los valores que se usaran para insertar la reserva
    :return:        Void
    """
    try:
        conexion.cur.execute('insert into  reservas(dni, numhab, checkin, checkout, noches) values(?,?,?,?,?)', fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadores(listreservas):
    """
    Actuliza el treeview de reservas

    :return:    Void
    """
    try:
        variables.listado = listares()

        variables.listreservas.clear()
        for registro in variables.listado:
            listreservas.append(registro)

    except sqlite3.OperationalError as e:
        print(e)
        print("error en listadores")
        conexion.conex.rollback()

def listares():
    """
    Busca todas las reservas

    :return:    Listado de todas las reservas de la base de datos
    """
    try:
        conexion.cur.execute('select codreser, dni, numhab, checkin, checkout, noches from reservas')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        print("Error en listares")
        conexion.conex.rollback()

def buscarapelcli(dni):
    """
    Busca un apellido de un cliente con su dni

    :param dni:     Dni del cliente a buscar
    :return:        Apellido del cliente encontrado
    """
    try:
        conexion.cur.execute('select apel from clientes where dni = ?', (dni,))
        apel = conexion.cur.fetchone()
        conexion.conex.commit()
        return apel
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarnome(dni):
    """
    Busca el nombre de un cliente a traves de su dni

    :param dni:     Dni del cliente a buscar el nombre
    :return:        Nome del cliente
    """
    try:
        conexion.cur.execute('select nome from clientes where dni = ?', (dni,))
        nome = conexion.cur.fetchone()
        conexion.conex.commit()
        return nome
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

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
'''''
def bajareserva(cod):
    try:
        print(cod)
        conexion.cur.execute('select numhab from reservas where codreser = ?', (cod,))
        conexion.conex.commit()
        if variables.switch.get_active():
            libre = 'SI'
        else:
            libre = 'NO'
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()
'''''

def versilibre(numhab):
    """
    Comprueba que una habitacion este libre

    :param numhab:  Numero de la habitacion a comprobar si esta libre
    :return:    Estado de la habitacion buscada
    """
    try:
        conexion.cur.execute('select libre from habitacion where numero = ?', (numhab,))
        lista= conexion.cur.fetchone()
        conexion.conex.commit()
        if lista[0] == 'SI':
            return True
        else:
            return False
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def numeroNoches(codigoReserva):
    """
    Busca el numero de noches de una reserva

    :param codigoReserva:  Codigo de reserva
    :return:    Numero de noches de la reserva
    """
    try:
        conexion.cur.execute('select noches from reservas where codreser=?',(codigoReserva,))
        lista= conexion.cur.fetchone()
        conexion.conex.commit()
        return lista[0]
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()