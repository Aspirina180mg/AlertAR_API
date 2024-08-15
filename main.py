import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Endpoints de la API
# @profile
@app.get('/Inversor/{texto}')
async def Inversor(texto: str):
    """
    Devuelve el texto ingresado, pero invertido
    Si recibe números, los convierte automáticamente a texto y los invierte igualmente

    Parametros
    ----------
    texto : str
        El texto a invertir, puede ser caracteres, palabras o textos, técnicamente no hay límite para el largo.

    Devuelve
    -------
    str
        Una cadena de caracteres con el mismo texto que se ingresó, pero invertido.

    Ejemplo
    --------
    \>\>\> Invertir("anita lava la tina")

    >\> {'anit al aval atina'}
    """
    
    texto_invertido = texto[::-1]
    return texto_invertido