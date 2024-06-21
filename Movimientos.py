class ConsultasYMovimientos:
    
    def __init__(self):
        self.saldoT = 0  
        self.movimientos = []
        
    def Consignar(self):
        self.sumar = int(input("Digite la cantidad a consignar: "))
        self.saldoT += self.sumar  # Sumamos la cantidad consignada al saldo total
        self.movimientos.append((self.sumar, "consignacion"))
        
    def Retirar(self):
        self.cantR = int(input("Digite la cantidad a retirar: "))
        
        if self.saldoT >= self.cantR:  # Verificamos si hay suficiente saldo para el retiro
            self.saldoT -= self.cantR  # Restamos la cantidad retirada del saldo total
            print(f"Se ha retirado {self.cantR} y queda {self.saldoT}")
            self.movimientos.append((self.cantR, "retiro"))
        else:
            print("Saldo insuficiente")
    
    def ConsultarSaldo(self):
        print(f"Su saldo es: {self.saldoT}")
    
    def Consultar_movimientos(self):
        print("Movimientos realizados:")
        for monto, tipo in self.movimientos:
            print(f"Tipo: {tipo}, Monto: {monto}")

def mostrar_menus():
    consulta_movimientos = ConsultasYMovimientos()
    
    while True:
        print("\nMenú de Operaciones:")
        print("1. Consignar")
        print("2. Retirar")
        print("3. Consultar Saldo")
        print("4. Consultar Movimientos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            consulta_movimientos.Consignar()
        elif opcion == '2':
            consulta_movimientos.Retirar()
        elif opcion == '3':
            consulta_movimientos.ConsultarSaldo()
        elif opcion == '4':
            consulta_movimientos.Consultar_movimientos()
        elif opcion == '5':
            print("Gracias por usar nuestro servicio.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-5).")


mostrar_menus()