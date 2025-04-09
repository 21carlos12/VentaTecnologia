from producto import Producto

class Smartphone(Producto):
    def _init_(self, id, nombre, precio, stock, marca, modelo):
        super()._init_(id, nombre, precio, stock)
        self.__marca = marca
        self.__modelo = modelo
    
    def aplicar_descuento(self, porcentaje):
        nuevo_precio = self.get_precio() * (1 - porcentaje/100)
        self.set_precio(nuevo_precio)
        return nuevo_precio
    
    def _str_(self):
        return f"{super()._str()} - {self.marca} {self._modelo}"
    