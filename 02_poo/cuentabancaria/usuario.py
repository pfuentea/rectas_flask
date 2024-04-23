from cuentabancaria import CuentaBancaria

class Usuario:
    
    def __init__(self,p_u_nombre, p_u_tasa_interes, p_u_balance):
        self.nombre = p_u_nombre
        cuenta_nueva = CuentaBancaria(p_u_tasa_interes, p_u_balance)
        self.cuenta = cuenta_nueva


        #self.cuenta=[] # generar una lista vacia que tendra multiples cuentas

        #self.cuenta.append(cuenta_nueva)

    def crear_cuenta_nueva(self,p_u_tasa_interes, p_u_balance):
        cuenta_nueva = CuentaBancaria(p_u_tasa_interes, p_u_balance)

        self.cuenta.append(cuenta_nueva)



    def recibir_deposito(self,p_monto):
        self.cuenta.deposito(p_monto)

    def hacer_retiro(self,p_monto):
        self.cuenta.retiro(p_monto)

    def hacer_transferencia(self,p_cuenta_destino,p_monto):
        self.cuenta.retiro(p_monto)
        p_cuenta_destino.cuenta.deposito(p_monto)

    def mostrar_balance_usuario(self):
        print(f"El cliente {self.nombre} cuenta con el siguiente balance:{self.cuenta.get_balance()}")
        
        #self.cuenta.mostrar_info_cuenta()



    







    

