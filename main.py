#importacion de los modulos nesesarios
import modules.mainlogicfiles as ml
import modules.mainmenufiles as mm
#Maquetacion de los menus que se van a formar
print("Bienvenido al programa del sistema bancario")
ml.time.sleep(1)

while True: 
    
    op = mm.MenuInicio()
    match op:
        case "1":
            ml.NuevaCuenta()
        case "2":
            ml.Depositar()
        case "3":
            ml.Retirar()
        case "4":
            ml.SolicitarProducto()
        case "5":
            ml.Pagodesaldo()
        case "6":
            ml.Saldopendiente()
        case "7":
            ml.EliminarCuenta()
        case "8":
            print("Gracias por usar el sistema bancario")
            exit()
        case _:
            print("Opcion no valida")
