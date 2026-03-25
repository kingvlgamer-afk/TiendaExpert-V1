print("=== BIENVENID@ A TAMALES LAS ExpertV1 ===")

total = 0

nombre = input("¿Cuál es tu nombre?: ")
print(f"Hola, {nombre}")

while True:
    print("\nOPCIONES DE COMPRA")
    print("1 - Tamal Pollo ($35)")
    print("2 - Atole Litro ($50)")
    print("3 - Atole Medio Litro ($25)")
    print("4 - Tamal Piña ($18)")
    print("5 - Ver Total")
    print("6 - Salir")

    try:
        opcion = int(input("¿Cuál es tu opción?: "))
    except:
        print("Por favor ingresa un número válido")
        continue

    if opcion == 1:
        cantidad = int(input("¿Cuántos tamales de pollo quieres?: "))
        total += cantidad * 35
        print("Añadido al pedido")

    elif opcion == 2:
        cantidad = int(input("¿Cuántos litros de atole quieres?: "))
        total += cantidad * 50
        print("Atole añadido al pedido")

    elif opcion == 3:
        cantidad = int(input("¿Cuántos medios litros de atole quieres?: "))
        total += cantidad * 25
        print("Añadido al pedido")

    elif opcion == 4:
        cantidad = int(input("¿Cuántos tamales de piña quieres?: "))
        total += cantidad * 18
        print("Añadido al pedido")

    elif opcion == 5:
        print(f"Tu total es: ${total}")

    elif opcion == 6:
        print(f"Gracias por tu compra, total: ${total}")
        break

    else:
        print("Opción inválida")