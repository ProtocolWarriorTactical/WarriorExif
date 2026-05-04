# WarriorExif
Herramienta de saneamiento de metadatos para guerreros de la privacidad.

## Características Actuales
- Borrado total de metadatos EXIF en imágenes (JPG, JPEG, PNG).
- Sobrescritura aleatoria en archivos PDF para evitar rastreo histórico.
- Eliminación de mapas de metadatos en video vía FFmpeg sin pérdida de calidad.
- Interfaz gráfica minimalista y segura.

## Roadmap 2026 (Próximas Actualizaciones)
- **V1.1:** Soporte para procesamiento por lotes y carpetas completas.
- **V1.2:** Inyección de metadatos señuelo (Decoy Profiles) para despistar analistas.
- **V2.0:** Motor de ofuscación de huella de sensor (Anti-Forensics) para romper el patrón único de la cámara.

## Compilación (Build)
Para crear el .exe en Windows:
`pyinstaller --noconsole --onefile --name WarriorExif main.py`

Para crear el binario en Linux:
`pyinstaller --onefile --name WarriorExif main.py`