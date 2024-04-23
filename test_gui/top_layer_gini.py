import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from autocompletion import Widget
import matplotlib.pyplot as plt
import requests 
import ctypes

countries = {} 

def _float_int(num):
    # Cargamos la libreria 
    libprocess = ctypes.CDLL('./libfloat_int.so') #gcc -m32 -shared -o libfloat_int.so float_int.o

    # Definimos los tipos de los argumentos de la función _float_int
    libprocess._float_int.argtypes = (ctypes.c_float,)
    
    # Definimos el tipo del retorno de la función _float_int
    libprocess._float_int.restype = ctypes.c_int

    # Llamamos a la funyción _float_int
    return libprocess._float_int(num)


def get_gini_index(country, year):
    url = f'https://api.worldbank.org/v2/en/country/{country}/indicator/SI.POV.GINI?format=json&date={year}:{year}'
    respuesta = requests.get(url)
    indice_gini = None
    error = "Ningun error"
    if respuesta.status_code == 200:
        datos = respuesta.json()[1]
        for dato in datos:
            if dato['countryiso3code'] == country and dato['date'] == str(year):
                indice_gini = dato['value']
                error = f"No se encontraron datos para {country} en el año {year}."
    else:
                error = f"No se pudo obtener el índice GINI para {country}. Código de estado: {respuesta.status_code}"
    return indice_gini, error


def get_gini_indices(country, start_year, end_year):
    gini_indices = []
    errors = []

    url = f'https://api.worldbank.org/v2/en/country/{country}/indicator/SI.POV.GINI?format=json&date={start_year}:{end_year}'
    response = requests.get(url)
        
    if response.status_code == 200:
        data = response.json()[1]
        if data is not None:
            for year in range(start_year, end_year + 1):
                gini_found = False
                for datum in data:
                    if datum['countryiso3code'] == country and datum['date'] == str(year):
                        value = datum['value']
                        if value is None or value == "null":
                            if(gini_indices.__len__() == 0):
                                gini_indices.append(0)
                            else:
                                gini_indices.append(gini_indices[-1])
                        else:
                            value1 = _float_int(float(value))
                            gini_indices.append(float(value1))
                        gini_found = True
                        break
                if not gini_found:
                    if gini_indices:
                        gini_indices.append(gini_indices[-1])
                    else:
                        gini_indices.append(None)
                    errors.append(f"No se encontraron datos para {country} en el año {year}.")
        else:
            if gini_indices.__len__() == 0:
                gini_indices.append(0)
            for year in range(start_year, end_year + 1):
                if gini_indices:
                    gini_indices.append(gini_indices[-1])
                else:
                    gini_indices.append(None)
                errors.append(f"No se encontraron datos para {country} en el año {year}.")
    else:
        for year in range(start_year, end_year + 1):
            if gini_indices:
                gini_indices.append(gini_indices[-1])
            else:
                gini_indices.append(None)
            errors.append(f"No se pudo obtener el índice GINI para {country} en el año {year}. Código de estado: {response.status_code}")

    return gini_indices, errors


def plot_gini_indices(country, start_year, end_year):
    gini_indices, errors = get_gini_indices(country, start_year, end_year)
    years = range(start_year, end_year + 1)

    plt.plot(years, gini_indices, marker='o')
    plt.title(f'Índice GINI de {country} ({start_year}-{end_year})')
    plt.xlabel('Año')
    plt.ylabel('Índice GINI')
    plt.grid(True)
    plt.xticks(years, rotation=45)
    plt.tight_layout()

    for error in errors:
        print(error)

    plt.show()




def get_all_countries_from_file(file_path):
    with open(file_path, 'r') as file:
        countries_data = json.load(file)

    countries_dict = {}
    for country_name, iso3_code in countries_data.items():
        countries_dict[country_name] = iso3_code

    return countries_dict


def handleItemSelected(selected_text,label):
    selected_country_id = countries[selected_text]
    
    plot_gini_indices(selected_country_id, 2000, 2023)

    #gini_index, obtained_error = get_gini_index(selected_country_id, 2020)
    
    
    
    #if gini_index is not None:
    #    label.setText(f"El índice GINI de {selected_text} es: {gini_index}")
    #else:
    #    label.setText(obtained_error)   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()

    countries = get_all_countries_from_file("countries.json")
    country_names = list(countries.keys())
    cb = Widget(country_names, parent=w)
    # cb.autocomplete.connectItemSelected(handleItemSelected) # se conecta la seleccion del item
    label = QLabel(parent=w)  # Crear una etiqueta para mostrar el índice GINI
    image_label = QLabel(parent=w)  # Crear una etiqueta para mostrar la imagen
    
    
    pixmap = QPixmap("gini_map.png")
    pixmap = pixmap.scaled(600, 800, Qt.KeepAspectRatio)  # Cambia 200, 200 a los tamaños deseados
    image_label.setPixmap(pixmap)
     
    image_label.setAlignment(Qt.AlignCenter) 
    
    cb.autocomplete.connectItemSelected(lambda text: handleItemSelected(text, label))  # Conectar la señal al método

    layout = QHBoxLayout()
    layout.addWidget(cb)
    layout.addWidget(label)  # Agregar la etiqueta al diseño
    layout.addWidget(image_label)
    w.setLayout(layout)
    w.show()
    sys.exit(app.exec_())

