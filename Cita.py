class Cita:      
    def __init__(self,nombre,idpaciente,datehour,motivo,estado,doctor):
        self.nombre = nombre #self=this
        self.idpaciente = idpaciente
        self.datehour = datehour
        self.motivo = motivo #self=this
        self.estado = estado
        self.doctor = doctor
    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getNombre(self):
        return self.nombre
    
    def getIdpaciente(self):
        return self.idpaciente
    
    def getDatehour(self):
        return self.datehour

    def getMotivo(self):
        return self.motivo
        
    def getEstado(self):
        return self.estado

    def getCoctor(self):
        return self.doctor
    


    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setIdpaciente(self, idpaciente):
        self.idpaciente = idpaciente
    
    def setDatehour(self, datehour):
        self.datehour = datehour

    def setMotivo(self, motivo):
        self.motivo = motivo

    def setEstado(self, estado):
        self.estado = estado

    def setDoctor(self, doctor):
        self.doctor = doctor