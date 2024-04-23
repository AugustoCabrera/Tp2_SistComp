import requests
import ctypes

# Definir la función _float_int antes de llamarla
def _float_int(num):
    # Cargamos la libreria 
    libprocess = ctypes.CDLL('./libfloat_int.so') #gcc -m32 -shared -o libfloat_int.so float_int.o

    # Definimos los tipos de los argumentos de la función _float_int
    libprocess._float_int.argtypes = (ctypes.c_float,)
    
    # Definimos el tipo del retorno de la función _float_int
    libprocess._float_int.restype = ctypes.c_int

    # Llamamos a la función _float_int
    return libprocess._float_int(num)

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

if __name__ == "__main__":
    pais = input("Por favor ingresa el código del país (por ejemplo, ARG para Argentina): ")
    año = int(input("Por favor ingresa el año: "))
    indice_gini = obtener_indice_gini(pais, año)
    if indice_gini is not None:
        print(f"El índice GINI de {pais} en el año {año} es: {indice_gini}")

    
    num_int = _float_int(indice_gini)
    print(f"The integer value of {indice_gini} is {num_int}")
