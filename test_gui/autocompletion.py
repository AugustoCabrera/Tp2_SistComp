from PyQt5.QtWidgets import QComboBox, QWidget, QHBoxLayout, QCompleter, QCheckBox, QLabel
from PyQt5 import QtCore

# https://gist.github.com/Timmyway/da2bd0677525cd39a40e2efd17fa8445


# Por defecto QComboBox no tienen la funcion de autocompleado, por lo que se implementa usando
# un objeto QCompleter para tenerla.

# https://pypi.org/project/textual-autocomplete/
# Funcion para el autocomplete de palabras en el widget

def completion(word_list, widget):	
    completer = QCompleter(word_list)                           # antes (word_set)
    completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)     # Se configura el case sensitive
    completer.setFilterMode(QtCore.Qt.MatchContains)
    widget.setCompleter(completer)

#   -----------------------------------
# Clase Autocomplete para agregar la funcionalidad al combobox
#  ------------------------------------
class Autocomplete(QComboBox):

    itemSelected = QtCore.pyqtSignal(str)  # Señal personalizada para el evento de selección
    def __init__(self, items, parent=None):
        super(Autocomplete, self).__init__(parent)
        self.items = items
        self.init()

    def init(self):
        self.setEditable(True)
        self.addItems(sorted(set(self.items))) # Ordenamos y evitamos duplicados
        completion(self.items, self) # Establecer el autocompletado
        self.activated.connect(self.emitItemSelected)  # Conectar la señal activated

    def emitItemSelected(self):
        selected_text = self.currentText()  # Obtener el texto seleccionado
        self.itemSelected.emit(selected_text)  # Emitir la señal con el texto seleccionado
    def connectItemSelected(self, slot):
        self.itemSelected.connect(slot)

class Widget(QWidget):
    def __init__(self, items, parent=None, fixed=True):
        super(Widget, self).__init__()
        self.items = items
        self.autocomplete = Autocomplete(self.items, parent=self)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.autocomplete)
        self.autocomplete.itemSelected.connect(self.handleItemSelected)

    def handleItemSelected(self, selected_text):
        print("Selected:", selected_text)

    def currentText(self):
        return self.autocomplete.currentText()

    def currentIndex(self):		
        return self.autocomplete.currentIndex()