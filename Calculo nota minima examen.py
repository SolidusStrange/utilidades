# Lista global donde se almacenan las notas y sus ponderaciones
notas = []

# Nota mínima necesaria para aprobar el ramo
nota_minima = 3.945

# Lista para mostrar el orden de las notas (estética del mensaje)
ordinales = ["primera", "segunda", "tercera", "cuarta", "quinta"]

# Función principal para registrar las notas del ramo
def registro_notas():
    global notas
    notas = []
    total_ponderaciones = 0

    # Solicita cuántas notas habrá
    while True:
        try:
            limite = int(input("Ingrese la cantidad total de notas del ramo: "))
            if limite < 1:
                print("Debe haber al menos una nota.")
            else:
                break
        except ValueError:
            print("Ingrese un valor numérico válido.")

    # Pregunta si una nota será un promedio de controles
    confirmacion = input("¿Una de esas notas es un promedio de controles? (s/n): ").lower()
    usar_control = (confirmacion == "s")

    if usar_control:
        limite -= 1  # Reservamos un espacio para la nota de controles
        promedio_control, pondera_control = controles()
        notas.append({
            "nota": promedio_control,
            "ponderacion": pondera_control
        })
        total_ponderaciones += pondera_control

    print("\n--- INGRESO DE NOTAS ---")
    lista_notas_temporales = []

    for i in range(limite):
        while True:
            try:
                nota = float(input(f"Ingrese la {ordinales[i] if i < len(ordinales) else f'#{i+1}'} nota (1 al 7): "))
                if 1 <= nota <= 7:
                    lista_notas_temporales.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1 y 7.")
            except ValueError:
                print("Ingrese una nota válida.")

    print("\n--- INGRESO DE PONDERACIONES ---")

    for i in range(limite):
        while True:
            try:
                pondera = int(input(f"Ingrese la ponderación de la {ordinales[i] if i < len(ordinales) else f'#{i+1}'} nota (%): "))
                if pondera <= 0:
                    print("La ponderación debe ser mayor que 0.")
                elif total_ponderaciones + pondera > 100:
                    print(f"La suma total no puede superar el 100%. Ya llevas {total_ponderaciones}%.")
                else:
                    notas.append({
                        "nota": lista_notas_temporales[i],
                        "ponderacion": pondera
                    })
                    total_ponderaciones += pondera
                    break
            except ValueError:
                print("Ingrese una ponderación válida.")

    # Validación final: debe ser exactamente 100%
    if total_ponderaciones != 100:
        print(f"\nLa suma total de las ponderaciones es {total_ponderaciones}%, y debe ser exactamente 100%.")
        print("Notas ingresadas:")
        for i, n in enumerate(notas, 1):
            print(f"  Nota {i}: {n['nota']} con {n['ponderacion']}%")

        opcion = input("\n¿Desea volver a ingresar las notas? (s/n): ").lower()
        if opcion == "s":
            registro_notas()
        else:
            notas = []
            print("Se descartaron las notas ingresadas.")

    # Validación final: debe ser exactamente 100%
    if total_ponderaciones != 100:
        print(f"\nLa suma total de las ponderaciones es {total_ponderaciones}%, y debe ser exactamente 100%.")
        print("Notas ingresadas:")
        for i, n in enumerate(notas, 1):
            print(f"  Nota {i}: {n['nota']} con {n['ponderacion']}%")

        opcion = input("\n¿Desea volver a ingresar las notas? (s/n): ").lower()
        if opcion == "s":
            registro_notas()
        else:
            notas = []
            print("Se descartaron las notas ingresadas.")

# Función para registrar notas de controles y devolver su promedio y ponderación
def controles():
    print("\n--- Promedio de controles ---")

    # Pedir cantidad de controles
    while True:
        try:
            cantidad = int(input("¿Cuántos controles tuvo?: "))
            if cantidad < 1:
                print("Debe ingresar al menos 1 control.")
            else:
                break
        except ValueError:
            print("Ingrese un número válido.")

    suma = 0  # Para acumular la suma de las notas

    # Ingreso de cada control
    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Ingrese nota del control {i+1} (1 al 7): "))
                if 1 <= nota <= 7:
                    break
                else:
                    print("La nota debe estar entre 1 y 7.")
            except ValueError:
                print("Ingrese una nota válida.")
        suma += nota

    # Cálculo del promedio de controles
    promedio = suma / cantidad
    print(f"Promedio de controles: {promedio:.2f}")

    # Pedir la ponderación de esa nota promedio
    while True:
        try:
            pondera = int(input("Ingrese la ponderación total del promedio de controles: "))
            if 1 <= pondera <= 100:
                break
            else:
                print("La ponderación debe estar entre 1 y 100.")
        except ValueError:
            print("Ingrese una ponderación válida.")

    return promedio, pondera  # Retornamos la nota y la ponderación

# Función para calcular cuánto necesitas en el examen
def calculo_examen():
    if not notas:
        print("Debe ingresar primero las notas.")
        return

    total_ponderado = 0
    suma_ponderaciones = 0

    # Calculamos el total ponderado de notas
    for n in notas:
        total_ponderado += n["nota"] * n["ponderacion"]
        suma_ponderaciones += n["ponderacion"]

    # Validación para evitar división por cero (raro pero seguro)
    if suma_ponderaciones == 0:
        print("Error: La suma de ponderaciones es 0, no se puede calcular.")
        return

    # Se calcula el 60% de las notas ya ingresadas
    porcentaje_60 = (total_ponderado / suma_ponderaciones) * 0.6

    # Aplicamos la fórmula: (nota_mínima - porcentaje_60) / 0.4
    necesario_en_examen = (nota_minima - porcentaje_60) / 0.4

    # Mostramos resultados
    print(f"\nResultado del 60% de las notas: {porcentaje_60:.2f}")
    if necesario_en_examen > 7:
        print(f"Necesitas un {necesario_en_examen:.2f} en el examen... ¡Imposible!")
    elif necesario_en_examen < 1:
        print("¡Ya tienes nota suficiente para aprobar!")
    else:
        print(f"Necesitas sacar al menos un {necesario_en_examen:.2f} en el examen para aprobar.")

# Función para mostrar el menú principal
def menu():
    print("\n--- NOTA APROBACIÓN EXAMEN ---")
    print("1. Ingresar notas del ramo")
    print("2. Calcular nota necesaria en examen")
    print("3. Salir")

# Bucle principal del programa
while True:
    menu()
    opcion = input("Ingrese la opción que desea: ")

    if opcion == "1":
        registro_notas()
    elif opcion == "2":
        calculo_examen()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Ingrese una opción válida.")
