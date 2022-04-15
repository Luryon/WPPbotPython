import pywhatkit
from  nice_modules import *
from flask import Flask, request




def main():
    try:
        #Intentar enviar el mensaje
        pywhatkit.sendwhatmsg_instantly("+5492994043773","Mensaje de Prueba", 16)

    except:
        print("Mensaje no enviado")

if __name__ == '__main__':
    main()
