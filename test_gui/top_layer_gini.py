import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from autocompletion import Widget
import requests
import subprocess

countries = {} 


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

def get_all_countries():
    base_url = "http://api.worldbank.org/v2/country"
    params = {
        "format": "json",
        "per_page": 50,  # Número de países por página
        "page": 1  # Página inicial
    }
    countries_dict = {}

    while True:
        response = requests.get(base_url, params=params)
        data = response.json()
        countries = data[1]

        if not countries:
            break

        for country in countries:
            name = country["name"]
            iso3 = country["id"]
            countries_dict[name] = iso3

        params["page"] += 1

    return countries_dict


def handleItemSelected(selected_text,label):
    selected_country_id = countries[selected_text]
    gini_index, obtained_error = get_gini_index(selected_country_id, 2020)
    if gini_index is not None:
        label.setText(f"El índice GINI de {selected_text} es: {gini_index}")
    else:
        label.setText(obtained_error)   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()

    countries = get_all_countries()
    country_names = list(countries.keys())
    cb = Widget(country_names, parent=w)
    # cb.autocomplete.connectItemSelected(handleItemSelected) # se conecta la seleccion del item
    label = QLabel(parent=w)  # Crear una etiqueta para mostrar el índice GINI
    cb.autocomplete.connectItemSelected(lambda text: handleItemSelected(text, label))  # Conectar la señal al método

    layout = QHBoxLayout()
    layout.addWidget(cb)
    layout.addWidget(label)  # Agregar la etiqueta al diseño
    w.setLayout(layout)
    w.show()
    sys.exit(app.exec_())