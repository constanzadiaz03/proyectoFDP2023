'''TOP 120 CANCIONES MÁS STREMEADAS EN SPOTIFY AÑO 2022'''

import pandas as pd
import matplotlib.pyplot as plt

# Función para cargar los datos desde Datos.gob (u otra fuente de datos externa)
def cargar_datos():
    datos = pd.read_csv("C:/Users/thebr/Desktop/Spotify.txt")
    return datos

'''LISTAS VACÍAS PARA ALMACENAR LO INGRESADO POR EL USUARIO'''
lista1 =[]
lista2 =[]
lista3 =[]
lista4 =[]
lista5 =[]


def salida():
  return ("Usted ha salido de la seccion de registros.!!")


'''FUNCIÓN DEL MENU CON VERIFICADOR DE NUMEROS EN CASO DE QUE SE INGRESEN OPCIONES QUE
NO ESTÁN DENTRO DEL MENÚ U OPCIONES QUE NO SEAN NUMEROS ENTEROS'''
def mostrar_menu():
    while True:
        option= int(input("\n ***** Menú *****" +
                            "\n 1. Ver los datos de la lista" +
                            "\n 2. Buscar datos por cantante"+
                            "\n 3. Buscar datos por canción" + 
                            "\n 4. Exportar los datos de la lista"+
                            "\n 5. Graficar datos"
                            "\n 6. Salir" +
                            "\n Ingrese su opción: "))
        if option == 1:
            mostrar_datos()
        elif option == 2:
            filtro_cantante()
        elif option == 3:
            mostrar_visualizaciones()
        elif option == 4:
            exportar_datos()
        elif option == 5:
            graficar()
        elif option == 6:#OPCION DEL MENÚ PARA SALIR Y TERMINAR EL PROGRAMA
            print("Saliendo..." + "\n Adiós :D")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

def mostrar_datos(): #FUNCION PARA LA OPCION 1 DEL MENU
    #datos = cargar_datos()
    while True:
        opcion1= input("\n *** Opciones ***" +
                        "\n 1. Ver lista de datos de manera normal" +
                        "\n 2. Ver lista de datos de manera invertida" + 
                        "\n 3. Volver al menú" +
                        "\n Ingrese su opción: ")
        if opcion1 == '1':
            print("Leyendo lista...")
            var = open("C:/Users/thebr/Desktop/Spotify.txt", "r")
            while True:
                linea=var.readline()
                if not linea : break
                print(linea)
            var.close()
            vuelta1=input("\n***¿Deseas realizar otra acción?***" +
                          "\n 1. Si" + "\n 2. No" + "\n Ingrese su opción: ")
            if vuelta1 == '1':
                return(opcion1)
            elif vuelta1 == '2':
                print("Saliendo..." + "\n Adiós :D")
                break
        elif opcion1 == '2':
             print(lista2)
        elif opcion1 == '3':
            print("Volviendo...")
            return(mostrar_menu)
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

def filtro_cantante():#FUNCION PARA LA OPCION 2 DEL MENÚ
    datos = mostrar_datos()
    # Ejemplo: Mostrar datos por provincia
    cantante = input("Ingrese el cantante a filtrar: ")
    print("Buscando...")
    var = open("C:/Users/thebr/Desktop/Spotify.txt", "r")
    lista2 =[]
    for line in var.readlines():
        while True:
            if line in cantante.lower() == 'Post Malone':
                lista2 = line
           # elif line in cantante.lower() == 
    datos_cantante = datos[datos['cantante'] == cantante]
    print(datos_cantante)

# Función para mostrar visualizaciones
def mostrar_visualizaciones():
    datos = cargar_datos()
    
    # Ejemplo: Mostrar un gráfico de barras de la distribución de edades
    datos['edad'].plot(kind='bar')
    plt.xlabel('Índice')
    plt.ylabel('Edad')
    plt.title('Distribución de Edades')
    plt.show()

# Función para exportar un subconjunto de datos en un formato seleccionado por el usuario
def exportar_datos(df, exportFormat=1):
    datos = cargar_datos()
    '''data frame de la lista '''
    #df_lista = pd.export(datos, columnas = ['Artista', 'Canción', 'dias', 'top10', 
                       # 'peak', 'tiempopeak', 'peakstream', 'totalstream'])
    nombre_archivo = int(input("\n *** Seleccione el tipo de archivo a exportar ***" +
                               "\n 1. archivo txt" + 
                               "\n 2. archivo panilla excel"
                               "\n 3. archivo csv" + 
                               "\n 4. Volver al menú"))
    if nombre_archivo not in (1, 2, 3, 4):
        print("Ingrese una opción válida")
    elif nombre_archivo == 1:
        with open('../out/export.txt', 'w') as f:
            txt = df.to_string(header=True)
            f.write(txt)
    elif nombre_archivo == 2:
        df.to_excel('../out/export.xlsx')
    elif nombre_archivo == 3:
        df.to_csv('../out/export.csv')
    elif nombre_archivo == 4:
        print("Volviendo al menú...")
        return(mostrar_menu)
    print("Datos exportados exitosamente con el nombre de export juntoa la extensión solicitada")

def graficar():
    datos = cargar_datos()
# Función principal para ejecutar el programa
def main():
    mostrar_menu()

# Ejecutar el programa
if __name__ == '__main__':
    main()
