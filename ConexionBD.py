import couchdb

couchdb_server_url = "http://admin:admin@localhost:5984" #Aquí cambian por sus credenciales
server = couchdb.Server(couchdb_server_url)

db_name = "replica_proyectobda"  
db = server[db_name]

# Ejemplo de inserción de un documento
doc = {
    "nombre": "Jeanpool Obando Calvo",
    "puesto": "Scrum Master",
    "departamento": "Proyectos",
    "esInternacional": "Sí",
    "paisDestino": "Portugal",
    "motivoViaje": "Trabajo",
    "fechaIncio": "10/08/2023",
    "fechaFinalización": "12/11/2023",
    "detallesVuelos": {
        "aerolinea": "Avianca",
        "precioBoletos": 650000
    },
    "alojamiento": "Four seasons",
    "requiereTransporte": "No"
}  
db.save(doc)
