
def convertir_a_binario(numero):
    if numero < 0:
        return "-" + convertir_a_binario(-numero)
    if numero < 2:
        return str(numero)
    return convertir_a_binario(numero // 2) + str(numero % 2)



def contar_digitos(numero):
    numero = abs(numero)
    if numero < 10:
        return 1
    return 1 + contar_digitos(numero // 10)



def calcular_raiz_cuadrada(numero, candidato):
    if candidato * candidato > numero:
        return candidato - 1
    return calcular_raiz_cuadrada(numero, candidato + 1)

def raiz_cuadrada_entera(numero):
    if numero < 0:
        return "Operacion incorrecta numeros negativos incorrectos"
    return calcular_raiz_cuadrada(numero, 0)



def convertir_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100,'D': 500, 'M': 1000
    }

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + convertir_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])

def suma_numeros_enteros(numero):
    if numero <= 0:
        return 0
    return numero + suma_numeros_enteros(numero - 1)


def menu():
    while True:
        print("\n--- MENÚ---")
        print("1. Convertir número a binario")
        print("2. Contar dígitos de un número")
        print("3. Raíz cuadrada entera")
        print("4. Convertir número romano a decimal")
        print("5. Sumar números enteros desde 0 hasta N")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            num = int(input("Ingrese un número entero: "))
            print("Binario:", convertir_a_binario(num))

        elif opcion == "2":
            num = int(input("Ingrese un número entero: "))
            print("Cantidad de dígitos:", contar_digitos(num))

        elif opcion == "3":
            num = int(input("Ingrese un número entero: "))
            print("Raíz cuadrada entera:", raiz_cuadrada_entera(num))

        elif opcion == "4":
            romano = input("Ingrese número romano en mayúsculas: ")
            print("Decimal:", convertir_a_decimal(romano))

        elif opcion == "5":
            num = int(input("Ingrese un número entero positivo: "))
            print("Suma total:", suma_numeros_enteros(num))

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida")
menu()