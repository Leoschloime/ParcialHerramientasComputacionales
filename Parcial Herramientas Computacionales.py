# Daniel Victoria Franco
# Leo Schloime


## IMPORTANTE: Todas las respuestas deben de ser dadas en minúscula

def tiendauniversitaria():
    cedula = input("Ingrese su documento de identidad: ")
    rol = input("¿Usted es estudiante o profesor? ")
    codigoaregistrar = str()
    print("Este es nuestro menú: ")
    print("Coca-cola $4.000 código: 10")
    cocacola = 4000
    print("Doritos $2.000 código: 20")
    doritos = 2000
    print("Hamburguesa $20.000 código: 30")
    hamburguesa = 20000
    print("Perro Caliente $17.000 código: 40")
    perro_caliente = 17000
    print("Pizza $15.000 código 50")
    pizza = 15000
    print("Manzana postobon $4.000 código 60")
    manzana_postobon = 4000

    n = int(input("¿Cuantos Productos quiere llevar? "))
    i = 0
    total = int(0)
    while i < n:
        codigo = int(input("Registre el código del producto deseado: "))
        if codigo == 10:
            total += int(cocacola)
            codigoaregistrar += str("10 ")
        elif codigo == 20:
            total += doritos
            codigoaregistrar += str("20 ")
        elif codigo == 30:
            total += hamburguesa
            codigoaregistrar += str("30 ")
        elif codigo == 40:
            total += perro_caliente
            codigoaregistrar += str("40 ")
        elif codigo == 50:
            total += pizza
            codigoaregistrar += str("50 ")
        elif codigo == 60:
            total += manzana_postobon
            codigoaregistrar += str("60 ")
        i += 1
    
    if rol == "estudiante":
        total = total / 2
    elif rol == "profesor":
        x = total / 5
        total -= x
    else:
        print("Digite si es profesor o estudiante")
        tiendauniversitaria()
    print("El ", rol, "con documento de identidad Nº", cedula, " debe pagar $", total, " por el/los productos de referencia ", codigoaregistrar )

    tiendauniversitaria()

tiendauniversitaria()
