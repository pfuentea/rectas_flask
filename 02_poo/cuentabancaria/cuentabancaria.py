class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, p_tasa_interes, p_balance=0): 
        self.balance=p_balance
        self.tasa_interes=p_tasa_interes
        
    
    def deposito(self, amount):
        if amount > 100:
            amount-=5
        elif amount > 500:
            amount-=10
        elif amount > 5000:
            amount-=20
        # 100 validaciones

        self.balance+=amount # self.balance = self.balance + amount
        return self

    def retiro(self, amount):
        if self.balance > amount:
            self.balance-=amount # self.balance = self.balance - amount
        else:
            self.balance-=5
            print("Fondos insuficientes: cobrando una tarifa de $5")
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance:{self.balance}")
        return self

    def generar_interes(self):
        if self.balance >0:
            self.balance+=self.balance*self.tasa_interes
        return self
    
    def get_balance(self):
        return self.balance
    
    def get_tasa(self):
        return self.tasa_interes




