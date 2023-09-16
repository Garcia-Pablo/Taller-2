import pickle

def menu():
    base_datos = validar_base_datos()
    while (True):
        # Despliegue de menú
        menu = input("\nMenú:\n1. Registrar estudiante\n2. Consultar estudiantes de una carrera\n3. Calcular promedio general\n4. Ver estudiantes destacados\n5. Salir\nSeleccione una opción: ")
        menu = validar_menu(menu,5)                                                     # Validación de opciones de menú
        if menu == 1:                                                                   # Registrar un estudiante
            # ############Se validan las variables de entrada
            nombre = validar_nombre()
            edad = validar_edad()
            carrera = menu_carreras()
            nota = validar_nota()
            base_datos['Nombre'].append(nombre)
            base_datos['Edad'].append(edad)
            base_datos['Carrera'].append(carrera)
            base_datos['Promedio'].append(nota)
            cargar_base_datos(base_datos)

        elif menu == 2 and cantidad_estudiantes(base_datos):
            carrera = menu_carreras()
            estudiantes_carrera(base_datos,carrera)
            
        elif menu == 3 and cantidad_estudiantes(base_datos):
            promedio_general(base_datos)
            
        elif menu ==4 and cantidad_estudiantes(base_datos):
            estudiantes_destacados(base_datos)
        elif menu ==5:
            print("Adiós, Vuelva pronto\n")
            break

def validar_base_datos():
    try:
        with open('base_datos.pkl', 'rb') as datos:
            datos_estudiantes = pickle.load(datos)
            estudiantes = list(datos_estudiantes.values())
            print(f"\nSe ha cargado una base de datos anterior con {len(estudiantes[0])} estudiantes.\n")
            return datos_estudiantes

    except FileNotFoundError:
        datos_estudiantes = {'Nombre': [], 'Edad': [], 'Carrera': [], 'Promedio': []}
        print("\nNo se encontró una base de datos anterior. Comenzando con una base de datos vacia\n")
        return datos_estudiantes

def cargar_base_datos(base_datos):
    with open('base_datos.pkl', 'wb') as datos:
        pickle.dump(base_datos, datos)

def cantidad_estudiantes(base_datos):
    estudiantes = list(base_datos.values())
    if len(estudiantes[0]) > 0:
        return True
    else:
        print("\nNo hay estudiantes registrados. Por favor, ingrese al menos un estudiante primero")
        return False

def estudiantes_carrera(base_datos,carrera_consultada):
    estudiantes = list(base_datos.values())
    carreras = estudiantes[2]
    nombres = estudiantes[0]
    
    posiciones = [i for i, carrera_lista in enumerate(carreras) if carrera_lista == carrera_consultada]
    if len(posiciones) > 0: 
        for x in posiciones: print(nombres[x])
    else:
        print("\nNo hay estudiantes registrados en esta carrera")

def promedio_general(base_datos):
    estudiantes = list(base_datos.values())
    notas = estudiantes[3]
    suma = 0.0

    for i in notas: suma += i
    promedio = suma/len(notas)
    print(f"Promedio general: {promedio:.{2}f}")

def estudiantes_destacados(base_datos):
    contenido = list(base_datos.items())
    promedio = contenido[3][1]

    posiciones = [i for i, notas in enumerate(promedio) if notas >= 4.5]
    for x in posiciones:
        print('\n'+'*'*50)
        print(f"{contenido[0][0]} = {contenido[0][1][x]}")
        print(f"{contenido[1][0]} = {contenido[1][1][x]}")
        print(f"{contenido[2][0]} = {contenido[2][1][x]}")
        print(f"{contenido[3][0]} = {contenido[3][1][x]}")
    print('\n'+'*'*50)


def num_entero(num):
    try:
        int(num)
        return int(num)
    except ValueError:
        print("El número ingresado no es un número entero")

def num_flotante(num):
    try:
        float(num)
        return float(num)
    except ValueError:
        print("El número ingresado no es un número flotante")

def validar_menu(num,n_opciones):
    try:
        menu = num_entero(num)
        if menu not in range(1,(n_opciones+1)):
            raise ValueError("\nEl valor ingresado no es una opción del menú")
    except ValueError as mes:
        print(mes)
    else:
        return menu
    
def menu_carreras():
    while (True):
        # Despliegue de menú
        menu = input("\nSeleccione una carrera de la siguiente lista: \n1. Ingeniería de Productividad y Calidad\n2. Ingeniería Agropecuaria\n3. Ingeniería Civil\n4. Ingeniería en Seguridad y Salud en el Trabajo\n5. Ingeniería en Automatización y Control\n6. Ingeniería Informática\n>> ")
        menu = validar_menu(menu,6)                                                   # Validación de opciones de menú
        if menu == 1:
            return("Ingeniería de Productividad y Calidad")
            break
        elif menu == 2:
            return("Ingeniería Agropecuaria") 
            break
        elif menu == 3:
            return("Ingeniería Civil")
            break
        elif menu ==4:
            return("Ingeniería en Seguridad y Salud en el Trabajo")
            break
        elif menu ==5:
            return("Ingeniería en Automatización y Control")
            break
        elif menu ==6:
            return("Ingeniería Informática")
            break

def validar_nombre():
    while(True):
        nombre = input("Ingrese el nombre del estudiante: ")
        
        try:
            if nombre.isalpha():
                nombre = nombre.lower()
                nombre = nombre[0].upper() + nombre[1:]

                return nombre
                break
            else:
                raise ValueError("El nombre ingresado tiene caracteres inválidos\n")
        except ValueError as mes:
            print(mes)

def validar_edad():
    while(True):
        edad = input("Ingrese la edad del estudiante: ")
        edad = num_entero(edad)
        # print(edad)
        if edad != None:
            if edad not in range(14,123):
                print("La edad permitida en el curso es entre 14 y 122 años\n")
            else:
                return edad
                break

def validar_nota():
    while(True):
        nota= input("Ingrese el promedio del estudiante entre (0.0) y (5.0): ")
        nota = num_flotante(nota)
        rango_nota = list(map(lambda x: x/10, range(0,51)))
        if nota != None:
            if nota not in rango_nota:
                print("El promedio ingresado debe estar entre 0.0 y 5.0, con un solo decimal\n")
            else:
                return nota
                break


if __name__ == '__main__':
    menu()