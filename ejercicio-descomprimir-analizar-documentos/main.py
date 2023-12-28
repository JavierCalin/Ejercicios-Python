"""Ejercicio del día 9, navegar estructura de carpetas y encontrar coincidencias en u pator regex"""
import os
from pathlib import Path
import re
import time
import math
from datetime import datetime
from tabulate import tabulate

bbdd_ruta = Path(os.getcwd(),'Mi_Gran_Directorio')
PATRON = r'N\w{3}\-\d{5}'
result_list = []

inicio = time.time()

for (root,dirs,files) in os.walk(bbdd_ruta,topdown=True):
    for file in files:
        archivo = open(Path(root,file), encoding="utf-8")
        coincidencia = re.search(PATRON,archivo.read())
        if coincidencia:
            result_list.append([file, coincidencia.group()])
final = time.time()

print("-"*20)
print(f'Fecha de búsqueda: {datetime.now().strftime("%d/%m/%Y")}')
print(tabulate(result_list, headers=['ARCHIVO','NRO SERIE']))
print(f'Números encontrados: {len(result_list)}')
print(f'Duración de la búsqueda: {math.ceil(final-inicio)}')
print("-"*20)
