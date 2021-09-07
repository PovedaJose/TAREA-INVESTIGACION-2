import os
from datetime import date

class Empresa:
    def __init__(self, razonSocial, direccion, telefono, ruc, dep_Departamento): 
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefono = telefono
        self.ruc = ruc 
        self.dep_Departamento = Departamento(dep_Departamento,empleado='')

    def mostrarEmpresa(self):   
        print(''' {} 
        - Ruc : {} 
        - Teléfono : {} 
        - Dirección: {}'''.format(self.razonSocial,self.ruc, self.telefono, self.direccion))

    
class Departamento: 
    codigo = 0
    def __init__(self, descripcion, empleado):
        Departamento.codigo += 1
        self.__id = Departamento.codigo
        self.descripcion = descripcion
        self.empleado = empleado
            
    @property
    def id(self):
        return self.__id

    def mostrarDepartamento(self):
        print('{}. DEPARTAMENTO DE {}'.format(self.id,self.descripcion))
 

class Empleado:    
    codigo = 0
    def __init__(self,nombre,tipoEmpleado, direccion, cedula, telefono, fechaIngreso, sueldo):
        Empleado.codigo += 1
        self.__id = Empleado.codigo
        self.nombre = nombre
        self.tipoEmpleado = tipoEmpleado
        self.direccion = direccion
        self.cedula = cedula
        self.telefono = telefono
        self.fechaIngreso = fechaIngreso
        self.sueldo = sueldo

    @property
    def id(self):
        return self.__id

    def valorHora(self):
        return self.sueldo/240

    def mostrarEmpleado(self):
        print(' {} Empleado : {} Cedula: {} dirección : {} Telefono: {} Fecha Ingreso: {}'.format(self.id,self.nombre,self.cedula,self.direccion,self.telefono,self.fechaIngreso))


class Admistrativo(Empleado):
    def __init__(self, nombre,tipoEmpleado, direccion, cedula, telefono, fechaIngreso, sueldo,comision= True):
        super().__init__(nombre,tipoEmpleado, direccion, cedula, telefono, fechaIngreso, sueldo)
        self.comision = comision

    def com(self):
        if self.comision == True:
            self.comision = '5% de comisión'
        else:
            self.comision = 'No adquiere comisión'
    
    def valorHora(self):
        return super().valorHora()
    
    def mostrarEmpleado(self): 
        print(''' {}° Empleado {}: 
        - Nombres:  {}          
        - Cedula:   {}
        - Telefono: {}  
        - Comision: {}
        - Dirección: {}
        - Fecha Ingreso: {}'''.format(self.id,self.tipoEmpleado,self.nombre,self.cedula,self.telefono,self.comision,self.direccion,self.fechaIngreso,))
     

class Obrero(Empleado):
    def __init__(self, nombre,tipoEmpleado, direccion, cedula, telefono, fechaIngreso, sueldo, sindicato=True, contratoColectivo=True):
        super().__init__(nombre,tipoEmpleado, direccion, cedula, telefono, fechaIngreso, sueldo)
        self.sindicato = sindicato
        self.contratoColectivo = contratoColectivo

    def sindicat(self):
        if self.sindicato == True:
            self.sindicato = 'Pertenece a un sindicato'
        else: self.sindicato = '--'
    def contratoc(self):
        if self.contratoColectivo == True:
            self.contratoColectivo = '2% de antiguedad'
        else: self.contratoColectivo = 'Sin contrato'
        
    def valorHora(self):
        return super().valorHora()

    def mostrarEmpleado(self): 
        print('''{}° Empleado {}:
          - Nombres: {} 
          - Cedula: {}  
          - Telefono:  {}
          - Dirección: {}
          - Sindicato: {}
          - Fecha Ingreso: {}
          - Contrato Colectivo: {}'''.format(self.id,self.tipoEmpleado,self.nombre,self.cedula,self.telefono,self.direccion,self.sindicato,self.fechaIngreso,self.contratoColectivo))

         
class Prestamo:
    secuencia = 0
    def __init__(self, fecha, valor, numPagos, cuota, saldo, empleado, estado= True): 
        Prestamo.secuencia += 1
        self.__id = Prestamo.secuencia
        self.fecha = fecha
        self.valor = valor
        self.numPagos = numPagos
        self.cuota = valor/numPagos
        self.saldo = saldo-cuota
        self.empleado = empleado
        self.estado = estado
    
    @property
    def id(self):
        return self.__id

    def calculoPrestamo(self):
        if self.valor > 0:
            self.estado = 'En proceso'
        else:
            self.estado = 'Terminado'

    def mostrarPrestamo(self):
        print('''{}° Prestamo realizado: {}
          - Empleado: {}
          - Valor = ${}
          - Numeros Pagos = {}  
          - Cuota = ${:.2f} 
          - Saldo = ${:.2f}
          - estado = {} '''.format(self.id,self.fecha,self.empleado.nombre,self.valor,self.numPagos,self.cuota,self.saldo,self.estado))


class Sobretiempo:
    secuencia = 0
    def __init__(self, horasRecargo, horasExtraordinarias, fecha, estado,empleado): 
        Sobretiempo.secuencia += 1
        self.__id = Sobretiempo.secuencia
        self.horasRecargo = horasRecargo
        self.horasExtraordinarias = horasExtraordinarias
        self.fecha = fecha
        self.estado = estado
        self.empleado = empleado
    
    @property
    def id(self):
        return self.__id

    def calculoSobretiempo(self):
        return self.empleado.valorHora()*(self.horasRecargo * 0.50 + self.horasExtraordinarias * 2) 

    def mostrarSobretiempo(self):
        print('''{}° sobretiempo realizado: {}
          - Empleado = {}  
          - Horas Recargo (50%) = {} 
          - Horas extraordinarias (100%) = {}
          - estado = {} '''.format(self.id, self.fecha, self.empleado.nombre,self.horasRecargo,self.horasExtraordinarias,self.estado ))


class Deduccion:
    def __init__(self, iess, comision, antiguedad):
        self.iess = iess
        self.comision = comision
        self.antiguedad = antiguedad
        
    def mostrarDeduccion(self):
        print('''Valor de deducciones:
        - Valor Iess = {}
        - Valor comision = {}
        - Valor antiguedad = {}'''.format(self.iess, self.comision, self.antiguedad))


class PagoNomina:
    secuencia = 0
    def __init__(self, fecha, periodo, empleado, sobretiempo,totalingreso, prestamo,totalDscto, liquidoRecibir):
        PagoNomina.secuencia += 1
        self.__id = PagoNomina.secuencia
        self.fecha = fecha
        self.periodo = periodo
        self.empleado = empleado
        self.sobretiempo = sobretiempo
        self.totalIngreso = totalingreso
        self.prestamo = prestamo
        self.totalDescuento = totalDscto
        self.netoPagar = liquidoRecibir
    
    @property
    def id(self):
        return self.__id

    def mostrarPagoNomina(self, razonSocial, direccion, telefono, ruc, dep_Departamento, iessEmpl, comisionEmpl, antigEmpl):
        os.system('cls')
        print('--------------------------------------------------------------------------------------------------------------------')
        print(' N O M I N A   D E   P A G O   I N D I V I D U A L            N°: {}        Fecha: {}'.format(self.id,self.fecha))
        print('---------------------------------------------------------------------------------------------------------------------')
        print(' {}\n Ruc : {:20} Teléfono : {:20} Dirección: {:20}'.format(razonSocial,ruc, telefono, direccion))
        print('--'*59)
        dep_Departamento.mostrarDepartamento()
        self.empleado.mostrarEmpleado() 
        print('---------------------------------------------------------------------------------------------------------------------')
        print(' Nomina del ',self.periodo) 
        if self.empleado.tipoEmpleado == 'Administrativo':
            comision = comisionEmpl * self.empleado.sueldo #CALCULO COMISION
            antiguedad = 0
        else:
            comision = 0
            antiguedad = antigEmpl*(self.fecha.year - self.empleado.fechaIngreso.year)/365* self.empleado.sueldo #CALCULO ANTIGUEDAD
        print('''\n  >> DEVENGADOS             
        - Sueldo:       $ {:.2f}
        - Sobretiempo:  $ {}
        - Comision:     $ {}
        - Antiguedad:   $ {:.2f}'''.format(self.empleado.sueldo, self.sobretiempo.calculoSobretiempo(),comision,antiguedad))
        iessEmpl = iessEmpl*(self.empleado.sueldo + self.sobretiempo.calculoSobretiempo()) #CALCULO IESS
        print('''\n  >> DEDUCCIONES 
        - Préstamo:     $ {:.2f}
        - iess:         $ {:.2f}'''.format(self.prestamo.cuota,iessEmpl))
        self.totalIngreso = self.empleado.sueldo + self.sobretiempo.calculoSobretiempo() + comision + antiguedad # CALCULO INGRESOS
        self.totalDescuento = self.prestamo.cuota + iessEmpl #CALCULO EGRESOS
        self.netoPagar = self.totalIngreso - self.totalDescuento #CALCULO NETO A PAGAR
        print('''\n  Total devengados:     $ {:.2f}\n  Total deducciones:    $ {:.2f} '''.format(self.totalIngreso, self.totalDescuento))                                      
        print('----------------------------------------------------------------------------------------------------------------------')
        print('  LIQUIDO A RECIBIR:    $ {:.2f}'.format(self.netoPagar))
        print('----------------------------------------------------------------------------------------------------------------------')


os.system('cls')  
print(''' << Presentacion de 2 empleados >>\n
 1| Empleado Administrativo.
 2| Empleado Obrero.''')

input('\n Presione ENTER para continuar...') 

os.system('cls')
emp = Empresa('EMPRESA MODELO S.A','Centro','0999999','43556', 'RECURSOS HUMANOS') 
fechaEmpleado = date(2010,9,8)
emple1 = Admistrativo('Heymi Gonzalez','Administrativo','Cdla. La lotita','1204645753', '0932446623',fechaEmpleado,300.00,True) 
print(emple1.com())
prest = Prestamo('5 de enero', 1000, 12,0,0,emple1,0 )
Sobre = Sobretiempo(2,4,'2 febrero', True,emple1) 
deducci = Deduccion(0.0935, 0.05, 0.02 )
fecha = date.today()
nomin = PagoNomina(date.today(),'1 al 30 de agosto' ,emple1,Sobre,0,prest,0,0.0)                                                 
nomin.mostrarPagoNomina(emp.razonSocial,emp.direccion,emp.telefono,emp.ruc, emp.dep_Departamento,deducci.iess,deducci.comision,deducci.antiguedad) 

input('\n Presione ENTER para continuar...')

emp = Empresa('EMPRESA MODELO S.A','Centro','0999999','43556', 'VENTAS') 
os.system('cls')
fechaEmpleadoO = date(2010,9,8)
emple2 = Obrero('Jose Poveda','Obrero','Centro','097687890', '0999999999',fechaEmpleadoO,500.00) 
#emple2.sindicat()
emple2.contratoc()
prest = Prestamo('5 de enero', 1000, 12,0,0,emple2,0 )
Sobre = Sobretiempo(2,4,'2 febrero', True,emple2) 
deducci = Deduccion(0.0935, 0.05, 0.02 )
nomin = PagoNomina(date.today(),'1 al 30 de agosto' ,emple2,Sobre,0,prest,0,0.0)                                          
nomin.mostrarPagoNomina(emp.razonSocial,emp.direccion,emp.telefono,emp.ruc, emp.dep_Departamento,deducci.iess,deducci.comision,deducci.antiguedad)                                         


