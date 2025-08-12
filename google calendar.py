import csv
import re
from datetime import datetime

#Texto original
texto = """
Taller N1: Jueves 28 Agosto
Taller N2: Lunes 22 Septiembre
Taller N3: Jueves 23 Octubre
Taller N4: Jueves 20 Noviembre
Prueba N1: Jueves 2 Octubre
Prueba N2: Jueves 27 Noviembre
"""

# Mapeo de meses a número

meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10,
    "noviembre": 11, "diciembre": 12
}


# Lista donde guardaremos los eventos
eventos = []

# Procesar cada línea
for linea in texto.strip().split("\n"):
    match = re.search(r"^(.*?):\s*(\w+)\s+(\d+)\s+(\w+)", linea)
    if match:
        titulo, dia_semana, dia, mes_nombre = match.groups()
        dia = int(dia)
        mes = meses[mes_nombre.lower()]
        anio = 2025
        
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
        start_date = f"{mes:02d}/{dia:02d}/{anio}"
        end_date = start_date
        
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
with open("eventos_calendar.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=eventos[0].keys())
    writer.writeheader()
    writer.writerows(eventos)
    
print("Archivo 'eventos_calendar.csv' generado correctamente.")