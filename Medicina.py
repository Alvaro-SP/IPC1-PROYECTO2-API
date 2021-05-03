class Medicina:      
    def __init__(self,nombre,price,descrip,cantidad):
        self.nombre = nombre #self=this
        self.price = price
        self.descrip = descrip
        self.cantidad = cantidad #self=this
       
       

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getNombre(self):
        return self.nombre
    
    def getPrice(self):
        return self.price
    
    def getDescrip(self):
        return self.descrip

    def getCantidad(self):
        return self.cantidad
    


    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPrice(self, price):
        self.price = price
    
    def setDescrip(self, descrip):
        self.descrip = descrip

    def setCantidad(self, cantidad):
        self.cantidad = cantidad
  