import os 
alumnos = []
profesores = []
cursos = []

print("Bienvenido!")
opcion =''
def menu():
    print("Menu Principal:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    
while opcion!= "salir":
    menu()
    opt = input("\nIngrese la opcion del menu: ")
    os.system("cls")
    if opt.isnumeric():
        if int(opt) == 1:
            print("asd")
        elif int(opt) ==2:
         print("asd")
        if int(opt) == 3:
            print("asd")
        elif int(opt) ==4:
         opcion="salir"
        else:
            print("ingrese una opcion valida")
    else:
        print("Ingrese una opcion numerica")
        
    input("Presione cualquier tecla para continuar....")  # Pausa
    
print ("Hasta luego!")
        
    