



class  Logearse: 
    def __init__(self) :
     self.idetificacion= None
     self.correo = None    
     self.usuario=None
     self.clave=None
     self.confirmar=None
     self.estado=False
     
    def Registrar(self):
        print("Ingrese la siguiente informacion:")
        self.idetificacion=input("Ingrese su identificacion: ")

        self.usuario=input("Ingrese su nombre de usuario: ")

        x=0
        while x ==0:
            
           self.correo =input("Ingrese su correo: ")
           if "@" in self.correo:
               print("correo valido")
               break
           else:
                print("correo no valido")
        
        y=0
        while y==0:
            
            self.clave=input("ingrese su clave: ")
            self.confirmar=input("confirme su clave: ")  
            if self.clave==self.confirmar:
                print("Las contraseñas conciden")
                break
            else:  
                print("las contraseñas no coinciden")
    
    def IniciarSesion(self):
        
        print("Iniciar Sesión")
        
        
        i=0
        while i<1:
           user= input("ingrese su usuario: ")
           password =input("ingrese su clave: ")
           if user == self.usuario and password== self.clave:
               print("inicio de sesion correcto")
              
               self.estado=True
               
               break
           else:
               print("el usuario o la contraseña son incorrectos")
               
     
  

x=Logearse()    



def mostrar_menu():
    print("*" * 17)
    print("Menú:".center(17))
    print("*" * 17)
    print("|1. Registrar     |")
    print("|2. IniciarSesion |")
    print("|3. Salir         |")
    print("-" * 17)



def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
           x.Registrar()
        elif opcion == "2":
         x.IniciarSesion()
         if x.estado==True:
            from Movimientos import mostrar_menus 

         
         
     
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
 main()