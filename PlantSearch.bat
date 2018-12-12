ECHO OFF

path = \Users\Guerra\Downloads\ProjMacrofitas-master\ProjMacrofitas-master\src\PlantSearch.py
set path=%path:\PlantSearch.py=\%
cd %path%

ECHO *** Instalando/ Verificando dependencias ***
\Python27\python.exe -m pip install -r requirements.txt


ECHO *** Subindo o servidor PlantSearch ***
\Python27\python.exe PlantSearch.py


