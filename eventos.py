# coding=utf-8
"""
Contiene todos los eventos de el programa
"""
import sqlite3
import webbrowser

import gi

import funciones_factura

gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import conexion, variables, funcionescli, funcioneshab, funcionesreser, funcionesvar, impresion,funciones_servicios
import os, shutil
import xlrd,xlwt
from datetime import date, datetime, time
class Eventos():

# eventos generales
    def on_acercade_activate(self, widget):
        """
        Abre la ventana acerca de
        :return:    Void
        """
        try:
            variables.venacercade.show()
        except:
            print('error abrira acerca de')

    def on_btnCerrarabout_clicked(self, widget):
        """
        Cierra la ventana acerca de
        :return:    Void
        """
        try:
            variables.venacercade.connect('delete-event', lambda w, e: w.hide() or True)
            variables.venacercade.hide()
        except:
            print('error abrir acerca de')

    def on_menuBarsalir_activate(self, widget):
        """
        sale del menu bar
        :return:    Void
        """

        try:
            self.salir()
        except:
            print('salir en menubar')

    def salir(self):
        """
        Abre la ventana acerca de
        :return:    Void
        """

        try:
            conexion.Conexion.cerrarbbdd(self)
            funcionesvar.cerrartimer()
            Gtk.main_quit()
        except:
            print('error función salir')

    def on_venPrincipal_destroy(self, widget):
        """
        Cierra la ventana principal
        :return:    Void
        """
        self.salir()

    def on_btnSalirtool_clicked(self, widget):
        """
        Cierra la
        :return:    Void
        """
        variables.vendialogsalir.show()

    def on_btnCancelarsalir_clicked(self, widget):
        """
            Boton de cancelar la salida
             :return:    Void
        """
        variables.vendialogsalir.connect('delete-event', lambda w, e: w.hide() or True)
        variables.vendialogsalir.hide()

    def on_btnAceptarsalir_clicked(self, widget):
        """
            Boton aceptar salir
             :return:    Void
        """
        self.salir()
    """
    Eventos Clientes
    """

    def on_btnAltacli_clicked(self, widget):
        """
            Boton dar alta cliente
             :return:    Void
        """
        try:
            dni = variables.filacli[0].get_text()
            apel = variables.filacli[1].get_text()
            nome = variables.filacli[2].get_text()
            data = variables.filacli[3].get_text()
            registro = (dni, apel, nome, data)
            if funcionescli.validoDNI(dni):
                funcionescli.insertarcli(registro)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                variables.menslabel[0].set_text('ERROR DNI')
        except:
            print("Error alta cliente")


    def on_btnBajacli_clicked(self, widget):
        """
            Boton dar de baja cliente
             :return:    Void
        """

        try:
            dni = variables.filacli[0].get_text()
            if dni != '' :
                funcionescli.bajacli(dni)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                print('falta dni u otro error')
        except:
            print("error en botón baja cliente")

    def on_btnModifcli_clicked(self, widget):
        """
            Boton modificar cliente
             :return:    Void
        """
        try:
            cod = variables.menslabel[1].get_text()
            dni = variables.filacli[0].get_text()
            apel = variables.filacli[1].get_text()
            nome = variables.filacli[2].get_text()
            data = variables.filacli[3].get_text()
            registro = (dni, apel, nome, data)
            if dni != '':
                funcionescli.modifcli(registro, cod)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                print('falta el dni')
        except:
            print('error en botón modificar')


    def on_entDni_focus_out_event(self, widget, dni):
        """
        Evento que controla que el dni sea correcto
             :return:    Void
        """
        try:
            dni = variables.filacli[0].get_text()
            if funcionescli.validoDNI(dni):
                variables.menslabel[0].set_text('')
                pass
            else:
                variables.menslabel[0].set_text('ERROR')
        except:
            print("Error alta cliente en out focus")


    def on_treeClientes_cursor_changed(self, widget):
        """
            Evento del tree clientes
             :return:    Void
        """
        try:
            model,iter = variables.treeclientes.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            variables.menslabel[0].set_text('')
            funcionescli.limpiarentry(variables.filacli)
            if iter != None:
                sdni = model.get_value(iter, 0)
                sapel = model.get_value(iter, 1)
                snome = model.get_value(iter, 2)
                sdata = model.get_value(iter, 3)
                if sdata == None:
                    sdata = ''
                cod = funcionescli.selectcli(sdni)
                variables.menslabel[1].set_text(str(cod[0]))
                variables.filacli[0].set_text(str(sdni))
                variables.filacli[1].set_text(str(sapel))
                variables.filacli[2].set_text(str(snome))
                variables.filacli[3].set_text(str(sdata))
                variables.menslabel[4].set_text(str(sdni))
                variables.menslabel[5].set_text(str(sapel))


        except:
            print ("error carga cliente")

    def on_btnCalendar_clicked(self, widget):
        """
            Boton que abre la ventana calendario en cliente
             :return:    Void
        """
        try:
            variables.semaforo = 1
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()

        except:
            print('error abrir calendario')

    def on_btnCalendarResIn_clicked(self,widget):
        """
            Boton que abre la ventana calendario en reserva check-in
             :return:    Void
        """
        try:
            variables.semaforo = 2
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()
        except:
            print('error abrir calendario')

    def on_btnCalendarResOut_clicked(self, widget):
        """
            Boton calendario en reserva check-out
             :return:    Void
        """
        try:
            variables.semaforo  = 3
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()
        except:
            print('error abrir calendario')

    def on_Calendar_day_selected_double_click(self, widget):
        """
            Evento al dar doble click a un dia del calendario
             :return:    Void
        """
        try:
            agno, mes, dia = variables.calendar.get_date()
            fecha = "%02d/" % dia + "%02d/" % (mes + 1) + "%s" % agno
            if variables.semaforo == 1:
                variables.filacli[3].set_text(fecha)
            elif variables.semaforo == 2:
                variables.filareserva[2].set_text(fecha)
            elif variables.semaforo == 3:
                variables.filareserva[3].set_text(fecha)
                funcionesreser.calculardias()
            else:
                pass
            variables.vencalendar.hide()
        except:
            print('error al coger la fecha')

# Eventos de las habitaciones

    def on_btnAltahab_clicked(self, widget):
        """
            Boton alta habitacion
             :return:    Void
        """
        try:
            numhab = variables.filahab[0].get_text()
            prezohab = variables.filahab[1].get_text()
            prezohab = prezohab.replace(',','.')
            prezohab = float(prezohab)
            prezohab = round(prezohab,2)
            if variables.filarbt[0].get_active():
                tipo = 'simple'
            elif variables.filarbt[1].get_active():
                tipo = 'doble'
            elif variables.filarbt[2].get_active():
                tipo = 'family'
            else:
                pass

            if variables.switch.get_active():
                libre = 'SI'
            else:
                libre = 'NO'
            registro = (numhab, tipo, prezohab, libre)
            if numhab != None:
               funcioneshab.insertarhab(registro)
               funcioneshab.listadohab(variables.listhab)
               funcioneshab.listadonumhab()
               funcioneshab.limpiarentry(variables.filahab)
            else:
                pass
        except:
            print("Error alta habitacion")

    def on_treeHab_cursor_changed(self, widget):
        """
            Evento tree habitaciones
             :return:    Void
        """
        try:
            model, iter = variables.treehab.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            funcioneshab.limpiarentry(variables.filahab)
            if iter != None:
                snumhab = model.get_value(iter, 0)
                stipo = model.get_value(iter, 1)
                sprezo = model.get_value(iter, 2)
                sprezo = round(sprezo,2)
                variables.filahab[0].set_text(str(snumhab))
                variables.filahab[1].set_text(str(sprezo))
                if stipo == str('simple'):
                    variables.filarbt[0].set_active(True)
                elif stipo == str('doble'):
                    variables.filarbt[1].set_active(True)
                elif stipo == str('family'):
                    variables.filarbt[2].set_active(True)
                slibre = model.get_value(iter,3)
                if slibre == str('SI'):
                    variables.switch.set_active(True)
                else:
                    variables.switch.set_active(False)
        except:
            print("error carga habitacion")


    def on_btnBajahab_clicked(self,widget):
        """
        Boton baja habitaciones
        :return:    Void
        """
        try:
            numhab = variables.filahab[0].get_text()
            if numhab != '':
                funcioneshab.bajahab(numhab)
                funcioneshab.limpiarentry(variables.filahab)
                funcioneshab.listadohab(variables.listhab)
            else:
                pass
        except:
            print('borrar baja hab')


    def on_btnModifhab_clicked(self, widget):
        """
        Boton modificar habitaciones
        :return:    Void
        """
        try:
            numhab = variables.filahab[0].get_text()
            prezo = variables.filahab[1].get_text()
            if variables.switch.get_active():
                libre = 'SI'
            else:
                libre = 'NO'

            if variables.filarbt[0].get_active():
                tipo = 'simple'
            elif variables.filarbt[1].get_active():
                tipo = 'doble'
            elif variables.filarbt[2].get_active():
                tipo = 'family'
            else:
                pass
            registro = (prezo, tipo, libre)
            if numhab != '':
                funcioneshab.modifhab(registro, numhab)
                funcioneshab.listadohab(variables.listhab)
                funcioneshab.limpiarentry(variables.filahab)
            else:
                print('falta el numhab')
        except:
            print('error modif hab')


    # eventos de los botones del toolbar

    def on_Panel_select_page(self, widget):
        """
        evento barra de herramientas
        :return:    Void
        """
        try:
            funcioneshab.listadonumhab()
        except:
            print("error botón cliente barra herramientas")

    def on_btnClitool_clicked (self, widget):
        """
        Boton para elegir pagina del panel
        :return:    Void
        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 0:
                variables.panel.set_current_page(0)
            else:
                pass
        except:
            print("error botón cliente barra herramientas")

    def on_btnReservatool_clicked(self, widget):
        """
        Boton reserva de la barra de herramientas
        :return:    Void
        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 1:
                variables.panel.set_current_page(1)
                funcioneshab.listadonumhab(self)
            else:
                pass
        except:
            print("error botón cliente barra herramientas")

    def on_btnHabita_clicked(self,widget):
        """
        Boton habitacion  de la barra de herramientas
        :return:    Void
        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 2:
                variables.panel.set_current_page(2)
            else:
                pass
        except:
            print("error botón habitacion barra herramientas")

    def on_btnCalc_clicked(self, widget):
        """
        Boton calculadora
        :return:    Void
        """
        try:
            os.system('/snap/bin/gnome-calculator')
        except:
            print('error lanzar calculadora')

    def on_btnRefresh_clicked(self, widget):
        """
        Boton refrescar
        :return:    Void
        """
        try:
            funcioneshab.limpiarentry(variables.filahab)
            funcionescli.limpiarentry(variables.filacli)
            funcionesreser.limpiarentry(variables.filareserva)
            funciones_servicios.limpiarEntry()
        except:
            print('error referes')

    def on_btnBackup_clicked(self, widget):
        """
        Boton para cargar el backup
        :return:    Void
        """
        try:
            variables.filechooserbackup.show()
            variables.neobackup = funcionesvar.backup()
            variables.neobackup = str(os.path.abspath(variables.neobackup))

        except:
            print('error abrir file choorse backup')

    def on_btnGrabarbackup_clicked(self, widget):
        """
       Boton para grabar el backup
        :return:    Void
        """
        try:
            destino = variables.filechooserbackup.get_filename()
            destino = destino + '/'
            variables.menslabel[3].set_text(str(destino))
            if shutil.move(str(variables.neobackup), str(destino)):
                variables.menslabel[3].set_text('Copia de Seguridad Creada')
        except:
            print('error dselect fichero')


    def on_btnCancelfilechooserbackup_clicked(self, widget):
        """
        Boton para cancelar la ventana de backup
        :return:    Void
        """
        try:
            variables.filechooserbackup.connect('delete-event', lambda w, e: w.hide() or True)
            variables.filechooserbackup.hide()
        except:
            print('error cerrar file chooser')

## reservas

    def on_cmbNumres_changed(self, widget):
        """
        Combobos numero reserva
        :return:    Void
        """
        try:
            index = variables.cmbhab.get_active()
            model = variables.cmbhab.get_model()
            item = model[index]
            variables.numhabres = item[0]
        except Exception as e:
            print(e)
            print('error mostrar habitacion combo')

    def on_btnAltares_clicked(self, widget):
        """
        Boton alta reserva
        :return:    Void
        """
        try:
            if variables.lbldnires.get_text()!="":
                if variables.reserva == 1:
                    dnir = variables.menslabel[4].get_text()
                    chki = variables.filareserva[2].get_text()
                    chko = variables.filareserva[3].get_text()
                    noches = int(variables.menslabel[2].get_text())
                    registro = (dnir, variables.numhabres, chki, chko, noches)
                    if funcionesreser.versilibre(variables.numhabres):
                        funcionesreser.insertares(registro)
                        funcionesreser.listadores(variables.listreservas)
                        #actualizar a NO
                        libre = 'NO'
                        funcioneshab.cambiaestadohab(libre, variables.numhabres)
                        funcioneshab.listadohab(variables.listhab)
                        funcioneshab.limpiarentry(variables.filahab)
                        funcionesreser.limpiarentry(variables.filareserva)
                    else:
                        variables.mensajeError = "Habitacion ocupada"
                        variables.vError.show()
            else:
                variables.mensajeError = "Selecciona un cliente de reserva"
                variables.vError.show()

        except Exception as e:
            print(e)
            print ('error en alta res')

    def on_btnRefreshcmbhab_clicked(self, widget):
        """
        Boton refrescar combobox habitacion
        :return:    Void
        """
        try:
            variables.cmbhab.set_active(-1)
            funcioneshab.listadonumhab(self)
        except:
            print ('error limpiar combo hotel')

    def on_treeReservas_cursor_changed(self, widget):
        """
        Evento tree Reservas
        :return:    Void
        """
        try:
            model, iter = variables.treereservas.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            funcionesreser.limpiarentry(variables.filareserva)
            if iter != None:
                variables.codr = model.get_value(iter,0)
                sdni = model.get_value(iter, 1)
                sapel = funcionesreser.buscarapelcli(str(sdni))
                snome = funcionesreser.buscarnome(str(sdni))
                snumhab =  model.get_value(iter, 2)
                lista = funcioneshab.listadonumhabres()
                m = -1
                for i, x in enumerate(lista):
                    if str(x[0]) == str(snumhab):
                        m = i
                variables.cmbhab.set_active(m)
                schki = model.get_value(iter, 3)
                schko = model.get_value(iter,4)
                snoches = model.get_value(iter, 5)

                variables.menslabel[4].set_text(str(sdni))

                variables.menslabel[5].set_text(str(sapel[0]))

                variables.menslabel[2].set_text(str(snoches))

                #variables.lblunidadesFacturacion.set_text(str(snoches))
                variables.filareserva[2].set_text(str(schki))
                variables.filareserva[3].set_text(str(schko))
                variables.lblfechaFacturacion.set_text(str(schko))
                variables.lbldniFacturacion.set_text(str(sdni))
                variables.lblapelidoFacturacion.set_text(str(sapel[0]))
                variables.lblcodigoReservaFacturacion.set_text(str(variables.codr))
                variables.lblnomeFacturacion.set_text(str(snome[0]))
                variables.lblhabitacionFacturacion.set_text(str(snumhab))
                precioUnidad= funcionesreser.buscarpreciohabitacion(str(snumhab))
                #variables.lblprecioUnidadFacturacion.set_text(str(precioUnidad[0]))
                precioTotal= float(str(snoches)) * float(str(precioUnidad[0]))
                #variables.lbltotalFacturacion.set_text(str(precioTotal))
                variables.lblCodigoReservaServicio.set_text(str(variables.codr))
                variables.lblHabitacionServicio.set_text(str(snumhab))
                global datosfactura
                datosfactura = (variables.codr,snoches,sdni,snumhab, schko,str(precioUnidad[0]))

                funciones_servicios.listadoServicio(variables.listServicios,variables.codr)
                funciones_factura.listadoServicios(variables.listFactura,variables.codr,snumhab)
                funciones_factura.calcularPreciosServicios()

        except Exception as e:
            print(e)
            print ('error cargar valores de reservas')


    def on_btnFinReserva_clicked(self, widget):
        """
        Boton fin Reserva
        :return:    Void
        """
        try:
            libre ='SI'
            numhabres = variables.numhabres
            funcioneshab.cambiaestadohab(libre, numhabres)
            print("cara")

            funcionesreser.listadores(variables.listreservas)
            print("cola")

            funcioneshab.listadohab(variables.listhab)

            funcionesreser.limpiarentry(variables.filareserva)

        except Exception as e:
            print(e)
            print('error baja reserva')

    def on_btnModifres_clicked(self, widget):
        """
        Boton modificar reserva
        :return:    Void
        """
        try:
            dnir = variables.menslabel[4].get_text()
            chki = variables.filareserva[2].get_text()
            chko = variables.filareserva[3].get_text()
            noches = int(variables.menslabel[2].get_text())
            registro = (dnir, variables.numhabres, chki, chko, noches)
            funcionesreser.modifreserva(registro, variables.codr)
            funcionesreser.limpiarentry(variables.filareserva)
            funcionesreser.listadores(variables.listreservas)

        except:
            print('error modificar reserva')

    def on_btChkout_clicked(self, widget):
        """
        Boton checkout reserva
        :return:    Void
        """
        try:
            chko = variables.filareserva[3].get_text()
            today = date.today()
            hoy = datetime.strftime(today,'%d/%m/%Y')
            registro = (variables.numhabres)
            if str(hoy) == str(chko):
                funcioneshab.modifhabres(registro)
                funcioneshab.listadohab(variables.listhab)
            else:
                print('puede facturar')
                #cambiar el estado de la habitación de ocupada a libre

        except Exception as e:
            print(e)
            print('error en checkout')

    def on_btnImprimir_clicked(self, widget):
        """
        Boton imprimir reserva
        :return:    Void
        """
        try:

            impresion.factura(datosfactura,variables.listFactura,variables.lblSubtotalFactura.get_text(),variables.lblIvaFactura.get_text(),variables.lblTotalFactura.get_text())
        except Exception as e:
            print(e)

    def on_btnCancelfilechooserImportar_clicked(self, widget):
        """
        Boton cancelar importar
        :return:    Void
        """
        try:
            variables.filechooserImportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.filechooserImportar.hide()
        except:
            print('error cerrar file chooser')

    def on_menuBarImportarClientes_activate(self, widget):
        """
        Boton importar
        :return:    Void
        """
        try:
            variables.filechooserImportar.show()

        except Exception as e:
            print(e)
            print('Error en exportar clientes')

    def on_btnCancelfilechooserExportar_clicked(self, widget):
        """
        Boton cancelar exportar
        :return:    Void
        """
        try:
            variables.fileChooserExportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.fileChooserExportar.hide()
        except:
            print('error cerrar file chooser exportar')

    def on_menuBarExportarClientes_activate(self, widget):
        """
        Boton exportar
        :return:    Void
        """
        try:
            variables.fileChooserExportar.show()

        except Exception as e:
            print(e)
            print('Error en abrir ventana exportar clientes')


    def on_btnCancelfilechooserImportar_clicked(self, widget):
        """
        Boton cancelar importar
        :return:    Void
        """
        try:
            variables.filechooserImportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.filechooserImportar.hide()
        except:
            print('error cerrar file chooser importar')

    def on_btnGrabarImportar_clicked(self, widget):
        """
        Boton grabar importacion
        :return:    Void
        """
        try:
            destino = variables.filechooserImportar.get_filename()
            fichero_excel = xlrd.open_workbook(destino)
            hoja_clientes = fichero_excel.sheet_by_index(0)
            numero_filas_clientes = hoja_clientes.nrows
            numero_columnas_clientes = hoja_clientes.ncols

            for i in range(numero_filas_clientes):
                celdas_cliente = []
                if i > 0:
                    for j in range(numero_columnas_clientes):
                        celdas_cliente.append(hoja_clientes.cell(i, j))
                    funcionescli.insertar_cliente_excel_BD(celdas_cliente)
                    funcionescli.listadocli(variables.listclientes)
            variables.filechooserImportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.filechooserImportar.hide()


        except Exception as e:
            variables.filechooserImportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.filechooserImportar.hide()
            print(e)
            print('Error en importar clientes')

    def on_btnGrabarExportar_clicked(self, widget):
        """
        Boton grabar exportacion
        :return:    Void
        """
        try:
            destino = variables.fileChooserExportar.get_filename()
            destino = str(destino) + str('/informes/clientes_exportados.xls')
            
            estilo_cabecera = xlwt.easyxf('font: name Times New Roman, colour red, bold on')

            estilo_celda = xlwt.easyxf(num_format_str='DD-MM-YY')
            fichero_excel = xlwt.Workbook(str(destino))

            hoja_excel = fichero_excel.add_sheet('NuevoClientes', cell_overwrite_ok=True)
            hoja_excel.write(0, 0, 'DNI', estilo_cabecera)
            hoja_excel.write(0, 1, 'APELIDOS', estilo_cabecera)
            hoja_excel.write(0, 2, 'NOMBRE', estilo_cabecera)
            hoja_excel.write(0, 3, 'FECHA_ALTA', estilo_cabecera)

            listado_clientes = funcionescli.listar()

            for i in range(len(listado_clientes)):
                for j in range(len(listado_clientes[0])):
                    hoja_excel.write(i, j, listado_clientes[i][j], estilo_celda)
            fichero_excel.save(destino)
            variables.fileChooserExportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.fileChooserExportar.hide()

        except Exception as e:
            variables.fileChooserExportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.fileChooserExportar.hide()
            print(e)
            print('Error en exportar clientes')


    def on_menuBarExportarClientes_activate(self, widget):
        """
        Menu barra exportar
        :return:    Void
        """
        try:
            variables.fileChooserExportar.show()


        except Exception as e:
            print(e)
            print("Error al abrir exportar clientes")


    def on_menuBarPreciosServicios_activate(self,widget):
        """
        abrir ventana de precios servicios con los precios cargados
        :return: Void
        """

        try:
         variables.venPrecios.show()
         conexion.cur.execute('select * from precios')
         precios = conexion.cur.fetchall()
         variables.entPrecioDesayuno.set_text(str(precios[0][0]))
         variables.entPrecioComida.set_text(str(precios[0][1]))
         variables.entPrecioParking.set_text(str(precios[0][2]))
        except:
            print('error abrir ventana precios')


    def on_btnCancelarPrecios_clicked(self, widget):
        """
        Boton cerrar sin guardar ventana precios
        :return:    Void
        """
        try:
            variables.venPrecios.connect('delete-event', lambda w, e: w.hide() or True)
            variables.venPrecios.hide()
        except:
            print('error cerrar ventana precios servicios')

    def on_btnAceptarPrecios_clicked(self, widget):
        """
        Boton cerrar ventana precios guardando los precios nuevos
        :return:    Void
        """
        try:
            precioDesayuno= variables.entPrecioDesayuno.get_text();
            precioComida=variables.entPrecioComida.get_text();
            precioParking=variables.entPrecioParking.get_text();
            precios=(precioDesayuno,precioComida,precioParking)
            funciones_servicios.modificarPrecios(precios)
            variables.venPrecios.connect('delete-event', lambda w, e: w.hide() or True)
            variables.venPrecios.hide()
        except sqlite3.OperationalError as e:
            print(e)
            conexion.conex.rollback()


    def on_btnAltaServicioBasico_clicked(self,widget):

        """
        Boton dar alta un servicio basico
        :return:    Void
        """
        try:
            conexion.cur.execute('select * from precios')
            precios = conexion.cur.fetchall()
            if(variables.lblCodigoReservaServicio.get_text()!=""):
                codigoReservaServicio = variables.lblCodigoReservaServicio.get_text()
                if(variables.rbDesayuno.get_active()):
                    existeDesayuno=False
                    for registro in variables.listFactura:
                        print(registro[0])
                        if registro[0] == "Desayuno":
                            existeDesayuno=True
                    if existeDesayuno==False:
                        precio=precios[0][0]
                        concepto="Desayuno"
                        datos=(codigoReservaServicio,concepto,precio)
                        funciones_servicios.insertarServicio(datos)
                    else:
                        variables.mensajeError = "No puedes insertar otro desayuno"
                        variables.vError.show()

                elif(variables.rbComida.get_active()):
                    existeComida = False
                    for registro in variables.listFactura:
                        if registro[0] == "Comida":
                            existeComida = True
                    if existeComida == False:
                        precio = precios[0][1]
                        concepto = "Comida"
                        datos = (codigoReservaServicio, concepto, precio)
                        funciones_servicios.insertarServicio(datos)
                    else:
                        variables.mensajeError = "No puedes insertar otra comida"
                        variables.vError.show()


                if(variables.chkParking.get_active()):
                    existeParking = False
                    for registro in variables.listFactura:
                        if registro[0] == "Parking":
                            existeParking = True
                    if existeParking == False:
                        precio = precios[0][2]
                        concepto = "Parking"
                        datos = (codigoReservaServicio, concepto, precio)
                        funciones_servicios.insertarServicio(datos)
                    else:
                        variables.mensajeError = "No puedes insertar otro servicio de parking"
                        variables.vError.show()


                variables.rbNinguno.set_active(True)
                variables.chkParking.set_active(False)
                funciones_servicios.listadoServicio(variables.listServicios,codigoReservaServicio)
                funciones_factura.listadoServicios(variables.listFactura,variables.codr,variables.lblHabitacionServicio.get_text())
                funciones_factura.calcularPreciosServicios()

            else:
                variables.mensajeError="Debes seleccionar un codigo de reserva"
                variables.vError.show()


        except Exception as e:
            print("Error alta servicio")
            print(e)

    def on_btnAltaOtroServicio_clicked(self,widget):

        """
        Boton dar alta un servicio extra
        :return:    Void
        """
        try:

            codigoReservaServicio=variables.lblCodigoReservaServicio.get_text()
            if (variables.lblCodigoReservaServicio.get_text() != ""):
                if(variables.entTipoServicio.get_text()!=""):
                    if (variables.entPrecioServicio.get_text() != ""):
                        existeOtroServicio = False
                        for registro in variables.listFactura:
                            if registro[0] == variables.entTipoServicio.get_text():
                                existeOtroServicio = True
                        if existeOtroServicio == False:
                            precio = str(variables.entPrecioServicio.get_text())
                            concepto = str(variables.entTipoServicio.get_text())
                            datos = (codigoReservaServicio, concepto, precio)
                            funciones_servicios.insertarServicio(datos)

                        else:
                            variables.mensajeError = "No puedes insertar otro servicio extra con el mismo nombre"
                            variables.vError.show()
                        variables.entTipoServicio.set_text("")
                        variables.entPrecioServicio.set_text("")

                    else:
                        variables.mensajeError = "Debes insertar un precio servicio"
                        variables.vError.show()

                else:
                    variables.mensajeError = "Debes insertar un tipo de servicio"
                    variables.vError.show()
                funciones_servicios.listadoServicio(variables.listServicios,codigoReservaServicio)
                funciones_factura.listadoServicios(variables.listFactura,variables.codr,variables.lblHabitacionServicio.get_text())
                funciones_factura.calcularPreciosServicios()

            else:
                variables.mensajeError = "Debes seleccionar un codigo de reserva"
                variables.vError.show()

        except Exception as e:
            print("Error alta servicio")
            print(e)

    def on_btnBajaServicio_clicked(self, widget):
        """
            Evento del boton que da de baja el servicio
             :return:    Void
        """
        try:
            codigoReservaServicio = variables.lblCodigoReservaServicio.get_text()
            if(variables.codigoServicio!= ""):
                funciones_servicios.eliminarServicio(variables.codigoServicio)
                funciones_servicios.listadoServicio(variables.listServicios, codigoReservaServicio)
                funciones_factura.listadoServicios(variables.listFactura,variables.codr,variables.lblHabitacionServicio.get_text())
                funciones_factura.calcularPreciosServicios()
            else:
                variables.mensajeError = "Debes seleccionar un servicio"
                variables.vError.show()


        except:
            print ("error baja servicio")

    def on_treeServicios_cursor_changed(self, widget):
        """
            Evento del tree servicios
             :return:    Void
        """
        try:
            model,iter = variables.treeServicios.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            variables.menslabel[0].set_text('')
            if iter != None:
                variables.codigoServicio = model.get_value(iter, 0)


        except:
            print ("error carga servicio")

    def on_btnCerrarVentanaError_clicked(self, widget):
        """
            Evento del boton que cierra la ventana error
             :return:    Void
        """
        try:
            variables.vError.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vError.hide()
        except:
            print ("error cerrar ventana error ")

    def on_vError_show(self, widget):
        """
            Evento del boton que cierra la ventana error
             :return:    Void
        """
        try:
            if(variables.mensajeError!=""):
                variables.lblMensajeError.set_text(variables.mensajeError)
                variables.mensajeError=""
            else:
                variables.lblMensajeError.set_text("error")

        except:
            print ("error cerrar ventana error ")

    def on_axuda_activate(self, widget):
        """
            Evento del boton para abrir la documentacion
             :return:    Void
        """

        os.system('pydoc -p 1234')
        webbrowser.open_new('http://localhost:1234')

    def on_imprimirClientes_activate(self,widget):

        """
        Boton imprimir clientes
        :return:    Void
        """
        try:
            impresion.clientes(variables.listclientes)
        except Exception as e:
            print(e)