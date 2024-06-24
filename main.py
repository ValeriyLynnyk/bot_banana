import os
import subprocess

def ejecutar_exe(RUTA):
    try:
        subprocess.call([RUTA], shell=True)
    except:
        return "Error al ejecutar el archivo: {e}"

def main():
    # RUTA_ARCHIVO = 'D:\Steam\steamapps\common\Banana\Banana.exe'
    RUTA_DIRECTORIO = 'D:/Steam/steamapps/common/Banana/'
    ARCHIVO = 'Banana.exe'
    RUTA = RUTA_DIRECTORIO + ARCHIVO
    # ruta = input("Ingrese la ruta del archivo a leer: ")
    # contenido = leer_archivo(ruta)
    print(ejecutar_exe(RUTA))

if __name__ == "__main__":
    main()