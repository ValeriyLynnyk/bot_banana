import os

def listar_directorio(ruta_directorio):
    try:
        # Lista los archivos y directorios en 'ruta_directorio'
        contenido = os.listdir(ruta_directorio)
        return contenido
    except FileNotFoundError:
        return FileNotFoundError
    except PermissionError:
        return PermissionError

def main():
    RUTA_DIRECTORIO = 'D:/Steam/steamapps/common/Banana/'  # Cambia '.' por cualquier ruta de directorio específica
    contenido_directorio = listar_directorio(RUTA_DIRECTORIO)
    if contenido_directorio == FileNotFoundError | PermissionError:
        print(contenido_directorio)
    else:
        for elemento in contenido_directorio:
            print(elemento)

if __name__ == "__main__":
    main()