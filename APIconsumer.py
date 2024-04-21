import requests
import ctypes

def obtener_indice_gini(pais, año):
    url = f'https://api.worldbank.org/v2/en/country/{pais}/indicator/SI.POV.GINI?format=json&date={año}:{año}'
    respuesta = requests.get(url)
    indice_gini = None
    if respuesta.status_code == 200:
        datos = respuesta.json()[1]
        for dato in datos:
            if dato['countryiso3code'] == pais and dato['date'] == str(año):
                indice_gini = dato['value']
        print(f"No se encontraron datos para {pais} en el año {año}.")
    else:
        print(f"No se pudo obtener el índice GINI para {pais}. Código de estado: {respuesta.status_code}")
    return indice_gini
    # Creamos nuestra función factorial en Python
    # hace de Wrapper para llamar a la función de C
def factorial(num):
    return libprocess.factorial(num)  



if __name__ == "__main__":
    pais = input("Por favor ingresa el código del país (por ejemplo, ARG para Argentina): ")
    año = int(input("Por favor ingresa el año: "))
    indice_gini = obtener_indice_gini(pais, año)
    if indice_gini is not None:
        print(f"El índice GINI de {pais} en el año {año} es: {indice_gini}")

    # Cargamos la libreria 
    libprocess = ctypes.CDLL('./libprocess.so')

    # Definimos los tipos de los argumentos de la función factorial
    libprocess.factorial.argtypes = (ctypes.c_int,)

    # Definimos el tipo del retorno de la función factorial
    libprocess.factorial.restype = ctypes.c_ulonglong

    print(factorial(10))

    
