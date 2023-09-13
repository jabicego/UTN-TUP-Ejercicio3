
print ("----- Ingrese los datos para la receta -----")


nombre_paciente = input("Ingrese nombre del paciente: ")
apellido_paciente = input("Ingrese apellido del paciente: ")
fecha_nac = input("Ingrese fecha nacimiento del paciente: ")
medicamento = input("Ingrese nombre del Medicamento: ")
dosis = input("Dosis: ")
instrucciones_uso = input("Indicaciones: ")
prox_turno = input("Ingrese fecha proximo turno: ")

def impresion_receta ():
    print("----Clinica Especialidades---")
    print("--Direccion: Corrientes 666--")
    print("--------Receta medica--------")
    print("-----------------------------")
    print("Paciente:", nombre_paciente + " " + apellido_paciente)
    print("Fecha de nacimiento: ", fecha_nac)
    print("Medicamente: ", medicamento + "   Dosis: ", dosis)
    print("Indicaciones: ", instrucciones_uso)
    print("Proximo Turno: ", prox_turno)
    return

impresion_receta()
