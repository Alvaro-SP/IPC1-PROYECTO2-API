from flask import Flask, jsonify, request
from flask_cors import CORS
from Paciente import Paciente
from Doctor import Doctor
from Enfermera import Enfermera
from Medicina import Medicina
from Pedido import Pedido
from Cita import Cita
import json
#MIS PERSONAS
Pacientes=[]
Enfermeras=[]
Doctores=[]
Medicinas=[]
Pedidos=[]
Citas=[]

#Pacientes.append(Paciente('Alvaro','Socop','EN DICIEMBREW','M','yo','12345678'))
#Doctores.append(Doctor('Hugo','Chavez','hola','M','logdoc','12345678','cirujano'))
#Enfermeras.append(Enfermera('Juanita','del Barrio','en abril','F','lognurse','12345678'))
Medicinas.append(Medicina('Enalopril','18','Para la pansa creo xd','8'))
Medicinas.append(Medicina('Alkad','18','Para la pansa creo xd','8'))
Medicinas.append(Medicina('Marihuanol','18','Para la pansa creo xd','8'))
Medicinas.append(Medicina('Alkaseltzer','18','Para matar la cruda por tomar mucho por ella','3'))
#Pacientes.append(Paciente('Richard','Arjona','15/04/2021','F','fuiste tu','12345678'))
#Doctores.append(Doctor('Gerardi','Chello','14/06/2007','M','boby','12345678','ginecologo'))
#Enfermeras.append(Enfermera('Joseline','Socop','15/01/2005','F','Me gusta el Yorch','12345678'))
#Medicinas.append(Medicina('Diamenil','20','Para la diabetes creo xd','12'))
#Pacientes.append(Paciente('Pancha','Socop','Socop','Socop','Socop','Socop'))

'''---COMENTARIO TOQUE---'''
app = Flask(__name__)
CORS(app)

#██████████████████   PACIENTES    █████████████████████
#OBTENER LOS PACIENTES
@app.route('/Pacientes', methods=['GET'])
def getPacientes():    
    global Pacientes  
    Datos=[]
   
    for paciente in Pacientes:
        objeto = {
            'Nombre': paciente.getNombre(),
            'Apellido': paciente.getApellido(),
            'Fecha': paciente.getNacimiento(),
            'Sexo': paciente.getSexo(),
            'Username': paciente.getUsername(),
            'Contra': paciente.getContra()
        }
        
        Datos.append(objeto)
    return(jsonify(Datos))

#POSTEAR LOS PACIENTES DESDE EL LOGIN U OTRO
@app.route('/Pacientes', methods=['POST'])
def AgregarPaciente():
    global Pacientes
    nombre = request.json['Nombre']
    nombre=nombre.replace(" ","")
    apellido= request.json['Apellido']
    nacimiento = request.json['Fecha']
    sexo = request.json['Sexo']
    username = request.json['Usuario']
    contra = request.json['Contraseña']

    nuevo = Paciente(nombre,apellido,nacimiento,sexo,username,contra)
    Pacientes.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el Paciente exitosamente',})
 
#OBTENER UN DATO DE LOS PACIENTES   
@app.route('/Pacientes/login/<string:username>', methods=['GET'])
def ObtenerPacient(username): 
    global Pacientes  
    for paciente in Pacientes:
        if paciente.getUsername() == username :
            objeto = {
            'Nombre': paciente.getNombre(),
            'Apellido': paciente.getApellido(),
            'Fecha': paciente.getNacimiento(),
            'Sexo': paciente.getSexo(),
            'Username': paciente.getUsername(),
            'Contra': paciente.getContra(),
            'tipo':0
            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe el usuario con ese nombre"}

    return(jsonify(salida))

#OBTENER UN DATO DE LOS PACIENTES LOGEADOS
@app.route('/Pacientes/<string:nombre>', methods=['GET'])
def ObtenerUserPaciente(nombre): 
    global Pacientes
    for paciente in Pacientes:
        if paciente.getNombre() == nombre:
            objeto = {
            'Nombre': paciente.getNombre(),
            'Apellido': paciente.getApellido(),
            'Fecha': paciente.getNacimiento(),
            'Sexo': paciente.getSexo(),
            'Username': paciente.getUsername(),
            'Contra': paciente.getContra()
            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe el usuario con ese nombre"}

    return(jsonify(salida))

#ACTUALIZAR UN PACIENTE 
@app.route('/Pacientes/<string:nombre>', methods=['PUT'])
def ActualizarPaciente(nombre):    
    global Pacientes
    for i in range(len(Pacientes)):
        if nombre == Pacientes[i].getNombre():
            Pacientes[i].setNombre(request.json['nombre'])
            Pacientes[i].setApellido(request.json['apellido'])
            Pacientes[i].setNacimiento(request.json['fecha'])
            Pacientes[i].setSexo(request.json['sexo'])
            Pacientes[i].setUsername(request.json['usuario'])
            Pacientes[i].setContra(request.json['contra'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#ELIMINAR UN PACIENTE 
@app.route('/Pacientes/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global Pacientes    
    for i in range(len(Pacientes)):        
        if nombre == Pacientes[i].getNombre():            
            del Pacientes[i]            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})           
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

#██████████████████   DOCTORES █████████████████████
#OBTENER LOS DOCTORES
@app.route('/Doctores', methods=['GET'])
def getDoctores():
    global Doctores
    Datos=[]
    for doctor in Doctores:
        objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'Fecha': doctor.getNacimiento(),
            'Sexo': doctor.getSexo(),
            'Username': doctor.getUsername(),
            'Contra': doctor.getContra(),
            'Especialidad': doctor.getSpecialy()
        }
        Datos.append(objeto)
    print("Obteniendo Doctores")    
   #return("<h1>Obteniendo Doctores</h1>")
    return(jsonify(Datos))
#POSTEAR LOS DOCTORES
@app.route('/Doctores', methods=['POST'])
def AgregarDoctor():
    
    global Doctores
    nombre = request.json['Nombre']
    nombre=nombre.replace(" ","")
    apellido= request.json['Apellido']
    nacimiento = request.json['Fecha']
    sexo = request.json['Sexo']
    username = request.json['Usuario']
    contra = request.json['Contraseña']
    especialidad = request.json['Especialidad']
    nuevo = Doctor(nombre,apellido,nacimiento,sexo,username,contra,especialidad)
    Doctores.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el Doctor exitosamente',})
#OBTENER UN DATO DE LOS DOCTORES 
@app.route('/Doctores/<string:nombre>', methods=['GET'])
def ObtenerDoctor(nombre): 
    global Doctores
    for doctor in Doctores:
        if doctor.getNombre() == nombre:
            objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'Fecha': doctor.getNacimiento(),
            'Sexo': doctor.getSexo(),
            'Username': doctor.getUsername(),
            'Contra': doctor.getContra(),
            'Especialidad': doctor.getSpecialy()
            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe el usuario con ese nombre"}

    return(jsonify(salida))
#OBTENER UN DATO DE LOS DOCTORES LOGEADOS
@app.route('/Doctores/login/<string:username>', methods=['GET'])
def ObtenerUserDoctor(username): 
    global Doctores  
    for doctor in Doctores:
        if doctor.getUsername() == username :
            objeto = {
            'Nombre': doctor.getNombre(),
            'Apellido': doctor.getApellido(),
            'Fecha': doctor.getNacimiento(),
            'Sexo': doctor.getSexo(),
            'Username': doctor.getUsername(),
            'Contra': doctor.getContra(),
            'Especialidad': doctor.getSpecialy(),
            'Tipo':1
            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe el usuario con ese nombre"}

    return(jsonify(salida))

#ACTUALIZAR UN DOCTOR
@app.route('/Doctores/<string:nombre>', methods=['PUT'])
def ActualizarDoc(nombre):    
    global Doctores
    for i in range(len(Pacientes)):
        if nombre == Doctores[i].getNombre():
            Doctores[i].setNombre(request.json['nombre'])
            Doctores[i].setApellido(request.json['apellido'])
            Doctores[i].setNacimiento(request.json['fecha'])
            Doctores[i].setSexo(request.json['sexo'])
            Doctores[i].setUsername(request.json['usuario'])
            Doctores[i].setContra(request.json['contra'])
            Doctores[i].setContra(request.json['specialy'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#ELIMINAR UN DOCTORES 
@app.route('/Doctores/<string:nombre>', methods=['DELETE'])
def EliminarDoc(nombre):
    global Doctores    
    for i in range(len(Doctores)):        
        if nombre == Doctores[i].getNombre():            
            del Doctores[i]            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})           
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
    

#██████████████████   ENFERMERAS    █████████████████████

#OBTENER LOS ENFERMERAS
@app.route('/Enfermeras', methods=['GET'])
def getEnfermeras():
    global Enfermeras
    Datos=[]
    for enfermera in Enfermeras:
        objeto = {
            'Nombre': enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'Fecha': enfermera.getNacimiento(),
            'Sexo': enfermera.getSexo(),
            'Username': enfermera.getUsername(),
            'Contra': enfermera.getContra()
        }
        Datos.append(objeto)
    print("Obteniendo Enfermeras")        
    return(jsonify(Datos))

#POSTEAR LOS ENFERMERAS
@app.route('/Enfermeras', methods=['POST'])
def AgregarEnfermera():
    
    global Enfermeras
    nombre = request.json['Nombre']
    nombre=nombre.replace(" ","")
    apellido= request.json['Apellido']
    print(apellido)
    nacimiento = request.json['Fecha']
    sexo = request.json['Sexo']
    username = request.json['Usuario']
    contra = request.json['Contraseña']
    
    nuevo = Enfermera(nombre,apellido,nacimiento,sexo,username,contra)
    Enfermeras.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el Doctor exitosamente',})

#OBTENER UN DATO DE LOS ENFERMERAS
@app.route('/Enfermeras/<string:nombre>', methods=['GET'])
def ObtenerNurse(nombre): 
    global Enfermeras
    for enfermera in Enfermeras:
        if enfermera.getNombre() == nombre:
            objeto = {
            'Nombre': enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'Fecha': enfermera.getNacimiento(),
            'Sexo': enfermera.getSexo(),
            'Username': enfermera.getUsername(),
            'Contra': enfermera.getContra()

            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe el usuario con ese nombre"}

    return(jsonify(salida))

#OBTENER UN DATO DE LOS ENFERMERAS LOGEADOS
@app.route('/Enfermeras/login/<string:username>', methods=['GET'])
def ObtenerUserNurse(username): 
    global Enfermeras  
    for enfermera in Enfermeras:
        if enfermera.getUsername() == username :
            objeto = {
            'Nombre': enfermera.getNombre(),
            'Apellido': enfermera.getApellido(),
            'Fecha': enfermera.getNacimiento(),
            'Sexo': enfermera.getSexo(),
            'Username': enfermera.getUsername(),
            'Contra': enfermera.getContra(),
            'Tipo':2
            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe la Enfermera con ese nombre"}

    return(jsonify(salida))   

    #OBTENER MEDICINAS CARGADAS

#ACTUALIZAR UN ENFERMERAS 
@app.route('/Enfermeras/<string:nombre>', methods=['PUT'])
def ActualizarEnfermera(nombre):    
    global Enfermeras
    for i in range(len(Enfermeras)):
        if nombre == Enfermeras[i].getNombre():
            Enfermeras[i].setNombre(request.json['nombre'])
            Enfermeras[i].setApellido(request.json['apellido'])
            Enfermeras[i].setNacimiento(request.json['fecha'])
            Enfermeras[i].setSexo(request.json['sexo'])
            Enfermeras[i].setUsername(request.json['usuario'])
            Enfermeras[i].setContra(request.json['contra'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#ELIMINAR UN ENFERMERAS  
@app.route('/Enfermeras/<string:nombre>', methods=['DELETE'])
def EliminarEnfermera(nombre):
    global Enfermeras    
    for i in range(len(Enfermeras)):        
        if nombre == Enfermeras[i].getNombre():            
            del Enfermeras[i]            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})           
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
   


#██████████████████   MEDICINAS    █████████████████████
#OBTENER LOS MEDICINAS
@app.route('/Medicinas', methods=['GET'])
def getMedicinas():
    global Medicinas
    Datos=[]
    for medicina in Medicinas:
        objeto = {
            'Nombre': medicina.getNombre(),
            'Precio': medicina.getPrice(),
            'Descripcion': medicina.getDescrip(),
            'Cantidad': medicina.getCantidad()
           
        }
        Datos.append(objeto)
    print("Obteniendo Pacientes")    
    #return("<h1>Obteniendo pacientes</h1>")
    return(jsonify(Datos))
#POSTEAR LOS MEDICINAS
@app.route('/Medicinas', methods=['POST'])
def AgregarMedicina():
    
    global Medicinas
    nombre = request.json['Nombre']
    nombre=nombre.replace(" ","")
    price= request.json['Precio']
    descrip = request.json['Descripcion']
    cantidad = request.json['Cantidad']
    
    nuevo = Medicina(nombre,price,descrip,cantidad)
    Medicinas.append(nuevo)
    return jsonify({'Mensaje':'Se agrego la Medicina exitosamente',})
#OBTENER UN DATO DE LOS MEDICINAS
@app.route('/Medicinas/<string:nombre>', methods=['GET'])
def ObtenerMedicina(nombre): 
    global Medicinas
    for medicina in Medicinas:
        if medicina.getNombre() == nombre:
            objeto = {
            'Nombre': medicina.getNombre(),
            'Precio': medicina.getPrice(),
            'Descripcion': medicina.getDescrip(),
            'Cantidad': medicina.getCantidad()

            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe la medicina con ese nombre"}

    return(jsonify(salida))
#ACTUALIZAR UN MEDICINAS 
@app.route('/Medicinas/<string:nombre>', methods=['PUT'])
def ActualizarMedicina(nombre):    
    global Medicinas
    for i in range(len(Medicinas)):
        if nombre == Medicinas[i].getNombre():
            Medicinas[i].setNombre(request.json['nombre'])
            Medicinas[i].setPrice(request.json['precio'])
            Medicinas[i].setDescrip(request.json['descripcion'])
            Medicinas[i].setCantidad(request.json['cantidad'])
            
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#ELIMINAR UN MEDICINAS 
@app.route('/Medicinas/<string:nombre>', methods=['DELETE'])
def EliminarMedicina(nombre):
    global Medicinas    
    for i in range(len(Medicinas)):        
        if nombre == Medicinas[i].getNombre():            
            del Medicinas[i]            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})           
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
#AGREGAR POSTEAR LOS PEDIDOS     
@app.route('/Pedido', methods=['POST'])
def AgregarPedido():
    
    
    nombre2 = request.json['Nombre']
    
    global Medicinas
    
    for i in range(len(Medicinas)): 
        print("Medicinasi"+Medicinas[i].getNombre())
        print("-------------------"+nombre2)
        print("-------------------------------")       
        if nombre2 == Medicinas[i].getNombre():
            global Pedidos
            print("REALIZANDO EL POST DE LOS PEDIDOS")  
            nombre = request.json['Nombre']             
            price= Medicinas[i].getPrice()
            descrip = Medicinas[i].getDescrip()
            cantidad = Medicinas[i].getCantidad()            
            nuevo = Pedido(nombre,price,descrip,cantidad)
            Pedidos.append(nuevo)            
            return jsonify({'Mensaje':'Se agregó el pedido al Carrito.',})         
    return jsonify({'Mensaje':'No hay nada para agregar al carrito.',})
#OBTENER LOS PEDIDO 
@app.route('/Medicinas/Pedido', methods=['GET'])
def getPedidos():
    global Pedidos
    Datos=[]
    for pedido in Pedidos:
       
        objeto = {
            'Nombre': pedido.getNombre(),
            'Precio': pedido.getPrice(),
            'Descripcion': pedido.getDescrip(),
            'Cantidad': pedido.getCantidad()
           
        }
        Datos.append(objeto)
    print("Obteniendo los pedidos realizados")    
    #return("<h1>Obteniendo pacientes</h1>")
    return(jsonify(Datos))
#ELIMINAR UN PEDIDO 
@app.route('/Medicinas/Pedido/<string:nombre>', methods=['DELETE'])
def EliminarPedidos(nombre):
    global Pedidos    
    for i in range(len(Pedidos)):  
        print("eliminando *****")      
        if nombre == Pedidos[i].getNombre():            
            del Pedidos[i]            
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})           
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

#██████████████████   CITAS    █████████████████████
#OBTENER LAS CITAS
@app.route('/Citas', methods=['GET'])
def getCitas():
    global Citas
    Datos=[]
    for cita in Citas:
        objeto = {
            'Nombre': cita.getNombre(),
            'Idpaciente': cita.getIdpaciente(),
            'Datehour': cita.getDatehour(),
            'Motivo': cita.getMotivo(),
            'Estado': cita.getEstado(),
            'Doctor': cita.getEstado()
           
        }
        Datos.append(objeto)
    print("Obteniendo Citas")         
    return(jsonify(Datos))

#POSTEAR LAS CITAS
@app.route('/Citas', methods=['POST'])
def AgregarCita():
    
    global Citas
    nombre = request.json['Nombre']    
    idpaciente= request.json['Idpaciente']
    datehour = request.json['Datehour']
    motivo = request.json['Motivo']
    estado = request.json['Estado']
    doctor=""
    nuevo = Cita(nombre,idpaciente,datehour,motivo,estado,doctor)
    Citas.append(nuevo)
    return jsonify({'Mensaje':'Se ha Generado la cita exitosamente',})
#OBTENER UN DATO DE LAS CITAS
@app.route('/Citas/<string:nombre>', methods=['GET'])
def ObtenerCita(nombre): 
    global Citas
    for cita in Citas:
        if cita.getIdpaciente() == nombre:
            objeto = {
            'Nombre': cita.getNombre(),
            'Idpaciente': cita.getIdpaciente(),
            'Datehour': cita.getDatehour(),
            'Motivo': cita.getMotivo(),
            'Estado': cita.getEstado()             
            }
            print("Todo bien")
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe la cita con ese nombre"}

    return(jsonify(salida))
#ACTUALIZAR UNA CITA 
@app.route('/Citas/<string:nombre>', methods=['PUT'])
def ActualizarCita(nombre):    
    global Citas
    for i in range(len(Citas)):
        if nombre == Citas[i].getNombre():
            Citas[i].setNombre(request.json['Nombre'])
            #Citas[i].setIdpaciente(request.json['Idpaciente'])
            #Citas[i].setDatehour(request.json['Datehour'])
            #Citas[i].setMotivo(request.json['Motivo'])
            Citas[i].setEstado(request.json['Estado'])
            Citas[i].setDoctor(request.json['Doctor'])
            
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

#ELIMINAR UNA CITAS 
@app.route('/Citas/<string:nombre>', methods=['DELETE'])
def EliminarCita(nombre):
    global Medicinas    
    for i in range(len(Citas)):        
        if nombre == Citas[i].getIdpaciente():            
            del Citas[i]            
            return jsonify({'Mensaje':'Se elimino la cita exitosamente'})           
    return jsonify({'Mensaje':'No se encontro la cita para eliminar'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)