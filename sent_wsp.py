#pip install pywhatkit

import pywhatkit

try:
    pywhatkit.sendwhatmsg("+56981736721","Hola hola coca cola!",21,23)
    print("envio exitoso")
except:
    print("Ocurrio un error")