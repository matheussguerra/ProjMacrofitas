ECHO OFF
ECHO *** Instalando/ Verificando dependencias ***
cd \
(dir /s /b *requirements.txt) > temp.txt
SET /p VAR=<temp.txt
Python27\python.exe -m pip install -r %VAR%

ECHO *** Executando PlantSearch ***

(dir /s /b *PlantSearch.py) > temp.txt
SET /p VAR=<temp.txt
Python27\python.exe %VAR%

Pause
