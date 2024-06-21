import random

# Diccionario para almacenar departamentos y capitales
Departamentos = {}

# Ciclo para ingresar departamentos y capitales
while True:
    departamento = input("Ingrese el nombre del departamento (o escriba 'salir' para terminar): ")
    
    if departamento.lower() == 'salir':
        break
    
    capital = input(f"Ingrese la capital de {departamento}: ")
    
    Departamentos[departamento] = capital

# Ciclo para imprimir departamento y capital
print("\nListado de Departamentos y Capitales:")
for depto, capital in Departamentos.items():
    print(f"{depto}: {capital}")

# Selección aleatoria de un departamento
departamento_aleatorio = random.choice(list(Departamentos.keys()))
capital_correcta = Departamentos[departamento_aleatorio]

# Validación de la capital con tres intentos
print(f"\nSe ha seleccionado aleatoriamente el departamento '{departamento_aleatorio}'.")
intentos = 3  # Cambio a tres intentos

for intento in range(1, intentos + 1):
    capital_ingresada = input(f"Ingrese la capital de '{departamento_aleatorio}' (Intento {intento}): ")
    
    if capital_ingresada.lower() == capital_correcta.lower():
        print("¡Correcto!")
        break
    elif capital_ingresada.lower() == 'salir':
        print("¡Hasta luego!")
        break
    else:
        if intento < intentos:
            print("Capital incorrecta. Intenta nuevamente.")
        else:
            print("Hasta luego. Has agotado tus intentos.")

