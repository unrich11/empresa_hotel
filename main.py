import gi


gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk

import eventos, conexion, variables
import funcionescli, funcioneshab, funcionesreser,funcionesvar,funciones_servicios

'''
el main contiene los elementos necesarios para lanzar la aplicación
así como la declaración de los widgets que se usarán. También los módulos
que tenemos que importar de las librerías gráficas

'''

class Empresa:
    def __init__(self):
        #iniciamos la libreria Gtk
        self.b = Gtk.Builder()
        self.b.add_from_file('ventana.glade')

        #cargamos los widgets con algún evente asociado o que son referenciados
        vprincipal = self.b.get_object('venPrincipal')
        self.vendialog = self.b.get_object('venDialog')
        variables.venacercade = self.b.get_object('venAcercade')
        variables.panel = self.b.get_object('Panel')
        variables.filechooserbackup = self.b.get_object('fileChooserbackup')
        variables.filechooserImportar = self.b.get_object('fileChooserImport')
        variables.fileChooserExportar = self.b.get_object('fileChooserExportar')
        variables.venPrecios = self.b.get_object('venPrecios')
        menubar = self.b.get_object('menuBar').get_style_context()


        #declaracion de wigdets
        entdni = self.b.get_object('entDni')
        entapel = self.b.get_object('entApel')
        entnome = self.b.get_object('entNome')
        entdatacli = self.b.get_object('entDatacli')
        lblerrdni = self.b.get_object('lblErrdni')
        lblcodcli = self.b.get_object('lblCodcli')
        lblnumnoches = self.b.get_object('lblNumnoches')
        lbldirbackup = self.b.get_object('lblFolderbackup')
        lbldirectorioImportar = self.b.get_object('lblFolderImportar')
        variables.lbldirExportar = self.b.get_object('lblFolderExportar')
        variables.lbldnires = self.b.get_object('lblDnires')
        lbldnires = self.b.get_object('lblDnires')
        variables.lblapelres = self.b.get_object('lblApelres')
        lblapelres = self.b.get_object('lblApelres')
        variables.vencalendar = self.b.get_object('venCalendar')
        variables.vendialogsalir = self.b.get_object('vendialogSalir')
        variables.calendar = self.b.get_object('Calendar')
        variables.filacli = (entdni, entapel, entnome, entdatacli)
        variables.listclientes = self.b.get_object('listClientes')
        variables.treereservas = self.b.get_object('treeReservas')
        variables.listreservas = self.b.get_object('listReservas')
        variables.treeclientes = self.b.get_object('treeClientes')
        variables.menslabel = (lblerrdni, lblcodcli, lblnumnoches, lbldirbackup, lbldnires, lblapelres)

        #widgets habitaciones
        entnumhab = self.b.get_object('entNumhab')
        entprezohab = self.b.get_object('entPrezohab')
        rbtsimple = self.b.get_object('rbtSimple')
        rbtdoble = self.b.get_object('rbtDoble')
        rbtfamily = self.b.get_object('rbtFamily')
        variables.treehab = self.b.get_object('treeHab')
        variables.listhab = self.b.get_object('listHab')
        variables.filahab = (entnumhab, entprezohab)
        variables.filarbt = (rbtsimple, rbtdoble, rbtfamily)
        variables.listcmbhab = self.b.get_object('listcmbHab')
        variables.cmbhab = self.b.get_object('cmbNumres')
        variables.switch = self.b.get_object('switch')

        #widgtes reservas

        entdatain = self.b.get_object('entDatain')
        entdataout = self.b.get_object('entDataout')
        #widgets precios
        variables.rbNinguno = self.b.get_object('rbNinguno')
        variables.rbDesayuno = self.b.get_object('rbDesayuno')
        variables.rbComida = self.b.get_object('rbComida')
        variables.chkParking = self.b.get_object('chkParking')

        variables.treeServicios=self.b.get_object('treeServicios')
        variables.treeReserva=self.b.get_object('treeReserva')
        variables.listServicios=self.b.get_object('listServicios')
        variables.listFactura=self.b.get_object('listFactura')
        variables.entPrecioServicio=self.b.get_object('entPrecioServicio')
        variables.entTipoServicio=self.b.get_object('entTipoServicio')


        variables.entPrecioDesayuno = self.b.get_object('entPrecioDesayuno')
        variables.entPrecioComida = self.b.get_object('entPrecioComida')
        variables.entPrecioParking = self.b.get_object('entPrecioParking')
        variables.lblCodigoReservaServicio = self.b.get_object('lblCodigoReservaServicio')
        variables.lblHabitacionServicio = self.b.get_object('lblHabitacionServicio')

        variables.vError = self.b.get_object('vError')
        variables.lblMensajeError = self.b.get_object('lblMensajeError')


        variables.filareserva = (entdni, entapel, entdatain, entdataout)

        #widgets facturacion

        variables.lbldniFacturacion = self.b.get_object('lblDniFacturacion')
        variables.lblapelidoFacturacion = self.b.get_object('lblApelidoFacturacion')
        variables.lblnomeFacturacion = self.b.get_object('lblNomeFacturacion')
        variables.lblcodigoReservaFacturacion = self.b.get_object('lblCodigoReservaFacturacion')
        variables.lblhabitacionFacturacion = self.b.get_object('lblHabitacionFacturacion')
        variables.lblfechaFacturacion = self.b.get_object('lblFechaFacturacion')
        variables.lblSubtotalFactura = self.b.get_object('lblSubtotalFactura')
        variables.lblIvaFactura = self.b.get_object('lblIvaFactura')
        variables.lblTotalFactura = self.b.get_object('lblTotalFactura')


        #conectamos
        self.b.connect_signals(eventos.Eventos())

        #conexion estilos

        self.set_style()
        menubar.add_class('menuBar')
        '''
        for i in range(len(variables.menserror)):
            variables.menserror[i].add_class('label')
        '''
        vprincipal.show_all()
        vprincipal.maximize()
        conexion.Conexion().abrirbbdd()
        funcioneshab.listadonumhab(self)
        funcionescli.listadocli(variables.listclientes)
        funcioneshab.listadohab(variables.listhab)
        funcionesreser.listadores(variables.listreservas)
        funcionesvar.controlhab()


    def set_style(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('estilos.css')
        Gtk.StyleContext().add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


if __name__=='__main__':
    main = Empresa()
    Gtk.main()

