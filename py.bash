# Paso 1: Actualizar el sistema
sudo apt update && sudo apt upgrade

# Paso 2: Instalar las dependencias necesarias
sudo apt install build-essential zlib1g-dev:i386 libncurses5-dev:i386 libgdbm-dev:i386 libnss3-dev:i386 libssl-dev:i386 libreadline-dev:i386 libffi-dev:i386 wget

# Paso 3: Descargar la fuente de Python 3.9 de 32 bits
wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tar.xz

# Paso 4: Extraer el archivo tar
tar -xf Python-3.9.9.tar.xz

# Paso 5: Navegar al directorio de la fuente
cd Python-3.9.9

# Paso 6: Configurar y compilar Python 3.9
./configure --prefix=/usr/local --enable-optimizations --with-ensurepip=install
make -j$(nproc)

# Paso 7: Instalar Python 3.9
sudo make altinstall

# Paso 8: Verificar la instalación
python3.9 -V
