#VERSION 1:
# Crear una tarea con diccionario
# Guardarla en una lista
# Que el día se genere automáticamente con datetime
# Poder ver todas las tareas en pantalla

import json
from datetime import date
import os

tareas = [] # Donde se guardarán las tareas

# Cargar el archivo .json reemplazando la lista tareas = []
def cargar_tareas():
    global tareas
    if os.path.exists("tareas.json"):  # Si el archivo existe
        with open("tareas.json", "r", encoding="utf-8") as f:
            tareas = json.load(f)
    else:
        tareas = []

# Guardar la lista de tareas en un archivo .json
def guardar_tareas():
    with open("tareas.json", "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

# Agregar una nueva tarea
def agregar_tarea(tarea, categoria):
    nueva_tarea = {
        "dia": str(date.today()), #fecha automática de hoy
        "tarea": tarea,
        "categoria": categoria,
        "estado": "pendiente"
    }

    tareas.append(nueva_tarea)
    print("Tarea agregada")

# Mostrar listado de todas las tareas
def mostrar_tareas():
    if not tareas: # Si la lista tarea no contiene nada
        print("No hay tareas registradas")
    else:
        print("\nLista de tareas: ")
        for i, t in enumerate(tareas, start= 1):
            print(f"{i}. [{t['estado']}] {t['tarea']} ({t['categoria']}) - {t['dia']}")

# Cambiar estado de la tarea de pendiente a completado
def cambiar_estado(indice_usuario):
    if 0 <= indice_usuario < len(tareas):
        tareas[indice_usuario]["estado"] = "completado"
        print(f"Tarea '{tareas[indice_usuario]['tarea']}' marcada como completada")
    else:
        print("Número inválido")

# Eliminar tareas de forma individual mediante el índice de la tarea
def eliminar_tareas(indice_usuario):
    if 0 <= indice_usuario < len(tareas):
        del tareas[indice_usuario]
        print("Tarea eliminada")
    else:
        print("Numero inválido")

# Eliminar todas las tareas del archivo
def eliminar_todas():
    confirmacion = input("¿Está realmente seguro de eliminar? (s/n)").lower()
    if confirmacion == "s" or confirmacion == "si":
        tareas.clear()
        print("Tareas eliminadas")
    
# Menu principal    
def menu():
    while True:
        print("\n---- MENU PRINCIPAL ----")
        print("1. Mostrar tareas")
        print("2. Agregar nueva tarea")
        print("3. Cambiar estado de la tarea")
        print("4. Eliminar tareas")
        print("5. Eliminar todas las tareas")
        print("6. Salir del menu")
        opcion = input("Ingrese la opción que desea:")

        if opcion == "1":
            mostrar_tareas()

        elif opcion == "2":
            while True:
                tarea_usuario = input("Ingresa la tarea a agregar (Ingrese 0 para dejar de añadir): ")
                if tarea_usuario == "0":
                    break
                categoria = input("Ingrese la categoria de la tarea: ")
                agregar_tarea(tarea_usuario, categoria)

        elif opcion == "3":
            if tareas:
                mostrar_tareas()
                try:
                    indice_usuario = int(input("Número de tarea a completar (0 para cancelar): ")) - 1
                    if indice_usuario == -1:
                        continue
                    cambiar_estado(indice_usuario)
                except ValueError:
                    print("Debe ingresar un número")
            else:
                print("No hay tareas registradas")
        
        elif opcion == "4":
            if tareas:
                mostrar_tareas()
                try:
                    indice_usuario = int(input("Número de tarea a eliminar (0 para cancelar): ")) - 1
                    if indice_usuario == -1:
                        continue
                    eliminar_tareas(indice_usuario)
                except ValueError:
                    print("Debe ingresar un número")
            else:
                print("No hay tareas registradas")

        elif opcion == "5":
            eliminar_todas()

        elif opcion == "6":
            print("Guardando y saliendo...")
            guardar_tareas()
            break

        else:
            print("Ingrese una opción válida")

        

#MENU PRINCIPAL
cargar_tareas()
menu()