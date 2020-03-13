#Funciones relacionadas con excel

import datetime
from xlrd.sheet import Cell
import xlrd


def formatear_fecha_excel(celda):
    """
    Le cambia el formato a la fecha del excel

    :param celda:   Celda del excel a la que se le cambia el formato
    :return:        Fecha con formato d/m/y
    """
    archivo_excel = xlrd.open_workbook("clientes.xls")
    fecha_formateada = datetime.datetime(*xlrd.xldate_as_tuple(celda.value, archivo_excel.datemode))
    return fecha_formateada.strftime('%d/%m/%Y')
