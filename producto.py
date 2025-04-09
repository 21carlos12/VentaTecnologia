class Producto:
    def _init_(self, id, nombre, precio, stock):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        
    def get_precio(self):
        return self.__precio
        
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
            
    def get_stock(self):
        return self.__stock
    
    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False
    
    def _str_(self):
        return f"{self._nombre} - ${self.precio} (Stock: {self._stock})"