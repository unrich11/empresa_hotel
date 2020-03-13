# coding=utf-8
"""
Impresion

"""
import shutil

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os, funcionescli

import variables


def basico(pdf):
    """
    Plantilla de la factua

    :return:    La plantilla de la factura
    """
    try:
        pdf = pdf
        texto_bienvenida = 'Bienvenido a nuestro hotel'
        cif = 'CIF:00000000A'
        pdf.drawImage('./img/logohotel.png', 475, 675, width=64, height=64)
        pdf.setFont('Helvetica-Bold', size=16)
        pdf.drawString(250, 780, 'HOTEL LITE')
        pdf.setFont('Times-Italic', size=10)
        pdf.drawString(240, 765, texto_bienvenida)
        pdf.drawString(260, 755, cif)
        pdf.line(50, 670, 540, 670)
        texto_pie = 'Hotel Lite, Tlfo = 986291132 e-mail = info@hotellite.com'
        pdf.setFont('Times-Italic', size=8)
        pdf.drawString(170, 30, texto_pie)
        pdf.setFont('Helvetica-Bold', size=10)

        pdf.drawString(530, 30,str(pdf.getPageNumber()))

        pdf.line(50, 50, 540, 50)
        return pdf
    except Exception as e:
        print(e)
        print('Error en basico')


def factura(datos_factura,listFactura,subtotalFactura,ivaFactura,totalFactura):
    """
    Rellena la plantilla de la factura con los datos de la reserva a facturar

    :param datos_factura:   Datos de la factura de la reserva
    :return:                Void
    """
    try:
        pdf=canvas.Canvas("factura.pdf",pagesize=A4)
        factura = basico(pdf)
        factura.setTitle('FACTURA')

        factura.setFont('Helvetica-Bold', size=8)
        numero_factura = 'Numero de Factura:'
        factura.drawString(50, 735, numero_factura)
        factura.setFont('Helvetica', size=8)
        factura.drawString(140, 735, str(datos_factura[0]))

        factura.setFont('Helvetica-Bold', size=8)
        fecha_factura = 'Fecha Factura:'
        factura.drawString(300, 735, fecha_factura)
        factura.setFont('Helvetica', size=8)
        factura.drawString(360, 735, str(datos_factura[4]))

        factura.setFont('Helvetica-Bold', size=8)
        dni_cliente = 'DNI CLIENTE:'
        factura.drawString(50, 710, dni_cliente)
        factura.setFont('Helvetica', size=8)
        factura.drawString(120, 710, str(datos_factura[2]))

        factura.setFont('Helvetica-Bold', size=8)
        numero_habitacion = 'Nº de Habitación:'
        factura.drawString(300, 710, numero_habitacion)
        factura.setFont('Helvetica', size=8)
        factura.drawString(380, 710, str(datos_factura[3]))
        nombre_y_apellidos = funcionescli.apelnomfac(datos_factura[2])

        factura.setFont('Helvetica-Bold', size=8)
        apellidos_cliente = 'APELLIDOS:'

        factura.drawString(50, 680, apellidos_cliente)
        factura.setFont('Helvetica', size=8)
        factura.drawString(120, 680, nombre_y_apellidos[0])
        factura.setFont('Helvetica-Bold', size=8)
        nombre_cliente = 'NOMBRE:'
        factura.drawString(300, 680, nombre_cliente)
        factura.setFont('Helvetica', size=8)
        factura.drawString(350, 680, nombre_y_apellidos[1])


        cabecera = ['CONCEPTO', 'UNIDADES', 'PRECIO/UNIDAD', 'TOTAL']

        x = 75
        for i in range(0, 4):
            factura.setFont('Helvetica-Bold', size=10)
            factura.drawString(x, 655, cabecera[i])
            x += 130

        y=625

        for registro in listFactura:
            x = 75

            for i in range(0, 4):
                if i==3:
                    factura.setFont('Helvetica', size=8)
                    factura.drawRightString(x+30, y, str(registro[i])+" €")
                elif i==2:
                    factura.setFont('Helvetica', size=8)
                    factura.drawRightString(x+50, y, str(registro[i])+" €")
                elif i==1:
                    factura.setFont('Helvetica', size=8)
                    factura.drawString(x+20, y, str(registro[i]))
                else:
                    factura.setFont('Helvetica', size=8)
                    factura.drawString(x, y, str(registro[i]))
                x += 130
            y -= 30

        factura.line(50, 120, 540, 120)

        factura.setFont('Helvetica', size=8)
        factura.drawString(420, 100, "Subtotal :")
        factura.drawString(420, 80, "Iva :")
        factura.drawString(420, 60, "Total :")
        factura.drawRightString(500, 100, subtotalFactura)
        factura.drawRightString(500, 80, ivaFactura)
        factura.drawRightString(500, 60, totalFactura)

        factura.line(50, 645, 540, 645)

        factura.showPage()
        directorio_actual = os.getcwd()

        factura.save()
        os.system('rm ' + directorio_actual + '/informes/factura.pdf')
        shutil.move(str("factura.pdf"), str(directorio_actual + '/informes'))
        os.system('/usr/bin/xdg-open ' + directorio_actual + '/informes/factura.pdf')
    except Exception as e:
        print(e)
        print('Error en factura')

def clientes(listClientes):

    """
    Rellena la plantilla de la factura con los datos de la reserva a facturar

    :param datos_factura:   Datos de la factura de la reserva
    :return:                Void
    """
    try:
        pdf=canvas.Canvas("clientes.pdf",pagesize=A4)

        pdf = basico(pdf)
        pdf.setTitle('CLIENTES')

        cabecera = ['DNI', 'APELLIDOS', 'NOME', 'DATA ALTA']

        x = 75
        for i in range(0, 4):
            pdf.setFont('Helvetica-Bold', size=10)
            pdf.drawString(x, 655, cabecera[i])
            x += 130
        y=600
        for registro in listClientes:
            x = 75
            if y<= 80:
                y=600
                pdf.showPage()
                pdf.setFont('Helvetica-Bold', size=10)
                pdf.drawString(530, 50, str(pdf.getPageNumber()))
                pdf.line(50, 780, 540, 780)
                for i in range(0, 4):
                    pdf.setFont('Helvetica-Bold', size=10)
                    pdf.drawString(x, 760, cabecera[i])
                    x += 130
                pdf.line(50, 740, 540, 740)
                pdf.line(50, 75, 540, 75)
                y=720
                x=75
            for i in range(0, 4):
                pdf.setFont('Helvetica', size=8)
                if(i==0):
                    pdf.drawString(x, y, str("*****"+registro[i][6]+registro[i][7]+registro[i][8]))
                else:
                    pdf.drawString(x, y, str(registro[i]))

                x += 130
            y -= 30


        pdf.showPage()
        pdf.save()
        directorio_actual = os.getcwd()
        os.system('rm ' + directorio_actual + '/informes/clientes.pdf')

        shutil.move(str("clientes.pdf"), str(directorio_actual + '/informes'))
        os.system('/usr/bin/xdg-open ' + directorio_actual + '/informes/clientes.pdf')
    except Exception as e:
        print(e)
        print('Error en factura')
