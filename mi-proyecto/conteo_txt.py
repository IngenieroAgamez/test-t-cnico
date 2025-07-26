import os

# Obtener la lista de archivos en el directorio actual
archivos = os.listdir('.')

# Filtrar los archivos que terminan en .txt
txt_files = [archivo for archivo in archivos if archivo.endswith('.txt')]

# Imprimir los nombres de los archivos .txt encontrados
print("Archivos .txt encontrados:")
for nombre in txt_files:
    print(nombre)

# Guardar la lista en un nuevo archivo llamado lista_txt.txt
with open('lista_txt.txt', 'w', encoding='utf-8') as f:
    for nombre in txt_files:
        f.write(nombre + '\n')

# Imprimir también cuántos archivos se encontraron
print(f"Total de archivos .txt encontrados: {len(txt_files)}")

# -------------------------------------------------------------
# Explicación del uso de IA para este reto
#
# Cómo formulé la pregunta a la IA:
# Le pregunté: "¿Cómo puedo contar todos los archivos .txt en el directorio actual
# usando Python nativo sin usar os.system, imprimir sus nombres y guardarlos en
# un archivo lista_txt.txt?"
#
# ¿Tuve que modificar la respuesta?
# Sí, la IA me sugirió inicialmente listar archivos con os y también ofreció ejemplos 
# usando os.system, pero modifiqué el código para utilizar únicamente os.listdir() 
# y asegurarlo al requisito de no usar os.system. Además, añadí la escritura de los 
# nombres en el archivo lista_txt.txt y la impresión del total de archivos encontrados.
#
# ¿Cómo verifiqué que el código funcionaba?
# Creé archivos de prueba con extensión .txt en la carpeta (por ejemplo, prueba1.txt y prueba2.txt),
# ejecuté el script con `python conteo_txt.py` y comprobé que:
# - Se imprimían los nombres correctamente en consola.
# - Se creaba el archivo lista_txt.txt con los nombres de los archivos .txt.
# - El conteo total coincidía con la cantidad de archivos de prueba creados.
# -------------------------------------------------------------
