
class Paciente:      
    def __init__(self,nombre,apellido,nacimiento,sexo,username,contra):
        self.nombre = nombre 
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.sexo = sexo 
        self.username = username
        self.contra = contra

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getNacimiento(self):
        return self.nacimiento

    def getSexo(self):
        return self.sexo
    
    def getUsername(self):
        return self.username
    
    def getContra(self):
        return self.contra

    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setNacimiento(self, nacimiento):
        self.nacimiento = nacimiento

    def setSexo(self, sexo):
        self.sexo = sexo
    
    def setUsername(self, username):
        self.username = username
    
    def setContra(self, contra):
        self.contra = contra