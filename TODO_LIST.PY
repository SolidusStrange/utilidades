#VERSION 1:
# Crear una tarea con diccionario
# Guardarla en una lista
# Que el día se genere automáticamente con datetime
# Poder ver todas las tareas en pantalla

from datetime import date

tareas = [] # Donde se guardarán las tareas

def agregar_tarea(tarea, categoria):
    nueva_tarea = {
        "dia": str(date.today()), #fecha automática de hoy
        "tarea": tarea,
        "categoria": categoria,
        "estado": "pendiente"
    }

    tareas.append(nueva_tarea)
    print("Tarea agregada")

def mostrar_tareas():
    if not tareas: # Si la lista tarea no contiene nada
        print("No hay tareas registradas")
    else:
        print("\nLista de tareas: ")
        for i, t in enumerate(tareas, start= 1):
            print(f"{i}. [{t['estado']}] {t['tarea']} ({t['categoria']}) - {t['dia']}")

def menu():
    while True:
        print("\n---- MENU PRINCIPAL ----")
        print("1. Mostrar tareas")
        print("2. Agregar nueva tarea")
        print("3. Cambiar estado de la tarea")
        print("4. Salir del menu")
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
            while True:
                if tareas:
                    indice_usuario = int(input("Número de tarea a completar (Ingrese 0 para dejar de añadir): ")) - 1
                    if indice_usuario == -1:
                        break
                    
                    if 0 <= indice_usuario < len(tareas):  
                        tareas[indice_usuario]["estado"] = "completado"
                        print(f"Tarea '{tareas[indice_usuario]['tarea']}' marcada como completada")
                    else:
                        print("Numero inválido")
                        continue
                else:
                    print("No hay tareas registradas")
        
        elif opcion == "4":
            print("Saliendo de la lista de tareas...")
            break

        else:
            print("Ingrese una opción válida")

menu()