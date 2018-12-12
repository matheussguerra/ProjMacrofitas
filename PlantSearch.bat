ECHO OFF

cd\
 
(dir /s /b *PlantSearch.py)>temp.txt
SET /p VAR=<temp.txt
SET path=%VAR:\PlantSearch.py=\%

cd %path%

ECHO *** Instalando/ Verificando dependencias ***
\Python27\python.exe -m pip install -r requirements.txt


ECHO *** Subindo o servidor PlantSearch ***
\Python27\python.exe PlantSearch.py

Pause


