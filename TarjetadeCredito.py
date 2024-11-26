class TarjetaCredito:
    def __init__(self, saldo_pagar=0, limite_credito=1000, intereses=0.02):
        self.saldo_pagar = saldo_pagar  # Saldo actual
        self.limite_credito = limite_credito  # Limite maximo de credito
        self.intereses = intereses  # interes como decimal

    # compra
    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            print('Compra realizada. Nuevo saldo a pagar: ${:.2f}'.format(self.saldo_pagar))
        else:
            print('Tarjeta Rechazada, has alcanzado tu limite de credito.')
        return self 

    # pago
    def pago(self, monto):
        if monto > 0:
            self.saldo_pagar -= monto #disminuye saldo
            if self.saldo_pagar < 0:
                self.saldo_pagar = 0 
            print('Pago realizado. Nuevo saldo a pagar: ${:.2f}'.format(self.saldo_pagar))
        else:
            print("El monto del pago debe ser mayor que 0.")  
        return self  

    # Mostras Info tarjeta
    def mostrar_info_tarjeta(self):
        print("Saldo a Pagar: ${:.2f}".format(self.saldo_pagar))
        return self 

    # Cobro intereses
    def cobrar_interes(self):
        if self.saldo_pagar > 0:
            intereses_cobrados = self.saldo_pagar * self.intereses  # Calcular intereses
            self.saldo_pagar += intereses_cobrados 
            print("Intereses cobrados: ${:.2f}".format(intereses_cobrados))
            print("Nuevo saldo a pagar: ${:.2f}".format(self.saldo_pagar))
        else:
            print("No hay saldo pendiente para cobrar intereses.")  
        return self 


# Crear las 3 tarjetas
tarjeta1 = TarjetaCredito(saldo_pagar=100, limite_credito=500, intereses=0.03)  # Tarjeta 1
tarjeta2 = TarjetaCredito(saldo_pagar=250, limite_credito=1000, intereses=0.02)  # Tarjeta 2
tarjeta3 = TarjetaCredito(saldo_pagar=50, limite_credito=300, intereses=0.05)  # Tarjeta 3


tarjeta1.compra(150).compra(200).pago(50).cobrar_interes().mostrar_info_tarjeta()

tarjeta2.compra(100).compra(200).compra(150).pago(100).pago(50).cobrar_interes().mostrar_info_tarjeta()

tarjeta3.compra(100).compra(50).compra(70).compra(30).compra(100).mostrar_info_tarjeta()
