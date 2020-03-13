
# coding=utf-8
"""
Contiene las funciones referentes a las funciones de las facturas
"""

import sqlite3
import conexion
import funcionesreser
import variables



def listar(codigoReserva):
    """
    Actualiza el treeview servicios

    :return:    Retorna los datos de la base de datos servicios
    """
    try:
        conexion.cur.execute('select concepto,precio from servicios where codigoReservaServicio=?',(codigoReserva,))
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadoServicios(listFactura,codigoReserva,numeroHabitacion):
    """
    esta funcion carga el treeview con los datos de la tabla servicios

    :param listFactura: lista de los servicios de la base de datos
    :return: Void
    """
    try:
        numeroHabitacion=int(numeroHabitacion)
        if(codigoReserva!=""):
            variables.listado = listar(codigoReserva)
            numeroNoches= funcionesreser.numeroNoches(codigoReserva)
            precioNoche=funcionesreser.buscarpreciohabitacion(numeroHabitacion)
            listFactura.clear()
            listFactura.append(["Noches",numeroNoches,precioNoche[0],(float(precioNoche[0])*float(numeroNoches))])
            for registro in variables.listado:
                listFactura.append([registro[0],"",registro[1],(float(numeroNoches)*registro[1])])
    except Exception as e:
        print("error en cargar treeview servicios de una factura")
        print(e)

def calcularPreciosServicios():
    """
    esta funcion carga el treeview con los datos de la tabla servicios

    :param listFactura: lista de los servicios de la base de datos
    :return: Void
    """
    try:
        preciosSinIva=0
        iva=0
        for registro in variables.listFactura:
            preciosSinIva= preciosSinIva + registro[3]
        for registro in variables.listFactura:
            if registro[0] =="Noches" or registro[0] =="Desayuno" or registro[0] =="Comida" or registro[0] =="Parking" :
                iva= iva+registro[3]*0.10
            else:
                iva=iva+ registro[3]*0.21


        preciosConIva= preciosSinIva+iva
        variables.lblSubtotalFactura.set_text(str("{0:.2f}".format(preciosSinIva))+" €")
        variables.lblIvaFactura.set_text(str("{0:.2f}".format(iva))+" €")
        variables.lblTotalFactura.set_text(str("{0:.2f}".format(preciosConIva))+" €")
        return preciosSinIva

    except Exception as e:
        print("error en calcular precios")
        print(e)
