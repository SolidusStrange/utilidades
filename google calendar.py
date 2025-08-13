import csv #Escribir el archivo CSV que Google Calendar leerá
import re #Expresiones regulares para extraer datos (día, mes, etc) del texto
from datetime import datetime #Trabajar con fechas si necesitamos validarlas o formatearlas

#Bloque que contiene los eventos en formato original. Lo recorremos linea por linea:
# Título (por ejemplo, “Taller N°1”).
# Día de la semana (“Jueves” o “Lunes”).
# Número del día (28, 22, etc.).
# Mes (“Agosto”, “Septiembre”, etc.).

texto = """
Taller N1: Jueves 28 Agosto
Taller N2: Lunes 22 Septiembre
Taller N3: Jueves 23 Octubre
Taller N4: Jueves 20 Noviembre
Prueba N1: Jueves 2 Octubre
Prueba N2: Jueves 27 Noviembre
"""

#Conversión de meses a números:

meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10,
    "noviembre": 11, "diciembre": 12
}
#GOOGLE CALENDAR necesita fechas en formato numérico (ej: 08/28/2025)
#Este diccionario traduce el nombre del mes en español a número

# Lista donde guardaremos los eventos
eventos = [] #Aquí vamos guardando cada evento como un diccionario con las columnas del CSV.

# Procesar cada línea
# ^(.*?) → Todo antes de los dos puntos (título del evento).
# (\w+) → El día de la semana (ej. “Jueves”).
# (\d+) → El número del día (ej. “28”).
# (\w+) → El nombre del mes (ej. “Agosto”).

for linea in texto.strip().split("\n"): #Quitamos espacios y saltos de línea al inicio/fin, y luego separamos el texto en líneas individuales
    match = re.search(r"^(.*?):\s*(\w+)\s+(\d+)\s+(\w+)", linea) #re.search(...) expresión regular para extraer
    if match:
        titulo, dia_semana, dia, mes_nombre = match.groups() #match.groups() → Devuelve esos valores como una tupla para guardarlos en variables.
        dia = int(dia)
        mes = meses[mes_nombre.lower()] #Lo pasamos a minúsculas para que coincida con las claves del diccionario.
        anio = 2025 #Año fijo para todos los eventos.
        
        # Asignar horas según día de la semana
        if dia_semana.lower() == "lunes":
            start_time = "08:30"
            end_time = "09:50"
        elif dia_semana.lower() == "jueves":
            start_time = "08:30"
            end_time = "10:30"
        else:
            start_time = "08:30"
            end_time = "09:30"  # default por si aparece otro día
            
         # Formato fecha para Google Calendar (MM/DD/YYYY)
        start_date = f"{mes:02d}/{dia:02d}/{anio}" #Asegura que el mes tenga dos dígitos (ej. 08), día con dia:02d, usamos MM/DD/YYYY
        end_date = start_date
        
        # Creamos el diccionario del evento 
        #Este diccionario representa una fila del CSV.
        # Las claves deben coincidir exactamente con los nombres que Google Calendar espera.
        eventos.append({
            "Subject": titulo,
            "Start Date": start_date,
            "Start Time": start_time,
            "End Date": end_date,
            "End Time": end_time,
            "All Day Event": "FALSE",
            "Description": "",
            "Location": ""
            })
        
    
# Guardar CSV
with open("eventos_calendar.csv", "w", newline="", encoding="utf-8") as f: #Abre un archivo llamado eventos_calendar.csv para escritura.
    writer = csv.DictWriter(f, fieldnames=eventos[0].keys()) #escribe usando las claves de cada diccionario como cabeceras de columna.
    writer.writeheader() #Escribe la primera fila con los nombres de columna.
    writer.writerows(eventos) #Escribe todas las filas de la lista.
    
print("Archivo 'eventos_calendar.csv' generado correctamente.") 