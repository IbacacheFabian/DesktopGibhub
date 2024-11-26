class TarjetaCredito:
    # Inicializacion con valores predeterminados
    def __init__(self, saldo_pagar=0, limite_credito=1000, intereses=0.02):
        self.saldo_pagar = saldo_pagar  # Saldo actual de la tarjeta
        self.limite_credito = limite_credito  # Limite maximo de credito
        self.intereses = intereses  # Porcentaje de interes como decimal

    # Metodo para realizar una compra
    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            print('Compra realizada. Nuevo saldo a pagar: ${:.2f}'.format(self.saldo_pagar))
        else:
            print('Tarjeta Rechazada, has alcanzado tu limite de credito.')

    # Metodo para realizar un pago
    def pago(self, monto):
        if monto > 0:
            self.saldo_pagar -= monto
            if self.saldo_pagar < 0:
                self.saldo_pagar = 0
            print('Pago realizado. Nuevo saldo a pagar: ${:.2f}'.format(self.saldo_pagar))
        else:
            print("El monto del pago debe ser mayor que 0.")

    # Metodo para mostrar la informacion de la tarjeta
    def mostrar_info_tarjeta(self):
        print("Saldo a pagar: ${:.2f}".format(self.saldo_pagar))
        print("Limite de credito: ${:.2f}".format(self.limite_credito))
        print("Tasa de interes: {:.2f}%".format(self.intereses * 100))

    # Metodo para cobrar intereses
    def cobrar_interes(self):
        if self.saldo_pagar > 0:
            intereses_cobrados = self.saldo_pagar * self.intereses
            self.saldo_pagar += intereses_cobrados
            print("Intereses cobrados: ${:.2f}".format(intereses_cobrados))
            print("Nuevo saldo a pagar: ${:.2f}".format(self.saldo_pagar))
        else:
            print("No hay saldo pendiente para cobrar intereses.")


class Usuario:
    def __init__(self, nombre, tarjetas=None):
        self.nombre = nombre
        self.tarjetas = tarjetas if tarjetas else []  # Lista de tarjetas de credito

    def agregar_tarjeta(self, tarjeta):
        """Agrega una tarjeta a la lista de tarjetas del usuario."""
        self.tarjetas.append(tarjeta)
        print('Tarjeta agregada para: {}'.format(self.nombre))

    def hacer_compra(self, monto, tarjeta_index=0):
        """
        Realiza una compra en una tarjeta especifica.
        Parametros:
        - monto: el monto de la compra.
        - tarjeta_index: indice de la tarjeta en la lista (por defecto, la primera tarjeta).
        """
        if 0 <= tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].compra(monto)
        else:
            print("Error: Indice de tarjeta invalido.")
        return self

    def pagar_tarjeta(self, monto, tarjeta_index=0):
        """
        Realiza un pago a una tarjeta especifica.
        Parametros:
        - monto: el monto del pago.
        - tarjeta_index: indice de la tarjeta en la lista (por defecto, la primera tarjeta).
        """
        if 0 <= tarjeta_index < len(self.tarjetas):
            self.tarjetas[tarjeta_index].pago(monto)
        else:
            print("Error: Indice de tarjeta invalido.")
        return self

    def mostrar_saldo_usuario(self):
        """Muestra el saldo de todas las tarjetas del usuario."""
        print('Usuario {}'.format(self.nombre))
        for i, tarjeta in enumerate(self.tarjetas):
            print('Tarjeta ${:.2f}'.format(i + 1))
            tarjeta.mostrar_info_tarjeta()

# Ejemplo de uso
from decimal import Decimal

# Crear tarjetas de credito
tarjeta1 = TarjetaCredito(saldo_pagar=0, limite_credito=1000, intereses=0.02)
tarjeta2 = TarjetaCredito(saldo_pagar=50, limite_credito=2000, intereses=0.03)

# Crear usuario y asociar tarjetas
usuario = Usuario("Carlos")
usuario.agregar_tarjeta(tarjeta1)
usuario.agregar_tarjeta(tarjeta2)

# Hacer compras y pagos
usuario.hacer_compra(200, tarjeta_index=0).pagar_tarjeta(50, tarjeta_index=0)
usuario.hacer_compra(500, tarjeta_index=1).pagar_tarjeta(300, tarjeta_index=1)

# Mostrar saldos
usuario.mostrar_saldo_usuario()
