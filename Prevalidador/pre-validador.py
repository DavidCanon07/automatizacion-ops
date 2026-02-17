import pandas as pd
from Ingesta import concatenar_datos, validar_largo_campos
from datetime import datetime


try: 
    df = concatenar_datos()
    print("Validación de campos iniciada...")
    df = df.drop(columns=["Unnamed: 0","Unnamed: 1"], errors="ignore")
    print(df)
    try:
        validar_largo_campos(df)
    except Exception as e:
        error_msg = str(e)
        print(error_msg)
        with open("C:\\Users\\usuario\\OneDrive\\Documentos\\GitHub\\automatizacion OPS\\Prevalidador\\archivos\\errores.txt", "a", encoding="utf-8") as f:
            f.write(f"\n-------02 - Validación de largo de campos.--------\n")
            f.write(f"\nLog de error: {datetime.now()} - {error_msg}\n")
            exit()
    #df.to_excel("C:\\Users\\usuario\\OneDrive\\Documentos\\GitHub\\automatizacion OPS\\Prevalidador\\archivos\\datos_concatenados.xlsx", index=True)
except Exception as e:
    error_msg = str(e)
    print(error_msg)
    
    #guardar el error en un archivo de texto
    with open("C:\\Users\\usuario\\OneDrive\\Documentos\\GitHub\\automatizacion OPS\\Prevalidador\\archivos\\errores.txt", "a", encoding="utf-8") as f:
        f.write(f"\n-------01 - Validación de columnas Y entrada de archivos.--------\n")
        f.write(f"\nLog de error: {datetime.now()} - {error_msg}\n")
    print("El error ha sido registrado en errores.txt")
    exit()  # Salir con código de error para indicar que hubo un problema



