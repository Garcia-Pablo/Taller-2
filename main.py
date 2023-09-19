import pickle

def menu():
    base_datos = validar_base_datos()
    while (True):
        # Despliegue de menú
        menu = input("\nMenú:\n1. Registrar estudiante\n2. Consultar estudiantes de una carrera\n3. Calcular promedio general\n4. Ver estudiantes destacados\n5. Salir\nSeleccione una opción: ")
        menu = validar_menu(menu,5)                                         # Validación de opciones de menú
        if menu == 1:                                                       # Registrar un estudiante
            # Se validan las variables de entrada para la base de datos
            nombre = validar_nombre()
            edad = validar_edad()
            carrera = menu_carreras()
            nota = validar_nota()
            # Agregamos al final de cada lista los datos ingresados
            base_datos['Nombre'].append(nombre)
            base_datos['Edad'].append(edad)
            base_datos['Carrera'].append(carrera)
            base_datos['Promedio'].append(nota)
            # Se carga el diccionario actualizado en la base de datos "pickle"
            cargar_base_datos(base_datos)

        elif menu == 2 and cantidad_estudiantes(base_datos):                # Consulta de estudiantes en una Carrera
            carrera = menu_carreras()
            estudiantes_carrera(base_datos,carrera)
            
        elif menu == 3 and cantidad_estudiantes(base_datos):                # Resultado del promedio general
            promedio_general(base_datos)
            
        elif menu == 4 and cantidad_estudiantes(base_datos):                # Estudiantes con promedio superior a 4.5
            estudiantes_destacados(base_datos)
        elif menu == 5:                                                     # Opción de salida
            print("Adiós, Vuelva pronto\n")
            break

# Funcion para acceder a la base de datos pre-existente
def validar_base_datos():
    try:
        # Se abre el archivo pickle en lectura (r) binaria (b)
        with open('base_datos.pkl', 'rb') as datos:
            datos_estudiantes = pickle.load(datos)                          # Se extrae el contenido del archivo
            estudiantes = list(datos_estudiantes.values())                  # Se crea una lista con las listas del diccionario
            print(f"\nSe ha cargado una base de datos anterior con {len(estudiantes[0])} estudiantes.\n")
            return datos_estudiantes
    
    except FileNotFoundError:                                               # Si no se encuentra un archivo:
        datos_estudiantes = {'Nombre': [], 'Edad': [], 'Carrera': [], 'Promedio': []}   # Se crea un diccionario con listas vacias
        print("\nNo se encontró una base de datos anterior. Comenzando con una base de datos vacia\n")
        return datos_estudiantes

# Funcion para guardar la base de datos 'actualizada'
def cargar_base_datos(base_datos):
    # Se abre el archivo pickle en escritura (w) binaria (b)
    with open('base_datos.pkl', 'wb') as datos:
        pickle.dump(base_datos, datos)                                      # Se guardan los datos en el archivo pickle

# Funcion para validar que hayan estudiantes registrados
def cantidad_estudiantes(base_datos):
    estudiantes = list(base_datos.values())                                 # Se crea una lista con las listas del diccionario
    # Verificamos que haya al menos 1 estudiante registrado retornando True o False según el caso
    if len(estudiantes[0]) > 0:
        return True
    else:
        print("\nNo hay estudiantes registrados. Por favor, ingrese al menos un estudiante primero")
        return False

# Funcion para consultar los estudiantes pertenecientes a una carrera especifica
def estudiantes_carrera(base_datos,carrera_consultada):
    carreras = base_datos['Carrera']                                        # Guardamos la lista de carreras en base de datos
    nombres = base_datos['Nombre']                                          # Guardamos la lista de nombres en base de datos
    
    # Ciclo for para guardar en una lista las posiciones del estudiante que estudia la carrera consultada
    posiciones = [i for i, carrera_lista in enumerate(carreras) if carrera_lista == carrera_consultada]
    # Si ubica almenos una vez la carrera, imprime los nombres de los estudiantes
    if len(posiciones) > 0: 
        for x in posiciones: print(nombres[x])
    # Si no, implica que no hay estudiantes que estén registrados en la carrera consultada
    else:
        print("\nNo hay estudiantes registrados en esta carrera")

# Función para calcular el promedio general de los estudiantes
def promedio_general(base_datos):
    notas = base_datos['Promedio']                                          # Guardamos la lista de promedios en base de datos
    suma = 0.0                                                              # Inicializamos la suma en cero

    for i in notas: suma += i                                               # Ciclo for para sumar todos los promedios
    promedio = suma/len(notas)
    print(f"Promedio general: {promedio:.{2}f}")

# Función para imprimir los estudiantes destacados
def estudiantes_destacados(base_datos):
    claves = list(base_datos.keys())                                        # Guardamos como lista las claves de la base de datos
    promedio = base_datos['Promedio']                                       # Guardamos la lista de promedios en base de datos

    # Ciclo for para guardar en una lista las posiciones del estudiante que tiene promedio de 4.5 o superior
    posiciones = [i for i, notas in enumerate(promedio) if notas >= 4.5]
    # Ciclo for para imprimir los datos de los estudiantes destacados
    for x in posiciones:
        print('\n'+'*'*50)
        print(f"{claves[0]} = {base_datos['Nombre'][x]}")
        print(f"{claves[1]} = {base_datos['Edad'][x]}")
        print(f"{claves[2]} = {base_datos['Carrera'][x]}")
        print(f"{claves[3]} = {base_datos['Promedio'][x]}")
    print('\n'+'*'*50)

# Función para validar un número entero
def num_entero(num):
    try:
        # Se intenta convertir el numero ingresado (string) a entero
        int(num)
        return int(num)
    # Si no es posible, implica que el valor ingresado no puede ser un numero entero
    except ValueError:
        print("El número ingresado no es un número entero")

# Función para validar un número flotante
def num_flotante(num):
    try:
        # Se intenta convertir el numero ingresado (string) a flotante
        float(num)
        return float(num)
    # Si no es posible, implica que el valor ingresado no puede ser un numero flotante
    except ValueError:
        print("El número ingresado no es un número flotante")

# Función para validar las opciones del menú
def validar_menu(num,n_opciones):
    try:
        # Se usa valida que el opcion seleccionada de menú sea un número entero
        menu = num_entero(num)
        # Si la opcion ingresada no esta en el rango del menú se "instancia un ValueError"
        if menu not in range(1,(n_opciones+1)):
            raise ValueError("\nEl valor ingresado no es una opción del menú")
    except ValueError as mes:
        print(mes)
    # Si el ValueError no se evoca se retorna el valor seleccionado de menú
    else:
        return menu
    
# Funcion para desplegar y elegir el menú de carreras disponibles
def menu_carreras():
    while (True):
        # Lista de las Carreras disponibles para menú
        carreras = ["Ingeniería de Productividad y Calidad", "Ingeniería Agropecuaria", "Ingeniería Civil",
                    "Ingeniería en Seguridad y Salud en el Trabajo", "Ingeniería en Automatización y Control",
                    "Ingeniería Informática"]
        # Despliegue de menú
        menu = input(f"\nSeleccione una carrera de la siguiente lista: \n1. {carreras[0]}\n2. {carreras[1]}\n3. {carreras[2]}\n4. {carreras[3]}\n5. {carreras[4]}\n6. {carreras[5]}\n>> ")
        menu = validar_menu(menu,6)                                                   # Validación de opciones de menú
        # Si la opcion de menú es válida entra al if
        if menu != None:
            return carreras[menu-1]
            break

# Funcion para validar que el nombre solo tenga letras del alfabeto
def validar_nombre():
    while(True):
        nombre = input("Ingrese el nombre del estudiante: ")
        
        try:
            # Se verifica que los caracteres del 'nombre ingresado solo sean letras'
            if nombre.isalpha():
                nombre = nombre.lower()                                 # Se convierte todo el nombre a minuscula
                nombre = nombre[0].upper() + nombre[1:]                 # Se guarda el nombre solo con la primera letra mayuscula

                return nombre
                break
            # Si el dato ingresado contiene algo diferente a letras se instancia ValueError
            else:
                raise ValueError("El nombre ingresado tiene caracteres inválidos\n")
        except ValueError as mes:
            print(mes)

# Funcion para validar edad del estudiante
def validar_edad():
    while(True):
        edad = input("Ingrese la edad del estudiante: ")
        edad = num_entero(edad)                                         # Se verifica que la edad sea un número entero
        # print(edad)

        # Si la edad es un numero entero entra al if
        if edad != None:
            # Se restringe la edad entre los 14 y los 122 años
            if edad not in range(14,123):
                print("La edad permitida en el curso es entre 14 y 122 años\n")
            else:
                return edad
                break

# Funcion para validar el promedio ingresada
def validar_nota():
    while(True):
        nota= input("Ingrese el promedio del estudiante entre (0.0) y (5.0): ")
        nota = num_flotante(nota)                                       # Se verifica que la edad sea un número flotante
        # Se usa una funcion lambda para crear una lista con números flotantes entre 0.0 y 5.0 solo con 1 decimal
        rango_nota = list(map(lambda x: x/10, range(0,51)))
        # Si el promedio es un numero flotante entra al if
        if nota != None:
            # Si el promedio no está en el rango permitido imprime mensaje
            if nota not in rango_nota:
                print("El promedio ingresado debe estar entre 0.0 y 5.0, con un solo decimal\n")
            else:
                return nota
                break


if __name__ == '__main__':
    menu()