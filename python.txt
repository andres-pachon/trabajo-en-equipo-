# Calculadora de Salud en Python

while True:
    print("\n===== CALCULADORA DE SALUD =====")
    print("1. Índice de Masa Corporal (IMC)")
    print("2. Porcentaje de Grasa Corporal (%GC)")
    print("3. Tasa Metabólica Basal según actividad física")
    print("4. Calorías diarias para adelgazar")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))

        imc = peso / (altura * altura)
        print(f"IMC: {imc}")

    elif opcion == 2:
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        edad = int(input("Edad: "))
        sexo = int(input("Sexo (1 = Hombre, 2 = Mujer): "))

        imc = peso / (altura * altura)

        if sexo == 1:
            gc = (1.20 * imc) + (0.23 * edad) - 16.2
        else:
            gc = (1.20 * imc) + (0.23 * edad) - 5.4

        print(f"Porcentaje de grasa corporal: {gc}%")

    elif opcion == 3:
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (cm): "))
        edad = int(input("Edad: "))
        sexo = int(input("Sexo (1 = Hombre, 2 = Mujer): "))

        if sexo == 1:
            tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
        else:
            tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)

        print("Nivel de actividad:")
        print("1. Sedentario")
        print("2. Ligero")
        print("3. Moderado")
        print("4. Intenso")

        actividad = int(input("Seleccione: "))

        if actividad == 1:
            factor = 1.2
        elif actividad == 2:
            factor = 1.375
        elif actividad == 3:
            factor = 1.55
        else:
            factor = 1.725

        print(f"TMB según actividad: {tmb * factor}")

    elif opcion == 4:
        tmb = float(input("Ingrese su TMB: "))
        calorias = tmb - 500
        print(f"Calorías diarias para adelgazar: {calorias}")

    elif opcion == 5:
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
