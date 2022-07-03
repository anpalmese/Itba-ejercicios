import csv
from hashlib import new
import pathlib
import os
import datetime
import time

def convertir_fecha_timestamp(fecha):
    fecha = fecha.timetuple()
    resultado = time.mktime(fecha)
    
    return resultado

ahora = datetime.datetime.now()


def registro_cheques(info):
    cantidad_cheques = int(input('¿Cuantos cheques desea registrar? '))
    campos = ['NroCheque','CodigoBanco','CodigoSucursal','NumeroCuentaOrigen','NumeroCuentaDestino','Valor','FechaOrigen','FechaPago','DNI','Estado','Tipo']

    if not pathlib.Path(info).exists():
        with open(info,'w',newline='') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=campos)
            writer.writeheader()
    
    with open(info,'a', newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        for i in range(cantidad_cheques):
            os.system('cls')
            NroCheque = input('Ingrese el numero del cheque: ')
            CodigoBanco = input('Ingrese el codigo de banco: ')
            CodigoSucursal = input('Ingrese el codigo de sucursal: ')
            NumeroCuentaOrigen = input('Ingrese el numero de la cuenta de origen: ')
            NumeroCuentaDestino = input('Ingrese el numero de la cuenta de destino:')
            Valor = input('Ingrese el valor del cheque: ')
            FechaOrigen = convertir_fecha_timestamp(ahora)
            FechaPago = convertir_fecha_timestamp(ahora)
            DNI = input('Ingrese su DNI: ')
            Estado = input('Ingrese el estado del cheque: ')
            Tipo = input('Ingrese el tipo del cheque:')
            writer.writerow({'NroCheque': NroCheque, 'CodigoBanco':CodigoBanco, 'CodigoSucursal':CodigoSucursal,'NumeroCuentaOrigen':NumeroCuentaOrigen,'NumeroCuentaDestino':NumeroCuentaDestino,'Valor':Valor,'FechaOrigen':FechaOrigen,'FechaPago':FechaPago, 'DNI': DNI,'Estado':Estado, 'Tipo': Tipo})

def mostrar_cheques(info):
    os.system('cls')
    with open(info, 'r', newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        filtro = input('ingrese su DNI: ')
        opcion = input('Emitidos(1) o Depositados(2)?: ')
        if(opcion=='1'):
            buscar = 'emitido'
        if(opcion=='2'):
            buscar = 'depositado'
        os.system('cls')
        for row in reader:
            if(row['DNI'] == filtro and row['Tipo'] == buscar):
                for campo , valor in row.items():
                    print(f'{campo}: {valor}')
                print('~'*50)

def main():
    archivo = 'Datos_de_Cheques.csv'
    operacion = input('Que operacion desea realizar? registrar(1) o revisar(2)')
    if(operacion == '1'):
        registro_cheques(archivo)
    
    if(operacion == '2'):
        mostrar_cheques(archivo)

if __name__ == '__main__':
    main()