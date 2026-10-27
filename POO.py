from enum import Enum

class Moneda(Enum):
    DOP = "DOP"
    USD = "USD"
    EUR = "EUR"


class TipoCuenta(Enum):
    AHORRO = "Ahorro"
    CORRIENTE = "Corriente"


class TipoPrestamo(Enum):
    PERSONAL = "Personal"
    VEHICULO = "Vehículo"
    HIPOTECARIO = "Hipotecario"

class Cliente():
    def __init__ (self, cedula, nombre_completo, edad, correo_electronico):
        self.cedula = cedula
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.correo_electronico = correo_electronico
        
    def mostrar_informacion(self):
        print(f"Cédula: {self.cedula}")
        print(f"Nombre: {self.nombre_completo}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo_electronico}") 


class Movimiento:
    def __init__(self, tipo, cantidad, moneda, descripcion):
        self.tipo = tipo
        self.cantidad = cantidad
        self.moneda = moneda
        self.descripcion = descripcion

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Cantidad: {self.cantidad:.2f} {self.moneda}")
        print(f"Descripción: {self.descripcion}")


class Prestamo:
    def __init__(self, tipo, monto, tasa_interes, plazo_meses, cliente):
        self.tipo = tipo
        self.monto = monto
        self.tasa_interes = tasa_interes
        self.plazo_meses = plazo_meses
        self.cliente = cliente
        self.saldo_pendiente = monto
        self.cuota = 0
    
    def calcular_cuota(self):
        tasa_mensual = self.tasa_interes / 100 / 12

        if self.plazo_meses <= 0:
            print("Error: el plazo debe ser mayor que cero.")
            return

        if tasa_mensual == 0:
            self.cuota = self.monto / self.plazo_meses
        else:
            self.cuota = (
                self.monto * tasa_mensual *
                (1 + tasa_mensual) ** self.plazo_meses
            ) / (
                (1 + tasa_mensual) ** self.plazo_meses - 1
            )
        return self.cuota
     
    def realizar_pago(self, cantidad):
     if cantidad <= 0:
        print("Error: el pago debe ser mayor que cero.")
        return

     if cantidad > self.saldo_pendiente:
        print("Error: el pago supera la deuda pendiente.")
        return

     self.saldo_pendiente -= cantidad

     print("Pago realizado correctamente.")
     print(f"Saldo pendiente: {self.saldo_pendiente:.2f} DOP")

class Tarjeta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.activa = True
        
class TarjetaDebito(Tarjeta):
    def __init__(self, numero, cliente, cuenta):
        super().__init__(numero, cliente)
        self.cuenta = cuenta
    
    
    def realizar_compra(self, cantidad):
     if not self.activa:
        print("Error: la tarjeta está inactiva.")
        return

     if cantidad <= 0:
        print("Error: la compra debe ser mayor que cero.")
        return

     if cantidad > self.cuenta.saldo:
        print("Error: saldo insuficiente.")
        return

     self.cuenta.retirar(cantidad)
     print("Compra realizada correctamente.")



class TarjetaCredito(Tarjeta):
    def __init__(self, numero, cliente, limite_credito):
        super().__init__(numero, cliente)
        self.limite_credito = limite_credito
        self.deuda = 0
    
    def realizar_compra(self, cantidad):
     if not self.activa:
        print("Error: la tarjeta está inactiva.")
        return

     if cantidad <= 0:
        print("Error: la compra debe ser mayor que cero.")
        return

     disponible = self.limite_credito - self.deuda

     if cantidad > disponible:
        print("Error: crédito insuficiente.")
        return

     self.deuda += cantidad
     print("Compra realizada correctamente.")
     print(f"Deuda actual: {self.deuda:.2f}")
     print(f"Crédito disponible: {disponible - cantidad:.2f}")
     
     
    def realizar_pago(self, cantidad):
     if cantidad <= 0:
        print("Error: el pago debe ser mayor que cero.")
        return

     if cantidad > self.deuda:
        print("Error: el pago supera la deuda actual.")
        return

     self.deuda -= cantidad

     print("Pago realizado correctamente.")
     print(f"Deuda actual: {self.deuda:.2f}")
     print(
        f"Crédito disponible: "
        f"{self.limite_credito - self.deuda:.2f}"
     )



                   
class Banco():
    def __init__ (self):
        self.clientes = []
        self.cuentas = []
        self.prestamos = []
        self.tarjetas = []
        
    def registrar_cliente(self,cliente):
        if self.buscar_cliente(cliente.cedula) is not None:
            print('Error, esas cedula ya esta registrada.')
            return
        self.clientes.append(cliente)
        print('Cliente registado correctamente.')

    def registrar_cuenta(self, cuenta):
        for c in self.cuentas:
            if c.numero_cuenta == cuenta.numero_cuenta:
                print('Error. Ese numero de cuenta ya existe.')
                return
        self.cuentas.append(cuenta)
        print('Cuenta registrada correctamente.')
            
    
    def buscar_cliente(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente
        
        return None
    
    def modificar_cliente(self, cedula, nombre, edad, correo):
        cliente = self.buscar_cliente(cedula)
        
        if cliente is None:
            print("Cliente no encontrado.")
            return
        
        cliente.nombre_completo = nombre
        cliente.edad = edad
        cliente.correo_electronico = correo
        
        print("Cliente modificado correctamente.")
        print("-" *50)
    
    def consultar_cliente(self, cedula):
        cliente = self.buscar_cliente(cedula)

        if cliente is None:
            print("Cliente no encontrado.")
            return

        cliente.mostrar_informacion()
        

    def mostrar_clientes(self):
        if not self.clientes:
            print('No hay clientes registrados.')
            return 
        
        for cliente in self.clientes:
            cliente.mostrar_informacion()
            print('-'*50)
            
    def mostrar_cuentas(self):
        if not self.cuentas:
            print("No hay cuentas registradas.")
            return

        for cuenta in self.cuentas:
            cuenta.mostrar_informacion()
            print("-" * 50)
    
    def registrar_prestamo(self, prestamo):
     self.prestamos.append(prestamo)
     print("Préstamo registrado correctamente.")

    def mostrar_prestamos(self):
     if not self.prestamos:
        print("No hay préstamos registrados.")
        return

     for prestamo in self.prestamos:
        print(f"Tipo: {prestamo.tipo}")
        print(f"Cliente: {prestamo.cliente.nombre_completo}")
        print(f"Monto: {prestamo.monto:.2f} DOP")
        print(f"Tasa anual: {prestamo.tasa_interes}%")
        print(f"Plazo: {prestamo.plazo_meses} meses")
        print(f"Cuota mensual: {prestamo.calcular_cuota():.2f} DOP")
        print(f"Saldo pendiente: {prestamo.saldo_pendiente:.2f} DOP")
        print("-" * 50)
        
    
    def registrar_tarjeta(self, tarjeta):
     for t in self.tarjetas:
        if t.numero == tarjeta.numero:
            print("Error: ese número de tarjeta ya existe.")
            return

     self.tarjetas.append(tarjeta)
     print("Tarjeta registrada correctamente.")

    def mostrar_tarjetas(self):
     if not self.tarjetas:
        print("No hay tarjetas registradas.")
        return

     for tarjeta in self.tarjetas:
        print(f"Número: {tarjeta.numero}")
        print(f"Titular: {tarjeta.cliente.nombre_completo}")
        print(f"Estado: {'Activa' if tarjeta.activa else 'Inactiva'}")

        if isinstance(tarjeta, TarjetaDebito):
            print("Tipo: Débito")
            print(f"Cuenta asociada: {tarjeta.cuenta.numero_cuenta}")

        elif isinstance(tarjeta, TarjetaCredito):
            print("Tipo: Crédito")
            print(f"Límite: {tarjeta.limite_credito:.2f}")
            print(f"Deuda: {tarjeta.deuda:.2f}")
            print(f"Disponible: {tarjeta.limite_credito - tarjeta.deuda:.2f}")

        print("-" * 40)

    def consultar_finanzas_cliente(self, cedula):
     cliente = self.buscar_cliente(cedula)

     if cliente is None:
        print("Cliente no encontrado.")
        return

     print("=" * 45)
     print("CONSULTA FINANCIERA DEL CLIENTE")
     print("=" * 45)

     cliente.mostrar_informacion()

     print("\n--- CUENTAS BANCARIAS ---")
     for cuenta in self.cuentas:
        if cuenta.titular.cedula == cedula:
            cuenta.mostrar_informacion()
            print("Movimientos:")
            cuenta.mostrar_movimientos()

     print("\n--- PRÉSTAMOS ---")
     for prestamo in self.prestamos:
        if prestamo.cliente.cedula == cedula:
            print(f"Tipo: {prestamo.tipo}")
            print(f"Monto inicial: {prestamo.monto:.2f}")
            print(f"Saldo pendiente: {prestamo.saldo_pendiente:.2f}")
            print(f"Cuota mensual: {prestamo.calcular_cuota():.2f}")
            print("-" * 30)

     print("\n--- TARJETAS ---")
     for tarjeta in self.tarjetas:
        if tarjeta.cliente.cedula == cedula:
            print(f"Número: {tarjeta.numero}")
            print(f"Estado: {'Activa' if tarjeta.activa else 'Inactiva'}")

            if isinstance(tarjeta, TarjetaDebito):
                print("Tipo: Débito")
                print(f"Cuenta asociada: {tarjeta.cuenta.numero_cuenta}")

            elif isinstance(tarjeta, TarjetaCredito):
                print("Tipo: Crédito")
                print(f"Límite: {tarjeta.limite_credito:.2f}")
                print(f"Deuda: {tarjeta.deuda:.2f}")
                print(f"Disponible: {tarjeta.limite_credito - tarjeta.deuda:.2f}")

            print("-" * 50)


            
banco = Banco()
     
cliente1 = Cliente(
        '202-6123567-8',
        'Jhansel Jazael Urena Mejia',
        25,
        'jhanseljazael@gmail.com'
    )
       
cliente2 = Cliente(
        '202-5024876-5',
        'Mario Torres Cepeda',
        19,
        'mario11@gmail.com'
        )

cliente3 = Cliente(
    '203-1123444-9',
    'Julio Bizcaino Cepo',
    23,
    'julio122@gmail.com'
)      


print('-'*50)
banco.registrar_cliente(cliente1)
banco.registrar_cliente(cliente2)
banco.registrar_cliente(cliente3)
banco.modificar_cliente(    
    '203-1123444-9',
    'Julio Bizcaino Cepo',
    26,
    'julio1@gmail.com'
)

banco.mostrar_clientes()
print('-'*50)
print('BUSCANDO CLIENTE:\n')
banco.consultar_cliente('203-1123444-9')
print('-'*50)

class Cuenta_bancaria():
    def __init__(self, numero_cuenta, tipo_cuenta, moneda, saldo, titular):
        if not isinstance(tipo_cuenta, TipoCuenta):
            raise ValueError("Tipo de cuenta no válido.")
        
        if not isinstance(moneda, Moneda):
            raise ValueError("Moneda no válida.")
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.moneda = moneda
        self.saldo = saldo
        self.titular = titular
        self.movimientos = []

        
    def registrar_movimiento(self, tipo, cantidad, descripcion):
     movimiento = Movimiento(
        tipo,
        cantidad,
        self.moneda,
        descripcion
    )
     self.movimientos.append(movimiento)
     
    def mostrar_informacion(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta.value}")
        print(f"Moneda: {self.moneda.value}")
        print(f"Saldo: {self.saldo:.2f} {self.moneda.value}")
        print(f"Titular: {self.titular.nombre_completo}")
    
    def depositar(self,cantidad):
        if cantidad<=0:
            print('Error: El monto no puede ser 0 o menor de 0.')
            return
        self.saldo += cantidad
        print("Depósito realizado correctamente.")
        print(f"Nuevo saldo: {self.saldo:.2f} {self.moneda.value}")
        print('-'*50)
        
        self.registrar_movimiento(
    "Depósito",
    cantidad,
    "Depósito realizado en la cuenta"
)
        
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return

        if cantidad > self.saldo:
            print("Error: fondos insuficientes.")
            return

        self.saldo -= cantidad
        print("Retiro realizado correctamente.")
        print(f"Nuevo saldo: {self.saldo:.2f} {self.moneda}")
        print('-'*50)
        
        self.registrar_movimiento(
    "Retiro",
    cantidad,
    "Retiro realizado de la cuenta"
)
        
    
    def transferir(self, cuenta_destino, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return

        if self.numero_cuenta == cuenta_destino.numero_cuenta:
            print("Error: no puedes transferir a la misma cuenta.")
            return

        if self.moneda != cuenta_destino.moneda:
            print("Error: las cuentas deben usar la misma moneda.")
            return

        if cantidad > self.saldo:
            print("Error: fondos insuficientes.")
            return

        self.saldo -= cantidad
        cuenta_destino.saldo += cantidad
        print('-'*50)
        print("Transferencia realizada correctamente.")
        print('-'*50)
        
        self.registrar_movimiento(
    "Transferencia enviada",
    cantidad,
    f"Transferencia a la cuenta {cuenta_destino.numero_cuenta}"
)
        cuenta_destino.registrar_movimiento(
    "Transferencia recibida",
    cantidad,
    f"Transferencia desde la cuenta {self.numero_cuenta}"
    )

    def mostrar_movimientos(self):
        if not self.movimientos:
            print("Esta cuenta no tiene movimientos.")
            return

        for movimiento in self.movimientos:
         movimiento.mostrar_informacion()
         print("-" * 50)
    

        
cuenta1 = Cuenta_bancaria(
    "1001",
    TipoCuenta.AHORRO,
    Moneda.DOP,
    5000,
    cliente1
)

cuenta2 = Cuenta_bancaria(
    "2002",
    TipoCuenta.CORRIENTE,
    Moneda.DOP,
    20000,
    cliente2
)

cuenta3= Cuenta_bancaria(
    "1333",
    TipoCuenta.CORRIENTE,
    Moneda.USD,
    1000,
    cliente3
)

prestamo1 = Prestamo(
    "Personal",
    100000,
    12,
    24,
    cliente1
)


banco.registrar_cuenta(cuenta1)
banco.registrar_cuenta(cuenta2)
banco.registrar_cuenta(cuenta3)
print("-"*50)
banco.mostrar_cuentas()
cuenta1.retirar(1000)
cuenta1.depositar(3000)
cuenta1.transferir(cuenta2, 500)
banco.mostrar_cuentas()
cuenta1.mostrar_movimientos()
cuenta2.mostrar_movimientos()
cuenta3.mostrar_movimientos()
print('-'*50)
prestamo1.realizar_pago(5000)
print(f"Cuota mensual: {prestamo1.calcular_cuota():.2f} DOP")
print('='*50)
banco.registrar_prestamo(prestamo1)
banco.mostrar_prestamos()
tarjeta1 = TarjetaDebito("TD1001", cliente1, cuenta1)
tarjeta2 = TarjetaCredito("TC1001", cliente2, 20000)

banco.registrar_tarjeta(tarjeta1)
banco.registrar_tarjeta(tarjeta2)
print('-'*50)

banco.mostrar_tarjetas()
banco.consultar_finanzas_cliente("202-6123567-8")