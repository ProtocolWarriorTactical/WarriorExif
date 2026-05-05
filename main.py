import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import sys
import pikepdf
from docx import Document
from pptx import Presentation

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class WarriorExifGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WarriorExif v1.0 | ProtocolWarriorTactical")
        self.geometry("600x400")
        
        icon_path = resource_path("icon.ico")
        if os.path.exists(icon_path) and sys.platform.startswith('win'):
            self.iconbitmap(icon_path)

        self.label = ctk.CTkLabel(self, text="SANEAMIENTO UNIVERSAL DE METADATOS", font=("Roboto", 20, "bold"))
        self.label.pack(pady=20)

        self.btn_select = ctk.CTkButton(self, text="SELECCIONAR ARCHIVO (IMG, PDF, OFFICE)", 
                                        command=self.procesar_archivo, height=50)
        self.btn_select.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Estado: Sistema Listo", text_color="gray")
        self.status_label.pack(pady=10)

    def limpiar_img(self, ruta, destino):
        img = Image.open(ruta)
        data = list(img.getdata())
        img_sin_exif = Image.new(img.mode, img.size)
        img_sin_exif.putdata(data)
        img_sin_exif.save(destino)

    def limpiar_pdf(self, ruta, destino):
        with pikepdf.open(ruta) as pdf:
            del pdf.Root.Metadata
            pdf.save(destino)

    def limpiar_office(self, ruta, destino, tipo):
        from datetime import datetime
        doc = Document(ruta) if tipo == "docx" else Presentation(ruta)
        prop = doc.core_properties
        
        # Campos de texto: se pueden poner en blanco o None
        text_props = ['author', 'category', 'comments', 'content_status', 
                      'identifier', 'keywords', 'last_modified_by', 
                      'language', 'subject', 'title', 'version']
        
        # Campos de fecha: requieren un manejo especial
        date_props = ['created', 'last_printed', 'modified']

        for p in text_props:
            setattr(prop, p, "") # Usamos cadena vacía en lugar de None
            
        # Para las fechas, si None falla, usamos una fecha base neutra (ej. año 1980 o 2000)
        fecha_neutral = datetime(2000, 1, 1)
        for p in date_props:
            try:
                setattr(prop, p, None)
            except:
                setattr(prop, p, fecha_neutral)

        doc.save(destino)
    def procesar_archivo(self):
        tipos = [("Todos los archivos", "*.jpg *.jpeg *.png *.pdf *.docx *.pptx")]
        archivo = filedialog.askopenfilename(filetypes=tipos)
        if archivo:
            ext = archivo.split('.')[-1].lower()
            nombre_final = f"CLEAN_{os.path.basename(archivo)}"
            ruta_final = os.path.join(os.path.dirname(archivo), nombre_final)
            
            try:
                self.status_label.configure(text=f"Saneando {ext.upper()}...", text_color="#3498db")
                self.update()

                if ext in ['jpg', 'jpeg', 'png']:
                    self.limpiar_img(archivo, ruta_final)
                elif ext == 'pdf':
                    self.limpiar_pdf(archivo, ruta_final)
                elif ext in ['docx', 'pptx']:
                    self.limpiar_office(archivo, ruta_final, ext)
                
                messagebox.showinfo("ÉXITO", f"Archivo saneado: {nombre_final}")
                self.status_label.configure(text="Estado: Operación Exitosa", text_color="#2ecc71")
            except Exception as e:
                messagebox.showerror("ERROR", f"Fallo: {str(e)}")

if __name__ == "__main__":
    app = WarriorExifGUI()
    app.mainloop()