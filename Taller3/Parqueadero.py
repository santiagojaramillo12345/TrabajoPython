from datetime import datetime
import random
import math

# Definir cuantos cupos tiene el parqueadero en motos y carros
print("////BIENVENIDO AL SISTEMA DE PARQUEADEROS GALVIS////")
print("----------------------------------------------------")
camp_cars = int(input('Ingresa la cantidad de parqueaderos para carros: '))
camp_motorcycles = int(input('Ingresa la cantidad de parqueaderos para motos: '))

# Definir los campos del parqueadero
name_camp_cars = []
name_camp_moto = []

while len(name_camp_cars) < camp_cars:
    name_camp_cars.append({'place': str(input('Ingresa el nombre del campo del parqueadero de carro: ')), 'available': True})

while len(name_camp_moto) < camp_motorcycles:
    name_camp_moto.append({'place': str(input('Ingresa el nombre del campo del parqueadero de moto: ')), 'available': True})

# Definir tarifa de cobro por tiempo
cost_frac_car = 2000
cost_frac_moto = 1000

# Registrar entrada de vehiculo o cobrar parqueadero
register_car = []
register_motorcycle = []

while True:
    # Recorrer un for dentro de una lista para consultar los diccionarios que hay
    place_free_moto = [x['place'] for x in name_camp_moto if x['available']]
    place_free_car = [x['place'] for x in name_camp_cars if x['available']]
    print("Lugares disponibles: ", place_free_car, place_free_moto)

    print("¿QUÉ OPCIÓN DESEAS REALIZAR?")
    options = input('1. Registrar nuevo vehiculo \n2. Registrar salida de vehiculo::\n3. salir\nOpción >: ')

    # Validar que el dato no sean letras
    if options.isdigit() and options not in ['1', '2','3']:
        print('NO SE ADMITEN LETRAS. SOLO LAS OPCIONES 1 o 2')
    elif options == '3':
                print("saliendo del menu ") 
                break
    # Opción para registrar Vehículo
    elif options == '1':
        if len(place_free_moto) > 0 or len(place_free_car) > 0:
            type_vehicle = input('¿QUÉ TIPO DE VEHÍCULO DESEAS REGISTRAR?\n1. Moto\n2. Carro\nOpción >: ')

            if type_vehicle.isdigit() and type_vehicle not in ['1', '2']:
                print('NO SE ADMITEN LETRAS. SOLO LAS OPCIONES 1 o 2')

            # Registrar Moto
            elif type_vehicle == '1' and len(place_free_moto) > 0:
                placa = str(input('POR FAVOR INGRESA LA PLACA DEL VEHÍCULO >: '))
                hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
                place_random = random.choice(place_free_moto)
                register_motorcycle.append({'place': place_random, 'placa': placa, 'hora de ingreso': hour_inside, 'Accion': 'Entro'})
                
                for x in name_camp_moto:
                    if x['place'] == place_random:
                        x['available'] = False
                
                print('El registro de vehículos es el siguiente: ', register_motorcycle)

            # Registrar Carro
            elif type_vehicle == '2' and len(place_free_car) > 0:
                placa = str(input('POR FAVOR INGRESA LA PLACA DEL VEHÍCULO >: '))
                hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
                place_random = random.choice(place_free_car)
                register_car.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})
                
                for x in name_camp_cars:
                    if x['place'] == place_random:
                        x['available'] = False
                
                print('El registro de vehículos es el siguiente: ', register_car)

        elif len(place_free_moto) == 0:
            print('PARQUEADERO DE MOTOS LLENO')
        elif len(place_free_car) == 0:
            print('PARQUEADERO DE CARROS LLENO')

    # Opción de retirar un vehículo, aquí se dirá cuanto se cobra y cuanto
    elif options == '2':
        # Juntar las dos listas para buscar el registro en una sola lista
        option_cash = input('POR FAVOR DIGITE EL TIPO DE VEHÍCULO A COBRAR\n1. Moto\n2. Carro\nOpción: ')

        if option_cash.isdigit() and option_cash not in ['1', '2']:
            print('NO SE ADMITEN LETRAS. SOLO LAS OPCIONES 1 o 2')

        # Registrar salida de una moto
        if option_cash == '1':
            placa_pay = str(input('POR FAVOR DIGITE LA PLACA A COBRAR: '))

            if not any(x['placa'] == placa_pay and x['Action'] == 'Entro' for x in register_motorcycle):
                print('LA PLACA CONSULTADA NO FUE ENCONTRADA')
                continue

            hour_inside = next(x['hour_inside'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro')
            place_out = next(x['place'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro')

            # Calcular tiempo de cobro
            hour_now = datetime.now().strftime('%Y-%m-%d %H:%M')
            total = (datetime.strptime(hour_now, '%Y-%m-%d %H:%M') - datetime.strptime(str(hour_inside), '%Y-%m-%d %H:%M')).total_seconds() / 3600
            total = math.ceil(total) * cost_frac_moto
            print('Tu valor a pagar de parqueo es => ', total)

            # Liberar parqueadero
            for x in name_camp_moto:
                if x['place'] == place_out:
                    x['available'] = True

            # Actualizar registro de salida
            for x in register_motorcycle:
                if x['placa'] == placa_pay:
                    x['hour_out'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    x['pay_all'] = total
                    x['Action'] = 'Salio'

            print('Los vehículos motorizados registrados son los siguientes: ', register_motorcycle)

        # Registrar salida de un carro
        elif option_cash == '2':
            placa_pay = str(input('POR FAVOR DIGITE LA PLACA A COBRAR: '))

            if not any(x['placa'] == placa_pay and x['Action'] == 'Entro' for x in register_car):
                print('LA PLACA CONSULTADA NO FUE ENCONTRADA')
                continue

            hour_inside = next(x['hour_inside'] for x in register_car if x['placa'] == placa_pay and x['Action'] == 'Entro')
            place_out = next(x['place'] for x in register_car if x['placa'] == placa_pay and x['Action'] == 'Entro')

            # Calcular tiempo de cobro
            hour_now = datetime.now().strftime('%Y-%m-%d %H:%M')
            total = (datetime.strptime(hour_now, '%Y-%m-%d %H:%M') - datetime.strptime(str(hour_inside), '%Y-%m-%d %H:%M')).total_seconds() / 3600
            total = math.ceil(total) * cost_frac_car
            print('Tu valor a pagar de parqueo es => ', total)

            # Liberar parqueadero
            for x in name_camp_cars:
                if x['place'] == place_out:
                    x['available'] = True

            # Actualizar registro de salida
            for x in register_car:
                if x['placa'] == placa_pay:
                    x['hour_out'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    x['pay_all'] = total
                    x['Action'] = 'Salio'

            print('Los vehículos registrados son los siguientes: ', register_car)

        else:
            print('POR FAVOR INTRODUZCA UNA SELECCIÓN VÁLIDA')

    else:
        print('POR FAVOR INTRODUZCA UNA SELECCIÓN VÁLIDA')
