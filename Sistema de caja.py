while True:
    print("1. Ingresar producto")
    print("2. Ver productos")
    print("3. Cobrar")
    print("4.Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "4":
        break
    if opcion == "1":
    
        nombre_del_producto = input("Ingrese el nombre del producto:")
        precio_del_producto = float(input("Ingrese el precio del producto:"))
        codigo_del_producto = int(input("Ingrese el codigo del producto:"))
        cantidad_de_producto = int(input("Ingrese la cantidad del producto:"))
        producto = {
            "nombre": nombre_del_producto,
            "precio": precio_del_producto,
            "codigo": codigo_del_producto,
            "cantidad": cantidad_de_producto
        }
    productos= []
    productos.append(producto)
    if opcion == "2": 
        print("Productos ingresados:")
        for producto in productos:
            print(f'Nombre:{producto["nombre"]} Precio:{producto["precio"]} Codigo:{producto["codigo"]} Cantidad:{producto["cantidad"]}')
    if opcion == "3": 
        total = 0 
        for producto in productos:
            total += producto["precio"]*producto["cantidad"]
            impuesto = total * 0.16
            total_con_impuesto = total + impuesto
            cambio= float(input(f'El total es: {total_con_impuesto}, ingrese el monto con el que va a pagar:'))
            print(f'Total: {total}')
            print(f'Impuesto: {impuesto}')
            print(f'Total con impuesto: {total_con_impuesto}')
            print(f'El cambio es: {cambio - total_con_impuesto}')
