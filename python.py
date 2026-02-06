print("===== MENÚ =====")
print("1. Índice de masa corporal (IMC)")
print("2. Porcentaje de grasa corporal (%GC)")
print("3. Tasa metabólica basal según actividad física")
print("4. Cálculo de las calorías diarias para adelgazar")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    # === CÓDIGO IMC ===
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = peso / (altura * altura)

    print(f"\nSu IMC es: {imc}")

    if imc < 18.5:
        print("Clasificación: Delgadez")
    elif imc >= 18.5 and imc < 25:
        print("Clasificación: Peso normal")
    elif imc >= 25 and imc < 30:
        print("Clasificación: Sobrepeso")
    else:
        print("Clasificación: Obesidad")

elif opcion == 2:
    # === PORCENTAJE DE GRASA CORPORAL ===
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo (H/M): ").upper()

    imc = peso / (altura * altura)

    if sexo == "H":
        grasa = (1.20 * imc) + (0.23 * edad) - 16.2
    else:
        grasa = (1.20 * imc) + (0.23 * edad) - 5.4

    print(f"\nSu porcentaje de grasa corporal es: {grasa:.2f}%")

elif opcion == 3:
    # tasa metabolica basal segun actividad fisica 
    sexo = input("Ingrese su sexo (h/m): ").lower()
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en centímetros: "))
    edad = int(input("Ingrese su edad: "))

    if sexo == "h":
        tmb = 10 * peso + 6.25 * altura - 5 * edad + 5
    else:
        tmb = 10 * peso + 6.25 * altura - 5 * edad - 161

    print("\nNivel de actividad física:")
    print("1. Sedentario")
    print("2. Ligero")
    print("3. Moderado")
    print("4. Intenso")
    print("5. Muy intenso")

    actividad = int(input("Seleccione su nivel de actividad: "))

    if actividad == 1:
        factor = 1.2
    elif actividad == 2:
        factor = 1.375
    elif actividad == 3:
        factor = 1.55
    elif actividad == 4:
        factor = 1.725
    elif actividad == 5:
        factor = 1.9
    else:
        factor = 1.2

    calorias_diarias = tmb * factor

    print(f"\nSu tasa metabólica basal ajustada a la actividad física es: {calorias_diarias} calorías/día")

elif opcion == 4:
    
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad: "))
    sexo = int(input("Ingrese su sexo (1 = Hombre, 0 = Mujer): "))

    print("\nNivel de actividad física:")
    print("1. Sedentario")
    print("2. Ligero")
    print("3. Moderado")
    print("4. Intenso")

    actividad = int(input("Seleccione una opción (1-4): "))

    altura_cm = altura * 100

    if sexo == 1:
        tmb = 10 * peso + 6.25 * altura_cm - 5 * edad + 5
    else:
        tmb = 10 * peso + 6.25 * altura_cm - 5 * edad - 161

    
    if actividad == 1:
        factor = 1.2
    elif actividad == 2:
        factor = 1.375
    elif actividad == 3:
        factor = 1.55
    elif actividad == 4:
        factor = 1.725
    else:
        factor = 1.2

    calorias_mantenimiento = tmb * factor
    calorias_adelgazar = calorias_mantenimiento - 500

    print(f"\nCalorías de mantenimiento: {calorias_mantenimiento:.2f} kcal/día")
    print(f"Calorías recomendadas para adelgazar: {calorias_adelgazar:.2f} kcal/día")
else:
    print("Opción no válida.")


    

    