

print("DATOS DEL PACIENTE")
print("🎫🎫🎫🎫🎫🎫🎫🎫")
nombre = input("Nombre y apellido: \n")
fecha = input("Fecha de nacimiento: \n")
dni = int(input("DNI: \n"))
obra = input("Obra social: \n")
print("🎫🎫🎫🎫🎫🎫🎫🎫")


print("DATOS DE LA MEDICAMENTO")
print("💊💉💊💉💊💉💊💉💊")
nombreM = input("Nombre: \n")
dosis = input("Dosis recetada: \n")
instrucciones = input("Instrucciones de uso: \n")
print("💊💉💊💉💊💉💊💉💊")

Telefono = 3534590011
Mail = "Baez@salud.com"

continuar = True
while continuar:
    print("📚Ingrese sus datos para agendar mas turnos📚 \n") 
    nombre = input("Ingrese el nombre del paciente nuevamente: \n")
    fecha = input("Ingrese la fecha del turno: \n")
    hora = input("Ingrese la hora del turno: \n")
    
    respuesta = input("¿Desea ingresar otro turno? (s/n): ")
    if respuesta.lower() != "s":
        continuar = False
        
  

def Ticket1():
    print("------------------------")
    print("-   TICKET DE RETIRO   -")
    print("------------------------")
    print("🎫DATOS DEL PACIENTE🎫 ")
    print(f"📌Nombre: {nombre}")
    print(f"📌Fecha de nacimiento: {fecha}")
    print(f"📌DNI: {dni}")
    print(f"📌Obra social: {obra}")
    print("------------------------")
    print("💊DATOS DEL MEDICAMENTO💊")
    print(F"📌Nombre: {nombreM}")
    print(f"📌Dosis Diarias: {dosis}")
    print(f"📌nstrucciones: {instrucciones}")
    print("------------------------")
    print(f"Proximos Turnos: ")
    print(fecha)
    print(f"❗❗CONSULTAS AL❗❗")
    print("📲",Telefono)
    print("📩",Mail)  


         
Ticket1()







