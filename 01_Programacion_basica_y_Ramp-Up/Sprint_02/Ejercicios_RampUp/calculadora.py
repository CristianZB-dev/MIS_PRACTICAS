def main_calculadora():
# MENSAJES INICIALES
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}")
    print("Que operación va a realizar?")
    print("\n1.Sumar")
    print("\n2.Restar")
    print("\n3.Multiplicar")
    print("\n4.Dividir")




#VALIDACION DE LA OPCION ELEGIDA

    while True:
        opcion = input("Elige una de las opciones anteriores (1/2/3/4): ")
        
        if opcion not in ["1", "2", "3", "4"]:
            ("Debe elegir una de las 4 opciones anteriores. Intente de nuevo.")
        else:
            break
  
# SOLICITAR NUMEROS PARA HACER LA OPERACIÓN
    try:

        num_1 = float(input("Introduzca el primer numero"))
        num_2 = float(input("Introduzca el segundo numero"))
    
    except ValueError:
        print("Por favor, introduzca numeros validos")
        return
# REALIZAR LA OPERACION SELECCIONADA

    if opcion == "1":
        resultado = num_1 + num_2
        operacion = "suma"

    elif opcion == "2":
        resultado = num_1 - num_2
        operacion = "resta"
    
    elif opcion == "3":
        resultado = num_1 * num_2
        operacion = "multiplicar"

    elif opcion == "4":
        if num_2 == 0:
            print("No se puede dividir entre 0")
            return
        resultado = num_1 / num_2
        operacion = "division"
    
# EL RESULTADO DE LA OPERACION CON SU PRESENTACION AL USUARIO
    
    print(f"\n{nombre}, el resultado de la {operacion} de {num_1} y {num_2} es {resultado}")


#EJECUTAR EL PROGRAMA

if __name__ == "__main__":
    main_calculadora()


