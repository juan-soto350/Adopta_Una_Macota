# simular el proceso de búsqueda y selecion de una mascota ideal segun las preferencias de una persona
def crear_mascotas():
   
    mascotas = [
        {
            "nombre": "Luna",
            "especie": "perro",
            "edad": 3,
            "energia": "media",
            "compatible_ninos": "sí"
        },
        {
            "nombre": "Max",
            "especie": "perro",
            "edad": 2,
            "energia": "alta",
            "compatible_ninos": "no"
        },
        {
            "nombre": "Coco",
            "especie": "perro",
            "edad": 5,
            "energia": "media",
            "compatible_ninos": "sí"
        },
        {
            "nombre": "Mimi",
            "especie": "gato",
            "edad": 1,
            "energia": "baja",
            "compatible_ninos": "sí"
        },
        {
            "nombre": "Pelusa",
            "especie": "gato",
            "edad": 4,
            "energia": "media",
            "compatible_ninos": "no"
        },
        {
            "nombre": "Rocco",
            "especie": "perro",
            "edad": 7,
            "energia": "baja",
            "compatible_ninos": "sí"
        },
        {
            "nombre": "Nieve",
            "especie": "conejo",
            "edad": 2,
            "energia": "media",
            "compatible_ninos": "sí"
        },
        {
            "nombre": "Sombra",
            "especie": "gato",
            "edad": 6,
            "energia": "baja",
            "compatible_ninos": "no"
        },
        {
            "nombre": "Chispa",
            "especie": "perro",
            "edad": 1,
            "energia": "alta",
            "compatible_ninos": "sí"
        },
        {
            "nombre": "Canela",
            "especie": "conejo",
            "edad": 3,
            "energia": "baja",
            "compatible_ninos": "sí"
        }
    ]
    return mascotas

def obtener_preferencias():
    """
    Solicita al usuario sus preferencias para adoptar una mascota.
    Retorna un diccionario con las preferencias del usuario.
    """
    print(" Bienvenido a AdoptaUnaMascota ")
    print("Vamos a encontrar tu mascota ideal!\n")
    

    especie = input("¿Cuál especie te interesa? (perro/gato/conejo): ").lower().strip()
    
    while True:
        try:
            edad_min = int(input("Edad mínima (años): "))
            edad_max = int(input("Edad máxima (años): "))
            if edad_min <= edad_max and edad_min >= 0:
                break
            else:
                print("Error: La edad mínima debe ser menor o igual a la máxima y no negativa.")
        except ValueError:
            print("Error: Por favor ingresa un número válido.")
    

    energia = input("¿Nivel de energía preferido? (alta/media/baja): ").lower().strip()
    

    tiene_ninos = input("¿Tienes niños en casa? (sí/no): ").lower().strip()
    
    preferencias = {
        "especie": especie,
        "edad_min": edad_min,
        "edad_max": edad_max,
        "energia": energia,
        "tiene_ninos": tiene_ninos
    }
    
    return preferencias

def filtrar_mascotas(mascotas, preferencias):
    """
    Filtra las mascotas según las preferencias del usuario.
    Retorna una lista de mascotas compatibles.
    """
    mascotas_compatibles = []
    
    for mascota in mascotas:

        compatible = True
        

        if mascota["especie"] != preferencias["especie"]:
            compatible = False
        

        if not (preferencias["edad_min"] <= mascota["edad"] <= preferencias["edad_max"]):
            compatible = False
        
   
        if mascota["energia"] != preferencias["energia"]:
            compatible = False
        
       
        if preferencias["tiene_ninos"] == "sí" and mascota["compatible_ninos"] == "no":
            compatible = False
        
        
        if compatible:
            mascotas_compatibles.append(mascota)
    
    return mascotas_compatibles

def mostrar_mascota(mascota):
    """
    Muestra los detalles de una mascota de forma amigable.
    """
    print(f"\n {mascota['nombre']}")
    print(f"   Especie: {mascota['especie'].title()}")
    print(f"   Edad: {mascota['edad']} años")
    print(f"   Energía: {mascota['energia'].title()}")
    print(f"   Amigable con niños: {mascota['compatible_ninos'].title()}")

def proceso_adopcion(mascotas_compatibles):
    """
    Aqui se muestran las mascotas compatibles una por una y permite al usuario elegir.
    Ademas retorna True si se adoptó una mascota, False si no.
    """
    if not mascotas_compatibles:
        print("\n Lo siento, no encontramos mascotas que coincidan exactamente con tus preferencias.")
        print("Te sugerimos ampliar tus criterios de búsqueda.")
        return False
    
    print(f"\n¡Genial! Encontramos {len(mascotas_compatibles)} mascota(s) perfecta(s) para ti:\n")
    
    for i, mascota in enumerate(mascotas_compatibles, 1):
        print(f"--- Mascota {i} ---")
        mostrar_mascota(mascota)
        
        while True:
            decision = input(f"\n¿Quieres adoptar a {mascota['nombre']}? (sí/no): ").lower().strip()
            if decision in ["sí", "si", "yes", "y"]:
                print(f"\n Felicidades! Has adoptado a {mascota['nombre']} ")
                print(f"{mascota['nombre']} está muy feliz de ir a su nuevo hogar contigo!")
                print("Gracias por darle una segunda oportunidad a una mascota necesitada. ")
                return True
            elif decision in ["no", "n"]:
                if i < len(mascotas_compatibles):
                    print("Entendido, veamos la siguiente opción...")
                break
            else:
                print("Por favor responde 'sí' o 'no'.")
    
    print("\n Has visto todas las opciones disponibles.")
    print("¡Esperamos que encuentres tu mascota ideal pronto!")
    return False

def mostrar_mascotas(mascotas):
    """
    Muestra la lista completa de mascotas disponibles.
    """
    print("Lista completa de mascotas disponibles")
    print("=" * 40)

    for i, mascota in enumerate(mascotas, 1):
        print(f"{i:2}. {mascota['nombre'].title()} ({mascota['especie'].title()})")
        print(f"    Edad: {mascota['edad']} años")
        print(f"    Energía: {mascota['energia'].title()}")
        print(f"    Compatible con niños: {mascota['compatible_ninos'].title()}")
        print()
        
def main():
    """
    Función principal que ejecuta el programa completo.
    """
    #imprime las mascotas
    mostrar_mascotas(mascotas)
    
    # Crear lista de mascotas disponibles
    mascotas = crear_mascotas()
    
    # Obtener preferencias del usuario
    preferencias = obtener_preferencias()
    
    # Filtrar mascotas compatibles
    mascotas_compatibles = filtrar_mascotas(mascotas, preferencias)
    
    # Ejecutar proceso de adopción
    adopcion_exitosa = proceso_adopcion(mascotas_compatibles)
    
    if not adopcion_exitosa:
        print("\n¡Gracias por visitar AdoptaUnaMascota!")
        print("Vuelve pronto para encontrar tu compañero perfecto. 🐾")


            
menu = '''
______________________
|  AdoptaUnaMascota  |
|____________________|
|1.Ver mascotas      |
|2.Adoptar mascota   |      
|3.Salir de programa | 
|____________________|

'''

        

while True:
    print(menu)
    opcion = int(input("ingrese una de las opciones del menu:"))
    if opcion == 1:
        # Crear la lista de mascotas
        mascotas = crear_mascotas()
        # Mostrar la lista de mascotas
        mostrar_mascotas(mascotas)
        
    elif opcion ==2:
        # Ejecutar el programa
        if __name__ == "__main__":
            main()
    elif opcion == 3:
        print("Saliendo del progrema")
        break
    else:
        print("Opcion no valida, ingrese una opcion del menu")
     

        
