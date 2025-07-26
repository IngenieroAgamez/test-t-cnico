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
