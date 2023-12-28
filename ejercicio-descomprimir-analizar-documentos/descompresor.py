import shutil
import os

ruta_main = os.getcwd()
archivo = 'ProyectoDia9.zip'
shutil.unpack_archive(f'{ruta_main}/{archivo}',ruta_main,'zip')