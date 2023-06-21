'''TOP 120 CANCIONES MÁS STREMEADAS EN SPOTIFY AÑO 2022'''
'''Librerias a importar para el funcionamiento del programa'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''FUNCIÓN DEL MENU CON VERIFICADOR DE NUMEROS EN CASO DE QUE SE INGRESEN OPCIONES QUE
NO ESTÁN DENTRO DEL MENÚ U OPCIONES QUE NO SEAN NUMEROS ENTEROS'''
def mostrar_menu():
    while True:
        option= input("\n ***** Menú *****" +
                            "\n 1. Ver los datos de la lista" +
                            "\n 2. Buscar datos" +
                            "\n 3. Datos por rango" + 
                            "\n 4. Exportar los datos de la lista"+
                            "\n 5. Graficar datos"+
                            "\n 6. Salir" +
                            "\n Ingrese su opción: ")
        if option == '1': #OPCION DEL MENU PARA DESPLEGAR VISUALIZACIÓN DE LOS DATOS 
            mostrar_datos()
        elif option == '2': #OPCION DEL MENÚ PARA FILTAR DATOS (BUSCADOR)
            filtro()
        elif option == '3':
            rango()
        elif option == '4': #OPCION DEL MENU PARA EXPORTAR LOS DATOS EN FORMATO A ELECCIÓN
            exportar()
        elif option == '5': #OPCION PARA GRAFICAR LOS DATOS 
            graficar()
        elif option == '6': #OPCION DEL MENÚ PARA SALIR Y TERMINAR EL PROGRAMA
            print("Saliendo..." + "\n Adiós :D")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

def mostrar_datos(): #FUNCION PARA LA OPCION 1 DEL MENU
    while True:
        opcion1= input("\n *** Opciones ***" +
                        "\n 1. Ver lista de datos de manera normal" +
                        "\n 2. Ver lista de datos de manera invertida"+
                        "\n 3. Ver solo columna 'Nombre de artistas' " +
                        "\n 4. Ver solo columna 'Nombre de canción' "+ 
                        "\n 5. Volver al menú" +
                        "\n Ingrese su opción: ")
        if opcion1 == '1': #OPERADOR QUE MUESTRA LA LISTA DE DATOS DE MANERA NORMAL (DEL 1 AL 120)
            print("Leyendo lista...")
            var = open("C:/Users/thebr/Desktop/Spotify.txt", "r")
            while True:
                linea=var.readline()
                if not linea : break
                print(linea)
            var.close()

        elif opcion1 == '2': #OPERADOR QUE MUESTRA LA LISTA DE DATOS DE MANERA INVERTIDA (DEL 120 AL 1)
            print("Leyendo lista...")
            def texto_invertido(nombre_archivo):
                with open(nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    for linea in reversed(lineas):
                        print(linea.rstrip())
            nombre_archivo = 'C:/Users/thebr/Desktop/Spotify.txt'  
            texto_invertido(nombre_archivo) 

        elif opcion1=='3':
            print("Leyendo columna...")
            def columna_cantantes(nombre_archivo):
                with open(nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    # Verificar si hay líneas en el archivo
                    if lineas:
                        # Obtener la primera línea y separar las columnas por un delimitador
                        primera_linea = lineas[0].strip()
                        columnas = primera_linea.split(',')

                        # Verificar si "cantantes" está en la lista de columnas
                        if 'Artist Name' in columnas:
                            # Obtener el índice de la columna de "cantantes"
                            indice_cantantes = columnas.index('Artist Name')
                            # Mostrar únicamente los valores de la columna de "cantantes"
                            for linea in lineas[1:]:
                                datos = linea.strip().split(',')
                                if len(datos) > indice_cantantes:
                                    print(datos[indice_cantantes])
                        else:
                            print('La columna de "cantantes" no está presente en el archivo.')
                    else:
                        print('El archivo está vacío.')
            nombre_archivo = 'C:/Users/thebr/Desktop/Spotify.txt'  
            columna_cantantes(nombre_archivo)

        elif opcion1=='4':
            print("Leyendo columna...")
            def columna_canciones(nombre_archivo):
                with open(nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    # Verificar si hay líneas en el archivo
                    if lineas:
                        # Obtener la primera línea y separar las columnas por un delimitador
                        primera_linea = lineas[0].strip()
                        columnas = primera_linea.split(',')

                        # Verificar si "canciones" está en la lista de columnas
                        if 'Song Name' in columnas:
                            # Obtener el índice de la columna de "canciones"
                            indice_canciones = columnas.index('Song Name')

                            # Mostrar únicamente los valores de la columna de "canciones"
                            for linea in lineas[1:]:
                                datos = linea.strip().split(',')
                                if len(datos) > indice_canciones:
                                    print(datos[indice_canciones])
                        else:
                            print('La columna de "cantantes" no está presente en el archivo.')
                    else:
                        print('El archivo está vacío.')
            nombre_archivo = 'C:/Users/thebr/Desktop/Spotify.txt'  
            columna_canciones(nombre_archivo)

        elif opcion1 == '5': #OPERADOR PARA VOLVER AL MENU
            print("Volviendo...")
            return(mostrar_menu)
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

def filtro():#FUNCION PARA LA OPCION 2 DEL MENÚ
    while True:
        opcion2 = input("\n *** Opciones ***" +
                        "\n 1. Buscar canción" +
                        "\n 2. Buscar cantante" + 
                        "\n 3. Volver al menú" +
                        "\n Ingrese su opción: ")
        if opcion2 =='1':
            def buscar_cancion(nombre_archivo, letra):
                canciones = set()
                primera_linea=True #operacion para que al momento de buscar se omita el título de la columna
                with open(nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    for linea in lineas:
                        if primera_linea:
                            primera_linea = False
                            continue
                        datos = linea.split(',')  
                        cancion = datos[2].strip() 

                        if cancion.startswith(letra):
                            canciones.add(cancion)
                for cancion in canciones:
                    print(cancion)
            nombre_archivo = 'C:/Users/thebr/Desktop/Spotify.txt'
            letra_elegida = input("\n(considere que las mayúsculas y minúsculas pueden influir" +
                                  "\nen su búsqueda)"+
                                  "\nIngrese la letra por la que quiere buscar: ")
            buscar_cancion(nombre_archivo, letra_elegida)

        elif opcion2 == '2':
            def buscar_cantante(nombre_archivo, letra):
                cantantes = set() #funcion para que al momento de buscar no aparezca el mismo nombre repetido
                primera_linea=True #operacion para que al momento de buscar se omita el título de la columna
                with open(nombre_archivo, 'r') as archivo:          
                    lineas = archivo.readlines()
                    for linea in lineas:
                        if primera_linea:
                            primera_linea = False
                            continue
                        datos = linea.split(',')  
                        cantante = datos[1].strip() 
                        if cantante.startswith(letra):
                            cantantes.add(cantante)
                for cantante in cantantes:
                    print(cantante)
            nombre_archivo = 'C:/Users/thebr/Desktop/Spotify.txt'
            letra_elegida = input("Ingrese la letra por la que quiere buscar: ") 
            buscar_cantante(nombre_archivo, letra_elegida.upper())

        elif opcion2 == '3': #OPERADOR PARA VOLVER AL MENU
            print("Volviendo...")
            return(mostrar_menu)
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

def rango(): #FUNCION PARA OPCION 3 EN EL MENU
    datos=pd.read_csv('C:/Users/thebr/Desktop/Spotify.txt', index_col=0, parse_dates=True)
    while True:
        opcion3= input("\n *** Opciones ***" +
                        "\n 1. Ver datos medios" +
                        "\n 2. Ver dato máximo" + 
                        "\n 3. Ver dato mínimo" +
                        "\n 4. Ver primeros 5 datos" +
                        "\n 5. Volver al menú" +
                        "\n Ingrese su opción: ")
        if opcion3 == '1':
            print(datos.describe())
        elif opcion3 =='2':
            print(datos.max())
        elif opcion3=='3':
            print(datos.min())
        elif opcion3=='4':
            print(datos.head())
        elif opcion3=='5':
            print("Volviendo...")
            return(mostrar_menu)
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

def exportar(): #FUNCION PARA OPCION 4 DEL MENU
    while True:
        opcion4 = input("\n *** Opciones ***" +
                        "\n 1. Exportar archivo txt" +
                        "\n 2. Exportar archivo csv" + 
                        "\n 3. Exportar archivo excel"
                        "\n 4. Volver al menú" +
                        "\n Ingrese su opción: ")
        datos = pd.read_csv('C:/Users/thebr/Desktop/Spotify.txt') 
        if opcion4 == '1': #OPERADOR PARA EXPORTAR ARCHIVO TXT
            print("Exportando archivo txt...")
            datos.to_csv('archivo_exportado.txt', sep='\t', index=False)
            print('Archivo TXT exportado correctamente :D' + 
                "\nPodrás encontrar el archivo como archivo_exportado.txt")
        elif opcion4 == '2': #OPERADOR PARA EXPORTAR ARCHIVO CSV
            print("Exportando archivo csv...")
            datos.to_csv('archivo_exportado.csv', index=False)
            print('Archivo CSV exportado correctamente :D' + 
                "\nPodrás encontrar el archivo como archivo_exportado.csv")
        elif opcion4 == '3': #OPERADOR PARA EXPORTAR ARCHIVO XLSX
            print("Exportando archivo excel...")
            datos.to_excel('archivo_exportado.xlsx', index=False)
            print("Archivo Excel exportado correctamente :D" + 
                "\nPodrás encontrar el archivo como archivo_exportado.xlsx")
        elif opcion4 == '4': #OPERADOR PARA VOLVER AL MENU 
            print("Volviendo...")
            return(mostrar_menu)
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

def graficar(): #FUNCION PARA OPCION 5 DEL MENÚ
    while True:
        opcion5 = input("\n *** Opciones ***" +
                        "\n 1. Mostrar grafico de los cantantes que más se repiten" +
                        "\n 2. Mostrar gráfico de los cantantes que han estado más veces en el numero 1" + 
                        "\n 3. Volver al menú" +
                        "\n Ingrese su opción: ")
        if opcion5 == '1':
            print("Generando gráfico...")   
            def grafico_cantidad_cantantes(nombre_archivo, columna):
                # Leer el archivo de texto y crear un DataFrame
                datos = pd.read_csv(nombre_archivo)

                # Realizar el conteo de repeticiones en la columna especificada
                conteo = datos[columna].value_counts()

                fix , ax = plt.subplots(figsize = (10,6))
                # Configurar etiquetas y título
                plt.xlabel(columna)
                plt.ylabel('Cantidad de repeticiones')
                plt.title('Cantidad de repeticiones por ' + columna)

                conteo.plot(kind='bar', color= 'green', ax=ax)
                # Mostrar el gráfico
                plt.show()
            nombre_archivo = 'C:/Users/thebr/Desktop/Spotify.txt'
            columna = 'Artist Name' 
            grafico_cantidad_cantantes(nombre_archivo, columna)
            
        elif opcion5 == '2':
            print("Generando gráfico...")
            def grafico_cantantes_posicion1(nombre_archivo):
                # Leer el archivo de texto y crear un DataFrame
                datos = pd.read_csv(nombre_archivo)

                # Filtrar los datos de los cantantes en posición número 1
                cantantes_posicion1 = datos[datos['Peak Position'] == 1]['Artist Name']

                # Contar la cantidad de veces que cada cantante estuvo en posición número 1
                conteo_cantantes = cantantes_posicion1.value_counts()

                # Crear el gráfico de barras
                fix , ax = plt.subplots(figsize = (10,6))

                conteo_cantantes.plot(kind='bar', color= 'violet', ax=ax)
                
                # Configurar etiquetas y título
                plt.xlabel('Cantante')
                plt.ylabel('Cantidad de veces en posición número 1')
                plt.title('Cantantes con mayor tiempo en la posición número 1')

                # Mostrar el gráfico
                plt.show()
            nombre_archivo = 'C:/Users/thebr/Desktop/Spotify.txt'
            grafico_cantantes_posicion1(nombre_archivo)
        elif opcion5=='3':
            print("Volviendo...")
            return(mostrar_menu)
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

# Función principal para ejecutar el programa
def main():
    mostrar_menu()

# Para ejecutar el programa
if __name__ == '__main__':
    main()
