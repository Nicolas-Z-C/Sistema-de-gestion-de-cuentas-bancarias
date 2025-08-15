
def MenuInicio():
    opcion = str(input(""" Elija una de las siguientes opciones porfavor
                        1. Crear nueva cuenta 
                        2. Depositar dinero 
                        3. Retirar dinero
                        4. Solicitar credito 
                        5. Pago cuota credito 
                        6. Visualizar mis productos
                        7. Eliminar cuenta
                        8. Salir
                    """))
    return opcion

def MenuProductos():
    print("Elija uno de los siguientes productos porfavor")
    opcion= input("""
    1.CDT
    2.Credito libre inversion
    3.Credito viviendia
    4.Credit compra auto movil
    """)
    return opcion
