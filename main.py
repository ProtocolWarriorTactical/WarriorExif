import os
from PIL import Image
import threading

def limpiar_imagen(ruta):
    try:
        img = Image.open(ruta)
        # Al guardar sin los datos EXIF, se crea una copia limpia
        datos_limpios = list(img.getdata())
        nueva_img = Image.new(img.mode, img.size)
        nueva_img.putdata(datos_limpios)
        nueva_img.save(ruta)
        print(f"[+] Metadatos eliminados: {ruta}")
    except Exception as e:
        print(f"[-] Error en {ruta}: {e}")

def inicio():
    print("--- WarriorExif v1.0 | ProtocolWarriorTactical ---")
    ruta_objetivo = input("Introduce la ruta del archivo o carpeta: ")
    
    if os.path.isfile(ruta_objetivo):
        limpiar_imagen(ruta_objetivo)
    elif os.path.isdir(ruta_objetivo):
        for archivo in os.listdir(ruta_objetivo):
            if archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
                limpiar_imagen(os.path.join(ruta_objetivo, archivo))
    
    print("\n[!] Proceso finalizado. Archivos saneados.")

if __name__ == "__main__":
    inicio()