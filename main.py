from smartphone import Smartphone
from computadora import Computadora

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Mostrar todos los productos")
    print("2. Aplicar descuento a smartphone")
    print("3. Actualizar especificación de computadora")
    print("4. Vender producto")
    print("5. Salir")

def main():
    # Crear productos iniciales
    productos = [
        Smartphone(1, "iPhone 15", 999.99, 10, "Apple", "15 Pro"),
        Smartphone(2, "Galaxy S23", 799.99, 8, "Samsung", "S23 Ultra"),
        Computadora(3, "MacBook Pro", 1499.99, 5, "Laptop", "M3"),
        Computadora(4, "Surface Pro", 1299.99, 7, "Tablet", "i7")
    ]

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- PRODUCTOS DISPONIBLES ---")
            for producto in productos:
                print(producto)
        
        elif opcion == "2":
            print("\n--- APLICAR DESCUENTO A SMARTPHONE ---")
            smartphones = [p for p in productos if isinstance(p, Smartphone)]
            for i, phone in enumerate(smartphones, 1):
                print(f"{i}. {phone}")
            
            try:
                seleccion = int(input("Seleccione un smartphone: ")) - 1
                descuento = float(input("Ingrese el porcentaje de descuento: "))
                smartphones[seleccion].aplicar_descuento(descuento)
                print(f"Nuevo precio: {smartphones[seleccion].get_precio()}")
            except (ValueError, IndexError):
                print("Selección inválida")
        
        elif opcion == "3":
            print("\n--- ACTUALIZAR COMPUTADORA ---")
            computadoras = [p for p in productos if isinstance(p, Computadora)]
            for i, comp in enumerate(computadoras, 1):
                print(f"{i}. {comp}")
            
            try:
                seleccion = int(input("Seleccione una computadora: ")) - 1
                nuevo_procesador = input("Ingrese el nuevo procesador: ")
                computadoras[seleccion].actualizar_especificacion(nuevo_procesador)
                print("¡Especificación actualizada!")
            except (ValueError, IndexError):
                print("Selección inválida")
        
        elif opcion == "4":
            print("\n--- VENDER PRODUCTO ---")
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto}")
            
            try:
                seleccion = int(input("Seleccione un producto: ")) - 1
                cantidad = int(input("Ingrese la cantidad a vender: "))
                if productos[seleccion].vender(cantidad):
                    print("¡Venta realizada con éxito!")
                else:
                    print("No hay suficiente stock")
            except (ValueError, IndexError):
                print("Selección inválida")
        
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "_main_":
    main()