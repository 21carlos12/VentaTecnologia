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
        
