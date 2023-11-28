import random
from datetime import datetime, timedelta
import http.server
import socketserver
import json

# Arreglos predefinidos
nombres = ["SmartFit", "Bodytech", "Stark", "YogaSpecial","NatacionClub","RockClimb"]
imagenes = ["rachel-moore-zfPEja1D0YA-unsplash.jpg", "imagen2.jpg", "imagen3.jpg", "imagen4.jpg"]
direcciones = ["Calle 26A #88D-60", "Calle 93 #73-19", "Calle 21 #78D-24", "Calle 45 #88B-60"]
horarios = ["5:00 am - 12:00 pm", "6:00 am - 1:00 pm", "10:00 am - 15:00 pm", "6:00 am - 12:00 pm", "7:00 am - 12:00 pm", "8:00 am - 12:00 pm", "9:00 am - 12:00 pm", "10:00 am - 12:00 pm", "11:00 am - 12:00 pm", "12:00 pm - 12:00 pm", "13:00 pm - 12:00 pm", "14:00 pm - 12:00 pm", "15:00 pm - 12:00 pm", "16:00 pm - 12:00 pm", "17:00 pm - 12:00 pm", "18:00 pm - 12:00 pm", "19:00 pm - 12:00 pm", "20:00 pm - 12:00 pm", "21:00 pm - 12:00 pm", "22:00 pm - 12:00 pm", "23:00 pm - 12:00 pm"]

def generar_restaurante():
    id_restaurante = random.randint(1, 1000)
    nombre_restaurante = random.choice(nombres)
    direccion_restaurante = random.choice(direcciones)
    imagen_restaurante = random.choice(imagenes)
    horario_restaurante = random.choice(horarios)

    restaurante = {
        'id': id_restaurante,
        'nombre': nombre_restaurante,
        'direccion': direccion_restaurante,
        'imagen': imagen_restaurante,
        'horario': horario_restaurante
    }

    return restaurante

# Ejemplo de uso: generar un restaurante
restaurante_generado = generar_restaurante()

# Imprimir resultados
print(f"ID: {restaurante_generado['id']}, Nombre: {restaurante_generado['nombre']}, Dirección: {restaurante_generado['direccion']}, Imagen: {restaurante_generado['imagen']}, Horario: {restaurante_generado['horario']}")


ListaGimnasios=[]

for i in range (0,1000,1):
    ListaGimnasios.append(generar_restaurante())

# Guardar el arreglo en un archivo JSON
with open('restaurantes.json', 'w') as f:
    json.dump(ListaGimnasios, f, indent=2)

# Configurar el servidor
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Iniciar el servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor activo en el puerto {PORT}")
    httpd.serve_forever()