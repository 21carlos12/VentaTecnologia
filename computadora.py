from producto import Producto

class Computadora(Producto):
    def _init_(self, id, nombre, precio, stock, tipo, procesador):
        super()._init_(id, nombre, precio, stock)
        self.__tipo = tipo
        self.__procesador = procesador
    
    def actualizar_especificacion(self, procesador_nuevo):
        self.__procesador = procesador_nuevo
    
    def _str_(self):
        return f"{super()._str()} - {self.tipo} ({self._procesador})"