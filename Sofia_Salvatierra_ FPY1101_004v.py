import datetime
import json

ventas=[]

precio_pizzas={
    "Cuatro quesos":{"Pequeña":6000,"mediana":9000,"familiar":12000},
    "Hawaiana":{"Pequeña":6000,"mediana":9000,"familiar":12000},
    "Napolitana":{"Pequeña":5500,"mediana":8500,"familiar":11000},
    "Pepperoni":{"Pequeña":7000,"mediana":10000,"familiar":13000}
}

def menu():
    print("\n***VENTA PIZZA DUOC***\n")
    print("1.Registrar una venta")
    print("2.Mostrar todas las ventas")
    print("3.Buscar ventas por cliente")
    print("4.Guardar las ventas en un archivo")
    print("5.Cargar las ventas desde un archivo")
    print("6.Generar boleta")
    print("7.Anular venta") 
    print("8.Salir del programa")
    opcion=input("seleccione una opcion:")
    return opcion
    
def registrar_venta():
    cliente=input('ingrese el nombre del cliente: ')
    tipo_usuario=input('A que jornada corresponde(vespertino/diurno/administrativo)').lower()
    tipo_pizza=input(' ingrese tipo de pizza quiere (cuatro quesos/hawaiana/napolitana/pepperoni):').lower()
    tamaño_pizza=input('ingrese el tamaño de la pizza (pequeña/mediana/familiar):').lower()
    
    if tipo_pizza not in precio_pizzas or tamaño_pizza not in precio_pizzas[tipo_pizza]:
        print("opcion invalida.")
        return
    precio_unitario = precio_pizzas[tipo_pizza][tamaño_pizza]
    
    descuento=0 
    if tipo_usuario == 'diurno':
        descuento= 0.12
    elif tipo_usuario == 'vespertino':
        descuento = 0.14
    elif tipo_usuario == 'administrativo':
        descuento = 0.10
        
    precio_final= precio_unitario * (1 - descuento)
    
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    venta = {
        'cliente': cliente,
        'tipo_cliente': tipo_usuario,
        'tipo_pizza': tipo_pizza,
        'tamaño_pizza': tamaño_pizza,
        'cantidad': cantidad,
        'precio_final': precio_final
    }
    ventas.append(venta)
    print('venta registrada exitosamente')
    
def Mostrar_todas_las_ventas():
    if not ventas:
        print("no hay ventas registradas")
    for venta in ventas:
        print(venta)

def buscar_venta():
    buscar_cliente=input('ingrese el nombre del cliente a buscar: ').lower()
    ventas_encontradas=[venta for venta in ventas if venta ['cliente'] == buscar_cliente]
    
    if ventas_encontradas:
        for venta in ventas_encontradas:
            print(venta)
    else:
        print(f"no se encontro venta para este usuario {buscar_cliente}")
        
def guardar_venta_en_archivo():
    with open ('ventas.json' , 'w')as archivo:
        json.dump(ventas,archivo)
        print("¡venta guardada con exito!")
        
def cargar_venta_en_archivo():
    global ventas
    try:
        with open ('ventas.json', 'r') as archivo:
            ventas=json.load(archivo)
            print("venta cargada en un archivo")
    except FileNotFoundError:
        print("No se encontro ningun archivo de ventas")
        
def generar_boleta():
    cliente = input('ingrese nombre del cliente: ')
    ventas_cliente=[venta for venta in ventas if venta['cliente']== cliente]
    if ventas_cliente:
        total= sum(venta['precio_final'] for venta in ventas_cliente)
        print('\nBoleta: ')
        print(f'cliente: {cliente}')
        print(f'fecha: {datetime.datetime.now()}')
        print('Detalle de compras: ')
        for venta in ventas_cliente:
            print(f"{venta['tipo_pizza']} - {venta['tamaño_pizza']} - ${venta['precio_final']}")
            print(f'Total a pagar: ${total}\n')
        else:
            print("no se encontro ninguna venta para este cliente.")
            
def anular_venta():
    print("venta anulada")
    
def main():
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
           Mostrar_todas_las_ventas()
        elif opcion == '3':
            buscar_venta()
        elif opcion == '4':
            guardar_venta_en_archivo()
        elif opcion == '5':
            cargar_venta_en_archivo()
        elif opcion == '6':
            generar_boleta()
        elif opcion == '7':
            anular_venta()
        elif opcion == '8':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()


    