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
    print("Opción no implementada.")

elif opcion == 4:
    print("Opción no implementada.")

else:
    print("Opción no válida.")


    
    