from flask import Flask, jsonify, request
from flask_cors import CORS
from Persona import Persona
import json

# ████████████████████████CREACION DE LISTAS PARA ALMACENAR INFORMACION████████████████████████
Personas = []

Personas.append(Persona('Carlos','Jimenez',22))
Personas.append(Persona('Roberto','Perez',22))
Personas.append(Persona('Ana','Solorzano',21))
Personas.append(Persona('Pancha','Lopez',23))

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def rutaInicial():
    return("<h1>Hola alumnos</h1>")

@app.route('/', methods=['POST'])
def rutaPost():
    objeto = {"Mensaje":"Se hizo el POST correctamente"}
    return(jsonify(objeto))

@app.route('/Personas', methods=['GET'])
def getPersonas():
    global Personas
    Datos = []
    for persona in Personas:
        objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Edad': persona.getEdad()
        }
        Datos.append(objeto)   
    return(jsonify(Datos))

@app.route('/Personas/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre): 
    global Personas
    for persona in Personas:
        if persona.getNombre() == nombre:
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Edad': persona.getEdad()
            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))


@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    global Personas
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    nuevo = Persona(nombre,apellido,edad)
    Personas.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})

@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    # Hacemos referencia a nuestro usuario global
    global Personas
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(Personas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == Personas[i].getNombre():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Personas[i].setNombre(request.json['nombre'])
            Personas[i].setApellido(request.json['apellido'])
            Personas[i].setEdad(request.json['edad'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

# METODO - ELIMINAR UN DATO☻████████████████████████
# En este caso, como trabajaremos con un solo dato, podemos mandar la informacion como parametro.
# NOTA: NO ES NECESARIO UTILIZAR EL METHOD DELETE, ES REFERENCIA UNICAMENTE
@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    # Referencia al arreglo global
    global Personas
    # Usamos un for para manejar por medio del indice
    for i in range(len(Personas)):
        # Validamos si es el nombre que queremos
        if nombre == Personas[i].getNombre():
            # Usamos del para eliminar el objeto
            del Personas[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for        
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
    
# NOTA IMPORTANTE: Cabe destacar que el dato que mandamos como parametro debe de ser el identificador del objeto
# Si trabajaramos con un Usuarios, mandamos username, si trabajamos con Recetas, mandamos el correlativo.

# Y POR ULTIMO, CORRER LA APLICACION
# Una vez definido todas nuestras rutas para ser consumidas por un cliente solo nos queda correr la aplicacion
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)