def registrarPersonas():

  
    individuo={}

    #nombre
    nombre=input("Como te llamas?")
    individuo["Nombre"]=nombre
    print()

    #edad
    edad=int(input("ingrese su edad"))
    while edad<18:
        edad=int(input("ingrese su edad"))
    individuo["edad"]=edad
    print()
    

    #selecionar genero
    generos = ["Masculino", "Femenino", "Otro"]
    print("Selecciona tu genero:")
    print("1. Masculino")
    print("2. Femenino")
    print("3. Otro ")
    
    opcion = int(input("Elige una opcion:  "))
    print()

    if opcion == 1:
        individuo["Genero"] = generos[0]
    elif opcion == 2:
        individuo["Genero"] = generos[1]
    elif opcion == 3:
        individuo["Genero"] = generos[2]
    else:
        print("Opcion no valida")


    #selecionar genero de interes
    generoInteres = ["masculino", "femenino", "otro"]
    print("Seleccina genero de interes:")
    print("1. Masculino")
    print("2. Femenino")
    print("3. Otro")

    opcion1 = int(input("Elige una opcion: "))
    print()


    if opcion1 == 1:
       individuo["Genero"] = generoInteres[0]
    elif opcion1 == 2:
       individuo ["genero"] = generoInteres[1]
    elif opcion1 == 3:
       individuo ["genero"] = generoInteres[2]
    else:
        print("opcion no valida")
       
   
    print(individuo)
    return individuo

  
def mostrarPersonas(personas):
    print (personas)

def main():
              
    
    
            #resgistro de personas
    
    
    
    opciones="1.registrar personas \n. mostrar las persona\n. salir"
    print(opciones)
    opcion2=int(input("digite una opcion"))
    print()
    while opcion2!=9:
        
        cuantasPersonas=int(input("cuantas personas se van a registrar"))
        print()
        
        if opcion2==1:
            registrarPersonas()
    
            personas=()
            for i in range (0,cuantasPersonas):
                print ("i",i)
                print(personas)
                personas[i]=registrarPersonas()

                #mostrar personas

                mostrarPersonas(personas)
        elif opcion2==9:
            print("gracias")
            break
        print(opciones)
        opcion2= input("digite una opcion")
        print()

main()

